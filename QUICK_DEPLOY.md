# Quick Render Deployment Guide

## Files Created for Deployment:
- ✅ `Procfile` - Tells Render how to start your app
- ✅ `runtime.txt` - Specifies Python version
- ✅ `.streamlit/config.toml` - Streamlit configuration for production
- ✅ `DEPLOYMENT.md` - Detailed deployment instructions
- ✅ `deploy.bat` / `deploy.sh` - Automated deployment scripts
- ✅ `health_check.py` - Application health monitoring

## Quick Deploy (5 minutes):

### 1. Prepare Repository
```bash
# Run this in your project directory
git init
git add .
git commit -m "Initial commit"
```

### 2. Push to GitHub
- Create new repository on GitHub
- Add remote: `git remote add origin YOUR_GITHUB_URL`
- Push: `git push -u origin main`

### 3. Deploy on Render
1. Go to [render.com](https://render.com)
2. Connect GitHub account
3. Create "Web Service"
4. Select your repository
5. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### 4. Set Environment Variables
Add in Render dashboard:
```
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=1000
TEMPERATURE=0.7
```

### 5. Deploy!
Click "Create Web Service" - Your app will be live in 2-3 minutes!

## Your App URL
After deployment: `https://your-app-name.onrender.com`

## Need Help?
See `DEPLOYMENT.md` for detailed instructions and troubleshooting.
