# Vercel Deployment Guide

## Prerequisites
- Vercel account
- Vercel CLI installed (`npm i -g vercel`)

## Deployment Steps

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy the project**:
   ```bash
   vercel
   ```

4. **For production deployment**:
   ```bash
   vercel --prod
   ```

## Configuration Files

- `vercel.json`: Main configuration for Vercel deployment
- `.vercelignore`: Files to exclude from deployment
- `requirements.txt`: Python dependencies

## Key Changes Made for Vercel

1. **Fixed API endpoints**: Changed from `http://localhost:5000/api/parse` to `/api/parse`
2. **Updated file handling**: Using `tempfile` instead of persistent upload folder
3. **Added Vercel configuration**: Proper routing and function settings
4. **Environment setup**: Added PYTHONPATH for proper module imports

## Testing Locally

To test the Vercel setup locally:

```bash
vercel dev
```

This will start a local development server that mimics the Vercel environment.

## Notes

- The app uses serverless functions with a 30-second timeout
- File uploads are handled using temporary files
- All static files (HTML, CSS, JS) are served directly by Vercel
- The Flask app is configured to work with Vercel's serverless environment
