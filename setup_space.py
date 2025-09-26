#!/usr/bin/env python3
"""
Setup script for Hugging Face Spaces deployment.
This script helps prepare the project for deployment.
"""

import os
import shutil
import subprocess
import sys

def check_requirements():
    """Check if required tools are installed."""
    print("🔍 Checking requirements...")
    
    # Check if git is available
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print("✅ Git is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    # Check if huggingface_hub is available
    try:
        import huggingface_hub
        print("✅ Hugging Face Hub is installed")
    except ImportError:
        print("❌ Hugging Face Hub is not installed. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "huggingface_hub"], check=True)
        print("✅ Hugging Face Hub installed")
    
    return True

def create_space_repo():
    """Create a new Hugging Face Space repository."""
    print("\n🚀 Creating Hugging Face Space...")
    
    space_name = input("Enter your space name (e.g., brandboost-content-generator): ").strip()
    if not space_name:
        space_name = "brandboost-content-generator"
    
    username = input("Enter your Hugging Face username: ").strip()
    if not username:
        print("❌ Username is required")
        return None
    
    try:
        from huggingface_hub import HfApi
        api = HfApi()
        
        # Create the space
        api.create_repo(
            repo_id=f"{username}/{space_name}",
            repo_type="space",
            space_sdk="streamlit",
            private=False
        )
        
        print(f"✅ Space created: https://huggingface.co/spaces/{username}/{space_name}")
        return f"{username}/{space_name}"
        
    except Exception as e:
        print(f"❌ Error creating space: {e}")
        return None

def prepare_files():
    """Prepare files for deployment."""
    print("\n📁 Preparing files for deployment...")
    
    # Check if all required files exist
    required_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "utils/generator.py",
        "utils/prompt_templates.py",
        "utils/visualization.py",
        "sample_data/products.csv"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files present")
    return True

def main():
    """Main setup function."""
    print("🚀 BrandBoost - Hugging Face Spaces Setup")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return 1
    
    # Prepare files
    if not prepare_files():
        return 1
    
    # Ask if user wants to create space
    create_space = input("\n🤔 Do you want to create a new Hugging Face Space? (y/n): ").lower().strip()
    
    if create_space == 'y':
        space_repo = create_space_repo()
        if space_repo:
            print(f"\n🎉 Setup complete!")
            print(f"📋 Next steps:")
            print(f"1. Clone your space: git clone https://huggingface.co/spaces/{space_repo}")
            print(f"2. Copy all files to the cloned directory")
            print(f"3. Commit and push: git add . && git commit -m 'Initial commit' && git push")
            print(f"4. Visit: https://huggingface.co/spaces/{space_repo}")
        else:
            return 1
    else:
        print("\n📋 Manual setup instructions:")
        print("1. Go to https://huggingface.co/spaces")
        print("2. Create a new Space with Streamlit SDK")
        print("3. Clone the repository")
        print("4. Copy all files from this project")
        print("5. Commit and push to deploy")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
