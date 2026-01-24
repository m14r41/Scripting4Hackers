# Google Photos Consolidation (PowerShell)

## Goal
- Collect **all images & videos** from Google Photos Takeout
- Ignore `.json` metadata files
- Avoid overwriting duplicate filenames

## Prerequisites

* Ensure all downloaded files have been **unzipped**.
* Place the unzipped folders in a **single parent folder** for easy processing.
* Run in curent directory

 ### Run in curent directory
>  Recursively copies all image and video files from the current directory (excluding the All_Photos folder) into .\All_Photos, 
> renaming files with a timestamp if a name conflict occurs, and suppresses output like below
<img width="318" height="205" alt="image" src="https://github.com/user-attachments/assets/5338037a-3baf-4671-a068-caff972f9041" />



## Command : 1

> Collects all image and video files recursively into .\All_Photos, skipping files already there, avoiding duplicates by comparing SHA256 hashes, and renaming only when a different file with the same name exists
```
$dest=".\All_Photos"; if(!(Test-Path $dest)){New-Item -ItemType Directory $dest|Out-Null}; Get-ChildItem . -Recurse -File -Include *.jpg,*.jpeg,*.png,*.heic,*.gif,*.mp4,*.mov,*.avi,*.mkv | ? {$_.FullName -notmatch '\\All_Photos\\'} | % { $t=Join-Path $dest $_.Name; if(Test-Path $t){$h1=(Get-FileHash $_.FullName -Algorithm SHA256).Hash;$h2=(Get-FileHash $t -Algorithm SHA256).Hash; if($h1 -eq $h2){return}; $b=[IO.Path]::GetFileNameWithoutExtension($_.Name);$t=Join-Path $dest "$b-$h1$($_.Extension)"}; Copy-Item $_.FullName $t }
```

## Command : 2
> Copy all photos/videos to .\All_Photos, skip duplicates using SHA256, rename only if same name but different content
```
$dest=".\All_Photos"; if(-not (Test-Path $dest)) { New-Item -ItemType Directory $dest | Out-Null }; Get-ChildItem . -Recurse -File -Include *.jpg,*.jpeg,*.png,*.heic,*.gif,*.mp4,*.mov,*.avi,*.mkv | Where-Object { $_.FullName -notmatch '\\All_Photos\\' } | ForEach-Object { $target=Join-Path $dest $_.Name; if(Test-Path $target){ $hashSrc=(Get-FileHash $_.FullName -Algorithm SHA256).Hash; $hashDest=(Get-FileHash $target -Algorithm SHA256).Hash; if($hashSrc -eq $hashDest){ Continue }; $base=[IO.Path]::GetFileNameWithoutExtension($_.Name); $ext=$_.Extension; $target=Join-Path $dest "$base-$($hashSrc.Substring(0,16))$ext" }; Copy-Item $_.FullName $target }
```

