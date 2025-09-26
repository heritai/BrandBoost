# 🔄 GitHub Actions Setup for Auto-Sync to Hugging Face Spaces

This guide will help you set up automatic synchronization from your GitHub repository to your Hugging Face Space.

## 📋 Prerequisites

1. **GitHub Repository**: Your BrandBoost code is in a GitHub repository
2. **Hugging Face Space**: You have a Hugging Face Space created
3. **Hugging Face Token**: You need a Hugging Face access token

## 🔑 Step 1: Create Hugging Face Access Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click **"New token"**
3. **Token name**: `github-actions-sync`
4. **Token type**: `Write` (needed to push to spaces)
5. **Click "Generate a token"**
6. **Copy the token** (you'll need it for GitHub secrets)

## 🔐 Step 2: Add GitHub Secrets

1. Go to your GitHub repository: `https://github.com/heritai/BrandBoost`
2. Click **"Settings"** tab
3. In the left sidebar, click **"Secrets and variables"** → **"Actions"**
4. Click **"New repository secret"** and add these secrets:

### Required Secrets:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `HF_TOKEN` | `hf_xxxxxxxxxxxx` | Your Hugging Face access token |
| `HF_USERNAME` | `heritai` | Your Hugging Face username |
| `HF_SPACE_NAME` | `brandboost-content-generator` | Your Space name |

## 🚀 Step 3: Enable GitHub Actions

1. Go to your repository's **"Actions"** tab
2. Click **"I understand my workflows, go ahead and enable them"**
3. The workflow will automatically run on the next push to `main` branch

## ✅ Step 4: Test the Setup

1. **Make a small change** to any file in your repository
2. **Commit and push** the changes:
   ```bash
   git add .
   git commit -m "Test auto-sync to HF Space"
   git push origin main
   ```
3. **Check the Actions tab** to see the workflow running
4. **Visit your Hugging Face Space** to see the updates

## 🔍 How It Works

1. **Trigger**: Every push to the `main` branch
2. **Process**:
   - Checks out your GitHub repository
   - Clones your Hugging Face Space
   - Syncs all files (excluding .git, .github, cache files)
   - Commits and pushes changes to the Space
3. **Result**: Your Hugging Face Space is automatically updated

## 🛠️ Troubleshooting

### Workflow Fails
- **Check secrets**: Ensure all three secrets are correctly set
- **Check token permissions**: Make sure your HF token has write access
- **Check space name**: Verify the space name matches exactly

### Files Not Syncing
- **Check .gitignore**: Make sure important files aren't ignored
- **Check file paths**: Ensure all files are in the repository
- **Check permissions**: Verify the HF token has write access

### Manual Trigger
You can manually trigger the sync:
1. Go to **Actions** tab
2. Click **"Sync to Hugging Face Space"**
3. Click **"Run workflow"**

## 📊 Monitoring

- **Actions Tab**: Monitor workflow runs and any failures
- **Hugging Face Space**: Check that updates appear correctly
- **Logs**: View detailed logs in the Actions tab

## 🔄 Alternative: Manual Sync Script

If you prefer manual control, you can also use this script:

```bash
#!/bin/bash
# sync-to-hf.sh

# Clone HF Space
git clone https://huggingface.co/spaces/heritai/brandboost-content-generator hf-space
cd hf-space

# Sync files
rsync -av --exclude='.git' --exclude='.github' --exclude='__pycache__' --exclude='*.pyc' ../BrandBoost/ .

# Commit and push
git add .
git commit -m "Manual sync from GitHub"
git push origin main

echo "✅ Synced to Hugging Face Space!"
```

## 🎉 Success!

Once set up, every time you push changes to your GitHub repository, your Hugging Face Space will automatically update within a few minutes!

Your BrandBoost AI Content Generator will always stay in sync between GitHub and Hugging Face Spaces. 🚀
