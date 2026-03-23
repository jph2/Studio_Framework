# TEMPLATE FILE - DO NOT SHIP AS-IS
# Replace placeholders before production use.

param(
    [string]$Configuration = "Release",
    [string]$Framework = "net48"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$projectFile = Join-Path $repoRoot "RhinoUSDMultiExport.csproj"
$releasesDir = Join-Path $repoRoot "releases"

if (!(Test-Path $projectFile)) {
    throw "Project file not found: $projectFile"
}

New-Item -ItemType Directory -Force -Path $releasesDir | Out-Null

dotnet build $projectFile -c $Configuration -f $Framework

$rhpSource = Join-Path $repoRoot "bin\$Configuration\$Framework\RhinoUSDMultiExport.rhp"
if (!(Test-Path $rhpSource)) {
    throw "Expected .rhp not found: $rhpSource"
}

$rhpTarget = Join-Path $releasesDir "RhinoUSDMultiExport.rhp"
Copy-Item -Force $rhpSource $rhpTarget

Write-Host "[SUCCESS] Release built: $rhpTarget"
