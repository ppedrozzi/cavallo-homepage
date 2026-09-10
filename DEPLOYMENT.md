# 🚀 Quick Deployment Guide

## Push to GitHub

### Step 1: Create Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Fill in:
   - **Repository name**: `cavallo-homepage` (or your preferred name)
   - **Description**: "Cavallo Music - Kulturverein Stäfa"
   - **Visibility**: Public (recommended) or Private
   - **DO NOT** check "Initialize with README" (we already have one)
5. Click **"Create repository"**

### Step 2: Push Your Code

GitHub will show you commands to push an existing repository. Run these in your terminal:

```bash
cd C:\Users\tk951\hubgit\cavallo-homepage
git remote add origin https://github.com/YOUR_USERNAME/cavallo-homepage.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Step 3: Verify Push

After pushing, refresh your GitHub repository page. You should see all your files.

---

## Enable GitHub Pages (Free Hosting)

### Step 1: Go to Settings

1. In your GitHub repository, click **"Settings"** tab
2. Scroll down to **"Pages"** in the left sidebar

### Step 2: Configure Pages

1. Under **"Source"**, select:
   - Branch: **main**
   - Folder: **/ (root)**
2. Click **"Save"**

### Step 3: Wait for Deployment

GitHub will build your site (takes 1-2 minutes). You'll see:

```
Your site is live at https://YOUR_USERNAME.github.io/cavallo-homepage/
```

### Step 4: Test Your Site

Click the link to view your live website!

---

## Custom Domain (Optional)

If you want to use `www.cavallomusic.ch`:

### Step 1: Add CNAME File

Create a file named `CNAME` (no extension) in your repository root with:

```
www.cavallomusic.ch
```

### Step 2: Update DNS Records

At your domain registrar (hoststar.ch), add:

**Type**: CNAME  
**Name**: www  
**Value**: YOUR_USERNAME.github.io  

### Step 3: Update GitHub Pages Settings

1. Go to Settings → Pages
2. Under **"Custom domain"**, enter: `www.cavallomusic.ch`
3. Click **"Save"**
4. Check **"Enforce HTTPS"** (after DNS propagates)

---

## Alternative: Netlify Deployment

### Option A: Git Integration

1. Go to [netlify.com](https://netlify.com)
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect your GitHub account
4. Select your `cavallo-homepage` repository
5. Click **"Deploy site"**

### Option B: Drag & Drop

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the `cavallo-homepage` folder
3. Your site is live instantly!

---

## Alternative: Traditional Web Hosting

### Upload via FTP

1. Get FTP credentials from your hosting provider (hoststar.ch)
2. Use FTP client (FileZilla, WinSCP)
3. Upload all files to your web root:
   - All `.html` files
   - `cavallo.css`
   - `pictures/` folder
   - `README.md` (optional)

### Directory Structure on Server

```
/public_html/
├── index.html
├── jam.html
├── composer-jam.html
├── membership.html
├── verein.html
├── kontakt.html
├── archive.html
├── cavallo.css
└── pictures/
```

---

## Post-Deployment Checklist

- [ ] Test all navigation links
- [ ] Verify images load correctly
- [ ] Check mobile responsiveness
- [ ] Test contact form (mailto links)
- [ ] Verify social media links
- [ ] Check page load speed
- [ ] Test in multiple browsers (Chrome, Firefox, Safari)
- [ ] Update Google Maps links with exact locations

---

## Updating Your Website

### Making Changes

1. Edit files locally
2. Test in browser
3. Commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
4. GitHub Pages auto-deploys in 1-2 minutes

### Adding New Pages

1. Create new `.html` file (copy existing template)
2. Add navigation link in all pages
3. Commit and push

### Updating Images

1. Replace image in `pictures/` folder
2. Keep same filename (or update HTML reference)
3. Commit and push

---

## Troubleshooting

### Site Not Loading

- Check that `index.html` is in the root directory
- Verify GitHub Pages is enabled in Settings
- Wait 2-3 minutes for deployment

### Images Not Showing

- Check file paths are relative: `pictures/image.jpg`
- Verify image files exist in `pictures/` folder
- Check file extensions (.jpg vs .jpeg)

### CSS Not Applying

- Verify `cavallo.css` is in the root directory
- Check `<link>` tag in HTML `<head>`
- Clear browser cache (Ctrl+F5)

### 404 Errors

- Ensure all internal links have `.html` extension
- Check for typos in filenames
- Verify files were pushed to GitHub

---

## Need Help?

- **GitHub Pages Docs**: https://pages.github.com/
- **Netlify Docs**: https://docs.netlify.com/
- **HTML/CSS Reference**: https://developer.mozilla.org/

---

**Good luck with your deployment! 🎵**
