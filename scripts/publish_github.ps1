$ErrorActionPreference = "Stop"
$Owner = "Cloudlake110"
$Repo = "photo-decode"
$Description = "Photo Decode 解图 — turn any image into a five-block editorial visual deconstruction and flat reinterpretation board."

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  throw "GitHub CLI (gh) is required. Install it from https://cli.github.com/"
}

try { gh auth status --hostname github.com | Out-Null }
catch {
  gh auth login --hostname github.com --git-protocol https --web
}

gh auth setup-git

if (-not (Test-Path .git)) { git init -b main }

git add .
$staged = git diff --cached --name-only
if ($staged) { git commit -m "Release Photo Decode v1.0.0" }

$exists = $true
try { gh repo view "$Owner/$Repo" | Out-Null }
catch { $exists = $false }

if ($exists) {
  $origin = git remote 2>$null
  if ($origin -notcontains "origin") { git remote add origin "https://github.com/$Owner/$Repo.git" }
  git push -u origin main
} else {
  gh repo create "$Owner/$Repo" --public --description "$Description" --source=. --remote=origin --push
}

Write-Host "Published: https://github.com/$Owner/$Repo"
