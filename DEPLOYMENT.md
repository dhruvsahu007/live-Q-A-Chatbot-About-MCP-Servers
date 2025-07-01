# Deploying MCP Q&A Chatbot to Render

This guide walks you through deploying the MCP Q&A Chatbot to Render, a cloud platform for hosting web applications.

## Prerequisites

1. **GitHub Account**: You need a GitHub account to connect with Render
2. **OpenAI API Key**: Get your API key from [OpenAI Platform](https://platform.openai.com/account/api-keys)
3. **Git Installed**: Ensure Git is installed on your computer

## Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit - MCP Q&A Chatbot"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub](https://github.com) and create a new repository
   - Name it something like `mcp-qa-chatbot`
   - Don't initialize with README (we already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/mcp-qa-chatbot.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up/Login to Render**:
   - Go to [Render.com](https://render.com)
   - Sign up or login using your GitHub account

2. **Create a New Web Service**:
   - Click "New +" button in the dashboard
   - Select "Web Service"
   - Choose "Build and deploy from a Git repository"

3. **Connect Your Repository**:
   - Select your GitHub account
   - Choose the repository you just created
   - Click "Connect"

4. **Configure the Service**:
   ```
   Name: mcp-qa-chatbot (or your preferred name)
   Environment: Python 3
   Region: Choose closest to your users
   Branch: main
   Root Directory: (leave blank)
   Runtime: Python
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

5. **Set Environment Variables**:
   In the "Environment Variables" section, add:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   OPENAI_MODEL=gpt-3.5-turbo
   MAX_TOKENS=1000
   TEMPERATURE=0.7
   ```

6. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy your application
   - This process takes 2-5 minutes

### Step 3: Access Your Application

1. **Get Your URL**:
   - Once deployed, Render provides a URL like: `https://mcp-qa-chatbot.onrender.com`
   - Your application will be accessible at this URL

2. **Test the Application**:
   - Open the provided URL in your browser
   - Test the chatbot functionality
   - Try asking MCP-related questions

## Important Notes

### Free Tier Limitations
- **Sleep Mode**: Free services sleep after 15 minutes of inactivity
- **Spin-up Time**: Takes 30-60 seconds to wake up from sleep
- **Monthly Hours**: Limited to 750 hours per month

### Environment Variables Security
- ✅ **DO**: Set your OpenAI API key as an environment variable in Render
- ❌ **DON'T**: Include your API key in the code or push `.env` file to GitHub

### Updating Your Application
1. Make changes to your local code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push
   ```
3. Render will automatically redeploy

## Troubleshooting

### Common Issues

1. **Build Fails**:
   - Check that `requirements.txt` is in the root directory
   - Ensure all dependencies are properly listed
   - Check the build logs in Render dashboard

2. **Application Won't Start**:
   - Verify the start command is correct
   - Check that port configuration is proper
   - Review application logs

3. **OpenAI API Errors**:
   - Confirm your API key is correctly set in environment variables
   - Check that your OpenAI account has sufficient credits
   - Verify the API key has the correct permissions

4. **Slow Response**:
   - Free tier services sleep after inactivity
   - Consider upgrading to paid tier for better performance

### Useful Commands

```bash
# Check Git status
git status

# View commit history
git log --oneline

# Push latest changes
git add .
git commit -m "Your commit message"
git push
```

## Custom Domain (Optional)

If you want a custom domain:
1. Go to your service settings in Render
2. Click on "Custom Domains"
3. Add your domain and follow DNS configuration instructions

## Monitoring and Logs

- **Logs**: View real-time logs in the Render dashboard
- **Metrics**: Monitor CPU, memory usage, and response times
- **Alerts**: Set up alerts for downtime or errors

## Cost Optimization

### Free Tier Tips:
- Use the free tier for development and testing
- Monitor your usage hours
- Consider sleep/wake cycles for cost management

### Paid Tier Benefits:
- No sleep mode
- Better performance
- More monthly hours
- Priority support

## Support

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **OpenAI Documentation**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)

## Security Best Practices

1. **Never commit sensitive data**:
   - API keys
   - Passwords
   - Personal information

2. **Use environment variables** for all configuration
3. **Regularly rotate API keys**
4. **Monitor API usage** to detect unusual activity

---

Your MCP Q&A Chatbot is now live and accessible to users worldwide! 🚀
