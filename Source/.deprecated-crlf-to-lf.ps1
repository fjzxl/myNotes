$ErrorActionPreference = 'Stop'
$root = 'D:\notes\myNotes'
$exts = @('*.md','*.txt','*.json','*.yml','*.yaml','*.xml','*.html','*.css','*.js','*.ts','*.cjs','*.mjs','.gitignore')
$files = Get-ChildItem -Path $root -Recurse -File -Include $exts -ErrorAction SilentlyContinue

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$report = foreach ($f in $files) {
  $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
  $hadBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF
  $crlfCount = 0; $bareCrCount = 0
  for ($i = 0; $i -lt $bytes.Length; $i++) {
    if ($bytes[$i] -eq 0x0D) {
      if ($i + 1 -lt $bytes.Length -and $bytes[$i+1] -eq 0x0A) { $crlfCount++; $i++ }
      else { $bareCrCount++ }
    }
  }
  $out = New-Object System.Collections.Generic.List[byte]
  $start = if ($hadBom) { 3 } else { 0 }
  for ($i = $start; $i -lt $bytes.Length; $i++) {
    if ($bytes[$i] -eq 0x0D) {
      $out.Add(0x0A)
      if ($i + 1 -lt $bytes.Length -and $bytes[$i+1] -eq 0x0A) { $i++ }
    } else {
      $out.Add($bytes[$i])
    }
  }
  [System.IO.File]::WriteAllBytes($f.FullName, $out.ToArray())
  [PSCustomObject]@{
    Path       = $f.FullName.Substring($root.Length)
    SizeBefore = $bytes.Length
    SizeAfter  = $out.Count
    CrlfFixed  = $crlfCount
    BareCrFixed= $bareCrCount
    HadBom     = $hadBom
  }
}
$report | Format-Table -AutoSize
""
"Total processed: $($report.Count)"
"Total CRLF->LF:  $(($report | Measure-Object -Property CrlfFixed -Sum).Sum)"
"Total bare CR:   $(($report | Measure-Object -Property BareCrFixed -Sum).Sum)"
"BOM stripped:    $(($report | Where-Object { $_.HadBom }).Count)"
