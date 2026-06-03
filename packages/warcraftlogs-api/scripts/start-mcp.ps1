param(
  [switch]$Check
)

$ErrorActionPreference = "Stop"

$packageRoot = Split-Path -Parent $PSScriptRoot
$envPath = Join-Path $packageRoot ".env.local"
$serverPath = Join-Path $packageRoot "dist\mcp\stdio.js"

if (-not (Test-Path -LiteralPath $envPath)) {
  throw "Missing env file: $envPath"
}

Get-Content -LiteralPath $envPath | ForEach-Object {
  $line = $_.Trim()
  if (-not $line -or $line.StartsWith("#")) {
    return
  }

  $line = $line -replace "^export\s+", ""
  $separator = $line.IndexOf("=")
  if ($separator -lt 1) {
    return
  }

  $name = $line.Substring(0, $separator).Trim()
  $value = $line.Substring($separator + 1).Trim()
  if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
    $value = $value.Substring(1, $value.Length - 2)
  }

  [Environment]::SetEnvironmentVariable($name, $value, "Process")
}

if ($Check) {
  foreach ($name in @("WARCRAFT_LOGS_CLIENT_ID", "WARCRAFT_LOGS_CLIENT_SECRET")) {
    if ([Environment]::GetEnvironmentVariable($name, "Process")) {
      Write-Output "$name=set"
    } else {
      Write-Output "$name=missing"
    }
  }
  exit 0
}

if (-not (Test-Path -LiteralPath $serverPath)) {
  throw "Missing built MCP server: $serverPath. Run npm run build first."
}

node $serverPath
