# Publishing Photo Decode

## Why browser login and ChatGPT GitHub connection are different

Your normal GitHub browser session and the ChatGPT GitHub app are separate authentication contexts. ChatGPT must be separately authorized through its own OAuth connection and repository access settings.

More importantly, the GitHub app inside standard ChatGPT is designed for repository **read/search** access. It does not provide repository write/push capability. For write operations, use Codex or a local authenticated Git/GitHub CLI workflow.

## Fastest GitHub publish path (macOS/Linux)

From the repository root:

```bash
./scripts/publish_github.sh
```

The script uses `gh auth login --web` when needed. That opens GitHub in your browser, so your existing browser login can complete the OAuth authorization without pasting a token into chat.

It then:

1. configures Git authentication;
2. initializes Git if needed;
3. commits the current repository;
4. creates `Cloudlake110/photo-decode` if it does not exist;
5. pushes `main`.

## Windows

```powershell
./scripts/publish_github.ps1
```

## Security

Do **not** paste a GitHub personal access token into ChatGPT. Browser-based GitHub CLI authorization is preferred for this workflow.

## Example-image rights check

The repository includes a development gallery under `examples/gallery/`. Some boards embed their original source image in the left panel. Confirm redistribution rights for each source before making the repository public. Remove or replace any example whose source rights are unclear.
