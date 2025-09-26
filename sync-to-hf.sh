#!/bin/bash
# sync-to-hf.sh - Manual sync script for Hugging Face Space

echo "🔄 Syncing BrandBoost to Hugging Face Space..."

# Configuration
HF_USERNAME="youtah"
HF_SPACE_NAME="brandboost-content-generator"
HF_SPACE_URL="https://huggingface.co/spaces/$HF_USERNAME/$HF_SPACE_NAME"

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Please run this script from the BrandBoost directory"
    exit 1
fi

# Clone or update HF Space
if [ -d "hf-space" ]; then
    echo "📁 Updating existing HF Space clone..."
    cd hf-space
    git pull origin main
    cd ..
else
    echo "📁 Cloning HF Space..."
    git clone $HF_SPACE_URL hf-space
fi

# Sync files (exclude git and cache files)
echo "🔄 Syncing files..."
rsync -av --delete \
    --exclude='.git' \
    --exclude='.github' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='hf-space' \
    --exclude='.DS_Store' \
    . hf-space/

# Commit and push changes
echo "💾 Committing changes..."
cd hf-space
git add .
git commit -m "Auto-sync from GitHub: $(date)" || echo "ℹ️ No changes to commit"
git push origin main

echo "✅ Successfully synced to Hugging Face Space!"
echo "🌐 Visit: $HF_SPACE_URL"
