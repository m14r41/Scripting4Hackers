# Google Photos Consolidation (PowerShell)

## Goal
- Collect **all images & videos** from Google Photos Takeout
- Ignore `.json` metadata files
- Avoid overwriting duplicate filenames

-  Assume we are **already in the current folder**
- **Create the destination directory**


### Step 1: Create destination folder
```powershell
mkdir All_Photos
````

## Script 1: Simple Copy (May Overwrite)

```powershell
Get-ChildItem ".\Google-Photos" -Recurse -File -Include *.jpg,*.jpeg,*.png,*.heic,*.gif,*.mp4,*.mov,*.avi,*.mkv | Copy-Item -Destination ".\All_Photos"

## Script 2: Duplicate-Safe Copy (Recommended)
```powershell
Get-ChildItem ".\Google-Photos" -Recurse -File -Include *.jpg,*.jpeg,*.png,*.heic,*.gif,*.mp4,*.mov,*.avi,*.mkv | ForEach-Object { $d=".\All_Photos\$($_.Name)"; if(Test-Path $d){$b=[IO.Path]::GetFileNameWithoutExtension($_.Name);$e=$_.Extension;$d=".\All_Photos\$b-$($_.LastWriteTime.Ticks)$e"}; Copy-Item $_.FullName $d }
```
