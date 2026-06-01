# Working folders

Every intern in the **Rethink-Labs** internship gets a personal folder in this directory. It's where you keep:

- **Your profile** — short bio, what project you're on, key links
- **Weekly progress reports** — one short markdown file per week
- **Work products** — anything you produce that lives here (notes, sketches, small scripts, design docs) rather than in a separate project repo

## How to create yours

1. **Copy the template:**

   ```bash
   cp -r working-folders/_template working-folders/<your-firstname>
   ```

   Use your first name only, lowercase, no spaces (e.g. `working-folders/jane`). If two interns share a first name, add a last-initial: `jane-d`.

2. **Edit `working-folders/<your-firstname>/README.md`** with your bio.

3. **Commit and push** on day one as your first PR.

## Layout inside each folder

```
working-folders/<your-firstname>/
├── README.md                    # Your profile (bio, project, links)
├── progress-reports/            # One file per week
│   └── README.md                # Format and cadence
└── workproducts/                # Anything you make
    └── README.md                # What goes here vs. a separate repo
```

## Rules

- **Edit only your own folder.** Don't push changes to another intern's folder without their PR review.
- **No secrets.** This repo is private but it's still on GitHub. API keys, customer data, anything sensitive — keep it out. Use 1Password or Zoho email instead.
- **Weekly progress reports are required.** Every Friday by EOD, push a new file under `progress-reports/`. See the template in `_template/progress-reports/README.md` for the format.
- **Work products that grow large get their own repo.** If a workproduct is more than ~20 files or has CI/tests, move it to a dedicated `<project>-<your-name>` repo under the org and link it from your README here.

## When you leave

Your folder stays — it's part of the program archive and useful for the next cohort to see real examples. Your manager and Arianna may archive or anonymize sensitive bits at offboarding.
