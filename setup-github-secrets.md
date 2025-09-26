# 🔐 GitHub Secrets Setup Guide

## Quick Fix for GitHub Actions Error

The error you're seeing means the GitHub secrets aren't properly configured. Follow these steps:

## Step 1: Go to GitHub Secrets

1. **Open your repository**: https://github.com/heritai/BrandBoost
2. **Click "Settings"** (top menu)
3. **Click "Secrets and variables"** → **"Actions"** (left sidebar)
4. **Click "New repository secret"** for each secret below

## Step 2: Add These Secrets

### Secret 1: HF_USERNAME
- **Name**: `HF_USERNAME`
- **Value**: `heritai`
- **Click "Add secret"**

### Secret 2: HF_SPACE_NAME
- **Name**: `HF_SPACE_NAME`
- **Value**: `[YOUR_ACTUAL_SPACE_NAME]`
- **Click "Add secret"**

> **Note**: Replace `[YOUR_ACTUAL_SPACE_NAME]` with your actual Hugging Face Space name. If you don't remember it, check your HF Space URL.

### Secret 3: HF_TOKEN
- **Name**: `HF_TOKEN`
- **Value**: `hf_xxxxxxxxxxxx` (your HF access token)
- **Click "Add secret"**

> **To get HF Token**: Go to https://huggingface.co/settings/tokens → "New token" → "Write" permission

## Step 3: Verify Secrets

You should now have 3 secrets:
- ✅ HF_USERNAME
- ✅ HF_SPACE_NAME  
- ✅ HF_TOKEN

## Step 4: Test the Workflow

1. **Make a small change** to any file
2. **Commit and push**:
   ```bash
   git add .
   git commit -m "Test GitHub Actions fix"
   git push origin main
   ```
3. **Check Actions tab** to see if it works

## 🔍 Troubleshooting

### Still Getting Empty Values?
- Double-check secret names are exactly: `HF_USERNAME`, `HF_SPACE_NAME`, `HF_TOKEN`
- Make sure there are no extra spaces in the values
- Try deleting and recreating the secrets

### Can't Find Your Space Name?
- Go to your Hugging Face Space
- Look at the URL: `https://huggingface.co/spaces/heritai/[SPACE_NAME]`
- Use the part after the last `/` as your space name

### Token Issues?
- Make sure your HF token has "Write" permissions
- Generate a new token if needed
- Make sure the token starts with `hf_`

## ✅ Success!

Once the secrets are properly configured, your GitHub Actions will automatically sync your code to your Hugging Face Space on every push!
