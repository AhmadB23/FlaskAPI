# Deploying FlaskAPI to Render

## Prerequisites
- A Render account (sign up at https://render.com)
- GitHub account
- Your code pushed to a GitHub repository

## Step-by-Step Deployment Guide

### 1. Prepare Your Repository

Make sure your repository has these files (already created):
- ✅ `requirements.txt` - Python dependencies (includes gunicorn)
- ✅ `build.sh` - Build script for Render
- ✅ `render.yaml` - Render infrastructure configuration
- ✅ `config/production.py` - Production configuration

### 2. Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare for Render deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/FlaskAPI.git

# Push to GitHub
git push -u origin main
```

### 3. Deploy on Render

#### Option A: Using Blueprint (Automated - Recommended)

1. Go to https://dashboard.render.com
2. Click **"New"** → **"Blueprint"**
3. Connect your GitHub repository
4. Select your FlaskAPI repository
5. Render will detect `render.yaml` and create:
   - PostgreSQL database
   - Web service
6. Click **"Apply"** to deploy

#### Option B: Manual Setup

##### Create PostgreSQL Database
1. Go to https://dashboard.render.com
2. Click **"New"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `flaskapi-db`
   - **Database**: `flaskapi`
   - **User**: `flaskapi_user`
   - **Region**: Choose closest to your users
   - **Plan**: Free tier or paid
4. Click **"Create Database"**
5. Copy the **Internal Database URL** (starts with `postgresql://`)

##### Create Web Service
1. Click **"New"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `flaskapi`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn run:app`
   - **Plan**: Free tier or paid

4. **Environment Variables** (click "Advanced"):
   ```
   FLASK_ENV=production
   PYTHON_VERSION=3.11.0
   SECRET_KEY=<click "Generate" for random value>
   JWT_SECRET_KEY=<click "Generate" for random value>
   DATABASE_URL=<paste Internal Database URL from step 5 above>
   ```

5. Click **"Create Web Service"**

### 4. Update Frontend Configuration

After deployment, update your frontend `config.js`:

```javascript
const CONFIG = {
    API_BASE_URL: 'https://your-app-name.onrender.com/api/v1',
    // ... rest of config
};
```

Replace `your-app-name` with your actual Render service name.

### 5. Seed Database (Optional)

After deployment, seed your database using Render Shell:

1. Go to your web service dashboard
2. Click **"Shell"** tab
3. Run seeding commands:
   ```bash
   python seed_categories_authors.py
   python seed_books.py
   python seed_admin.py
   python seed_users.py
   ```

### 6. Set Up Custom Domain (Optional)

1. In your web service settings
2. Go to **"Settings"** → **"Custom Domain"**
3. Add your domain and follow DNS configuration instructions

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `FLASK_ENV` | Environment mode | `production` |
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `JWT_SECRET_KEY` | JWT signing key | Auto-generated |
| `DATABASE_URL` | PostgreSQL connection string | From Render database |
| `PYTHON_VERSION` | Python version | `3.11.0` |
| `ALLOWED_ORIGINS` | CORS allowed origins (optional) | `https://yourdomain.com` |

## Important Notes

### Free Tier Limitations
- Web service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Database has 256 MB storage limit

### Production Checklist
- ✅ Never commit `.env` file
- ✅ Use strong, unique `SECRET_KEY` and `JWT_SECRET_KEY`
- ✅ Database URL uses `Internal Database URL` for better performance
- ✅ Enable "Auto-Deploy" for automatic deployments on git push
- ✅ Set up monitoring and alerts
- ✅ Configure backup strategy for database

### Troubleshooting

**Build Fails**
- Check build logs in Render dashboard
- Ensure `build.sh` has execute permissions: `git update-index --chmod=+x build.sh`
- Verify all dependencies in `requirements.txt`

**Database Connection Issues**
- Verify `DATABASE_URL` is set correctly
- Use **Internal Database URL** (not External)
- Check database is in the same region

**Migration Errors**
- Run migrations manually in Shell: `flask db upgrade`
- Check migration files in `migrations/versions/`

**CORS Errors**
- Add your frontend domain to `ALLOWED_ORIGINS` environment variable
- Format: `https://yourdomain.com` (no trailing slash)

## Monitoring Your Deployment

1. **Logs**: View real-time logs in Render dashboard
2. **Metrics**: Monitor CPU, memory, and request metrics
3. **Health Checks**: Render automatically monitors your service
4. **Alerts**: Set up email/Slack notifications for downtime

## Updating Your Deployment

After pushing changes to GitHub:
- If Auto-Deploy is enabled: Automatic deployment
- If not: Click **"Manual Deploy"** → **"Deploy latest commit"**

## Cost Estimation

**Free Tier**:
- Web Service: Free (with spin-down)
- PostgreSQL: Free (256 MB)
- Total: $0/month

**Starter Tier**:
- Web Service: $7/month (always on)
- PostgreSQL: $7/month (1 GB)
- Total: $14/month

## Support

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Flask Documentation: https://flask.palletsprojects.com
