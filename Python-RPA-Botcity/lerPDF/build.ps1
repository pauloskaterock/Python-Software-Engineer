$exclude = @("venv", "lerPDF.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "lerPDF.zip" -Force