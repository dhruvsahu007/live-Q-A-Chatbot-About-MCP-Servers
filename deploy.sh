#!/bin/bash
# Quick deployment script for Render

echo "🚀 Preparing MCP Q&A Chatbot for Render deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
fi

# Add all files
echo "📦 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
read -p "Enter commit message (or press Enter for default): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Deploy MCP Q&A Chatbot to Render"
fi
git commit -m "$commit_msg"

# Check if remote origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Add your GitHub repository URL:"
    read -p "Enter GitHub repo URL (https://github.com/username/repo.git): " repo_url
    git remote add origin "$repo_url"
fi

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "✅ Code pushed to GitHub!"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://render.com"
echo "2. Sign in with your GitHub account"
echo "3. Create a new Web Service"
echo "4. Connect your GitHub repository"
echo "5. Set these environment variables in Render:"
echo "   - OPENAI_API_KEY=your_api_key_here"
echo "   - OPENAI_MODEL=gpt-3.5-turbo"
echo "   - MAX_TOKENS=1000"
echo "   - TEMPERATURE=0.7"
echo "6. Deploy!"
echo ""
echo "📖 For detailed instructions, see DEPLOYMENT.md"
