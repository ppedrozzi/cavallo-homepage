# Cavallo Music - Homepage

A minimalist, static website for Kulturverein Cavallo Music, migrated from BaseKit to plain HTML/CSS.

## 🎵 About

This website serves as the online home for **Cavallo Music**, a cultural association organizing weekly jam sessions and concerts in Stäfa, Zürichsee, Switzerland.

**Key Features:**
- Weekly jam sessions (every Thursday during the season)
- Special events and concerts
- Composer-Jam sessions for original music
- Open to all musicians and music lovers

## 📁 Project Structure

```
cavallo-homepage/
├── index.html              # Home page (GIG)
├── jam.html                # Weekly jam sessions info
├── composer-jam.html       # Composer-Jam special events
├── membership.html         # Membership registration
├── verein.html             # About the association
├── kontakt.html            # Contact & team
├── archive.html            # Archive 2013-2026
├── cavallo.css             # Main stylesheet
└── pictures/               # Images
    ├── header-bg.png
    ├── save-the-dates-2026.jpg
    ├── gallery-1.jpg
    ├── gallery-2.jpg
    ├── gallery-3.jpg
    └── favicon.svg
```

## 🎨 Design Philosophy

This website follows a **minimalist approach** inspired by [kanzlei-sessions.ch](https://kanzlei-sessions.ch):

- **Dark theme** (#000924 background)
- **Blue accents** (#04a4db, #00AEEF)
- **Clean typography** (Playfair Display + Rubik)
- **No JavaScript dependencies**
- **Fully responsive** (mobile-first)
- **Fast loading** (minimal CSS, optimized images)

## 🚀 Deployment

### Option 1: GitHub Pages

1. Push this repository to GitHub
2. Go to Settings → Pages
3. Select `main` branch as source
4. Your site will be live at `https://[username].github.io/cavallo-homepage`

### Option 2: Netlify

1. Connect your GitHub repository to Netlify
2. Deploy automatically on every push
3. Custom domain support available

### Option 3: Traditional Hosting

Upload all files to your web server via FTP/SFTP.

## 📝 Content Updates

### Updating Events

Edit the relevant sections in `index.html`:

```html
<section class="event-section">
    <h2>SLOW UP</h2>
    <p>
        <time>Sonntag, 27. September 2026</time>
        <!-- Update event details here -->
    </p>
</section>
```

### Adding New Pages

1. Create a new `.html` file based on existing templates
2. Add navigation link in all pages
3. Update CSS if needed

### Changing Images

Replace images in the `pictures/` directory. Recommended formats:
- Photos: JPEG or WebP (optimized for web)
- Graphics: SVG (scalable)
- Favicon: SVG or ICO

## 🎯 SEO & Performance

- **Meta tags**: Unique titles and descriptions for each page
- **Open Graph**: Social media sharing optimized
- **Responsive**: Mobile-friendly design
- **Fast loading**: Minimal CSS, no JavaScript
- **Accessible**: Semantic HTML, proper headings

## 📊 Analytics (Optional)

To add analytics, insert tracking code before `</head>` in all pages:

```html
<!-- Google Analytics example -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
```

## 🔧 Customization

### Colors

Edit `cavallo.css` to change the color scheme:

```css
body {
    background-color: #000924;  /* Main background */
}

a {
    color: #04a4db;  /* Link color */
}

h2 {
    color: #00AEEF;  /* Heading accent */
}
```

### Fonts

The site uses Google Fonts (Playfair Display + Rubik). To change:

1. Update the `<link>` in `<head>`
2. Modify `font-family` in CSS

## 📱 Social Media

Current social media links:
- Facebook: [@cavallomusic](https://www.facebook.com/cavallomusic)
- Instagram: [@cavallomusic](https://instagram.com/cavallomusic)

Update links in all pages if needed.

## 🤝 Contributing

To contribute to this website:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This website is maintained by Kulturverein Cavallo Music.

## 📞 Contact

For questions or contributions:
- Email: info@cavallomusic.ch
- Website: [cavallomusic.ch](https://www.cavallomusic.ch)

---

**Built with ❤️ for the Zürichsee music community**
