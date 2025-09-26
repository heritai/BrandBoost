# 🚀 Deployment Guide - Hugging Face Spaces

This guide will help you deploy BrandBoost to Hugging Face Spaces.

## 📋 Prerequisites

1. **Hugging Face Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **Git**: Install Git on your system
3. **Hugging Face CLI**: Install with `pip install huggingface_hub`

## 🚀 Step-by-Step Deployment

### Step 1: Create a New Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Fill in the details:
   - **Space name**: `brandboost-content-generator`
   - **License**: `MIT`
   - **SDK**: `Streamlit`
   - **Hardware**: `CPU Basic` (free tier)
   - **Visibility**: `Public` (or Private if you prefer)

### Step 2: Clone the Space Repository

```bash
# Clone your space (replace YOUR_USERNAME with your HF username)
git clone https://huggingface.co/spaces/YOUR_USERNAME/brandboost-content-generator
cd brandboost-content-generator
```

### Step 3: Copy Project Files

Copy all files from this project to your cloned space:

```bash
# Copy all files (run from the BrandBoost directory)
cp -r * /path/to/your/cloned/space/
```

### Step 4: Commit and Push

```bash
# Add all files
git add .

# Commit changes
git commit -m "Initial commit: BrandBoost AI Content Generator"

# Push to Hugging Face
git push origin main
```

### Step 5: Verify Deployment

1. Go to your space URL: `https://huggingface.co/spaces/YOUR_USERNAME/brandboost-content-generator`
2. Wait for the build to complete (usually 2-3 minutes)
3. Test the application

## 🔧 Configuration

### Environment Variables (Optional)

If you need to set any environment variables, add them in the Space settings:

1. Go to your Space settings
2. Navigate to "Variables and secrets"
3. Add any required environment variables

### Hardware Upgrade (Optional)

For better performance, you can upgrade to:
- **CPU Upgrade**: Better performance for larger models
- **GPU**: For faster AI inference (paid)

## 📁 Required Files

Make sure these files are in your Space:

```
brandboost-content-generator/
├── app.py                    # Main Streamlit app
├── requirements.txt          # Python dependencies
├── README.md                # Space description
├── .gitignore               # Git ignore rules
├── utils/                   # Utility modules
│   ├── generator.py
│   ├── prompt_templates.py
│   └── visualization.py
├── sample_data/             # Product catalog
│   └── products.csv
└── reports/                 # Export directory
    └── example_report.pdf
```

## 🐛 Troubleshooting

### Common Issues

1. **Build Fails**: Check that all dependencies are in `requirements.txt`
2. **Import Errors**: Ensure all Python files are in the correct directories
3. **API Errors**: The app includes fallback content generation for reliability

### Debug Steps

1. Check the Space logs in the "Logs" tab
2. Test locally first: `streamlit run app.py`
3. Verify all file paths are correct

## 🔄 Updates

To update your Space:

```bash
# Make changes to your local files
# Then commit and push
git add .
git commit -m "Update: [describe changes]"
git push origin main
```

## 📊 Monitoring

- **Usage**: Check the "Metrics" tab in your Space
- **Logs**: Monitor the "Logs" tab for any errors
- **Performance**: Use the built-in analytics in the app

## 🎉 Success!

Once deployed, your BrandBoost AI Content Generator will be available at:
`https://huggingface.co/spaces/YOUR_USERNAME/brandboost-content-generator`

Share it with others and start generating amazing marketing content!
