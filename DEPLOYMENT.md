# 🚀 Deployment Guide

## Quick Deploy to Render.com (FREE)

### Step 1: Prepare GitHub Repository

```bash
cd GITHUB_READY
git init
git add .
git commit -m "Initial commit: PyQuotex API Server"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pyquotex-api.git
git push -u origin main
```

### Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure settings:

**Basic Settings:**
- **Name**: `pyquotex-api`
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`

**Build & Deploy:**
- **Build Command**: 
  ```
  pip install -r requirements.txt && playwright install
  ```
- **Start Command**: 
  ```
  uvicorn api:app --host 0.0.0.0 --port 10000
  ```

**Instance Type:**
- Select **Free** (0.1 CPU, 512 MB RAM)

### Step 3: Environment Variables

Add these in Render dashboard under "Environment":

```
PYQUOTEX_EMAIL=your_email@example.com
PYQUOTEX_PASSWORD=your_password_here
LOG_LEVEL=INFO
```

### Step 4: Deploy

Click **Create Web Service** and wait 5-10 minutes for deployment.

Your API will be live at: `https://your-app-name.onrender.com`

---

## Test Your Deployment

```bash
# Health check
curl https://your-app-name.onrender.com/health

# Get candles
curl "https://your-app-name.onrender.com/candles/last?asset=EURUSD_otc&count=10&period=60"
```

---

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Set environment variables
export PYQUOTEX_EMAIL="your_email@example.com"
export PYQUOTEX_PASSWORD="your_password"

# Run server
uvicorn api:app --host 0.0.0.0 --port 10000 --reload
```

Visit: http://localhost:10000/docs for interactive API documentation

---

## Troubleshooting

### Playwright Installation Issues

If deployment fails with playwright errors:

```bash
playwright install chromium
```

### Connection Issues

- Verify credentials are correct
- Check Quotex account is active
- Ensure no IP restrictions

### Memory Issues on Free Tier

Free tier has 512MB RAM limit. If issues occur:
- Reduce concurrent requests
- Consider upgrading to paid tier

---

## Monitoring

Render provides:
- **Logs**: View real-time logs in dashboard
- **Metrics**: CPU, memory, request stats
- **Alerts**: Set up email notifications

---

## Updating Your Deployment

```bash
git add .
git commit -m "Update: description"
git push origin main
```

Render will auto-deploy on push.

---

## Custom Domain (Optional)

1. Go to Settings → Custom Domain
2. Add your domain
3. Update DNS records as instructed

---

**Need Help?** Open an issue on GitHub
