param (
    [Parameter(Mandatory=$true)]
    [string]$Domain
)

Write-Host "Running domain wiring script for: $Domain"
python scripts/wire_domain.py "$Domain"
