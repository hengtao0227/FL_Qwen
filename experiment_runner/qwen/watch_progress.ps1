param(
    [string]$RunDirectory = '.\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only',
    [int]$RefreshSeconds = 5
)

$ErrorActionPreference = 'Stop'
$RunDirectory = (Resolve-Path -LiteralPath $RunDirectory).Path
$PlanPath = Join-Path $RunDirectory 'plan.json'
$RunsPath = Join-Path $RunDirectory 'runs'
$PipelineStatusPath = Join-Path $RunDirectory 'pipeline_status.json'

function Read-JsonShared([string]$Path) {
    $Share = [System.IO.FileShare]::ReadWrite -bor [System.IO.FileShare]::Delete
    $Stream = [System.IO.File]::Open(
        $Path, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Read, $Share)
    try {
        $Reader = New-Object System.IO.StreamReader($Stream, [System.Text.Encoding]::UTF8, $true)
        try { return ($Reader.ReadToEnd() | ConvertFrom-Json) }
        finally { $Reader.Dispose() }
    } finally {
        $Stream.Dispose()
    }
}

if (-not (Test-Path -LiteralPath $PlanPath)) {
    throw "Missing plan.json: $PlanPath"
}

$Plan = Read-JsonShared $PlanPath
$Planned = @($Plan.jobs).Count
if ($Planned -le 0) {
    throw 'The frozen plan contains no jobs.'
}

Write-Host "Monitoring: $RunDirectory"
Write-Host 'This monitor is read-only. Press Ctrl+C to close it; the experiment will continue.'

while ($true) {
    $Rows = @(
        Get-ChildItem -LiteralPath $RunsPath -Recurse -Filter metrics.json -File -ErrorAction SilentlyContinue |
            ForEach-Object {
                try { Read-JsonShared $_.FullName } catch { }
            }
    )

    $CompletedCases = @(
        $Rows |
            Where-Object { $_.status -eq 'completed' -and $_.prediction_valid -eq $true } |
            Select-Object -ExpandProperty case_id -Unique
    )
    $Completed = $CompletedCases.Count
    # Use a floating-point Min overload; an integer 100 would round 1.3 down to 1.
    $Percent = [Math]::Min(100.0, [Math]::Round(100.0 * $Completed / $Planned, 1))
    $Active = @($Rows | Where-Object { $_.status -in @('preparing', 'running') } |
        Sort-Object started_at | Select-Object -Last 1)
    $CurrentCase = if ($Active.Count) { $Active[0].case_id } else { 'waiting/finalizing' }
    $AttemptCount = $Rows.Count
    $RetryCount = [Math]::Max(0, $AttemptCount - @($Rows | Select-Object -ExpandProperty case_id -Unique).Count)
    $FailedAttempts = @($Rows | Where-Object {
        $_.status -notin @('completed', 'preparing', 'running')
    }).Count
    $WallSeconds = ($Rows | Where-Object { $null -ne $_.wall_seconds } |
        Measure-Object -Property wall_seconds -Sum).Sum
    if ($null -eq $WallSeconds) { $WallSeconds = 0 }
    $KnownCost = ($Rows | Where-Object { $null -ne $_.estimated_cost_cny } |
        Measure-Object -Property estimated_cost_cny -Sum).Sum
    if ($null -eq $KnownCost) { $KnownCost = 0 }
    $UnknownCost = @($Rows | Where-Object {
        $_.process_started -eq $true -and $null -eq $_.estimated_cost_cny
    }).Count

    $Status = "{0:N1}% | {1}/{2} valid | current {3} | failed attempts {4}" -f `
        $Percent, $Completed, $Planned, $CurrentCase, $FailedAttempts
    $Details = "attempts {0} | retries {1} | cumulative {2:N2}h | estimated CNY {3:N3} | unknown cost {4}" -f `
        $AttemptCount, $RetryCount, ($WallSeconds / 3600), $KnownCost, $UnknownCost
    Write-Progress -Activity 'Qwen 395 fault-localization experiment' `
        -Status $Status -CurrentOperation $Details -PercentComplete $Percent

    $PipelineState = $null
    if (Test-Path -LiteralPath $PipelineStatusPath) {
        try {
            $PipelineState = (Read-JsonShared $PipelineStatusPath).state
        } catch { }
    }
    if ($PipelineState -in @('completed', 'blocked')) {
        Write-Progress -Activity 'Qwen 395 fault-localization experiment' -Completed
        Write-Host "Pipeline state: $PipelineState"
        break
    }

    Start-Sleep -Seconds $RefreshSeconds
}
