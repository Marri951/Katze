$name_list = Get-Content -Path ./hostnames.txt
foreach ($hostname in $name_list) {
    Add-Content -Path $env:windir\System32\drivers\etc\hosts -Value "`n127.0.0.1`t$($hostname)" -Force
}