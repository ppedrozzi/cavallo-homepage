# 🎯 HTML Content Capture Plan
## Objective
Update all HTML files in C:\Users\tk951\hubgit\cavallo-homepage to exactly match the current visible content at https://www.cavallomusic.ch/ as of today (2026-09-11).

## Explicit URL to HTML File Mapping

This is the definitive mapping between live website URLs and local HTML files:

| Live Website URL | Local HTML File | Section/Page Name |
|---------------|---------------|------------------|
| https://www.cavallomusic.ch/ | **index.html** | Homepage |
| https://www.cavallomusic.ch/mitgliedschaft | **membership.html** | Membership Page |
| https://www.cavallomusic.ch/verein | **verein.html** | Verein/About Section |
| https://www.cavallomusic.ch/kontakt | **kontakt.html** | Contact Page |
| https://www.cavallomusic.ch/jam-sessions-20132024 | **archive.html** | Jam Sessions Archive (2013-2024) |
| https://www.cavallomusic.ch/jam1 | **jam.html** | Jam Sessions Page |
| https://www.cavallomusic.ch/composer-jam | **composer-jam.html** | Composer Jam Page |

**Note**: The mapping shows exact 1:1 correspondence between website structure and local files.

## Background
The local HTML files appear to be outdated. We need to capture the ACTUAL current state of the website as it appears today, not rely on potentially old cached versions.

## Scope

### Files to Update (7 total):
1. index.html
2. membership.html
3. verein.html
4. kontakt.html
5. jam.html (mapped from jam-sessions-20132024)
6. composer-jam.html
7. archive.html

## Methodology

### Phase 1: Capture Current Website State (PRIMARY - Most Important)
**Action**: Use development tools to scrape the CURRENT visible content from each live URL

**Tools**:
- Browser developer tools (Chrome/Firefox)
- JavaScript-based content extraction to get fully rendered HTML
- Manual verification of each page

**Steps for each page**:
1. Open the URL in browser in incognito/private mode to avoid cache
2. Open DevTools (F12) → Elements tab to view full DOM structure
3. Copy the complete HTML content including all meta tags, scripts, and styles
4. Save as temporary file for comparison
5. Verify content is current (look for date stamps, "last updated" text, or recent event info)

**Verification Checklist**:
- [ ] Check "lastmod" dates in sitemap vs website content
- [ ] Look for any 2026 dates or recent event information on pages
- [ ] Verify images, styles, and scripts are loading from correct URLs
- [ ] Compare old HTML file content with newly captured content

### Phase 2: Content Comparison & Update (SECONDARY)
**Action**: Compare old vs new and update files only where content differs

**Process**:
1. For each mapped file: old-file.html vs newly-captured-content.html
2. Use diff tool to identify differences:
   - Git diff (if Git repo)
   - WinMerge or similar file comparison tool
   - Simple side-by-side comparison
3. Update only the changed sections, preserving layout structure
4. Maintain consistent formatting (indents, line breaks) across all files

### Phase 3: Validation (TERTIARY - Essential)
**Action**: Ensure updates reflect current website state

**Validation Steps**:
1. Open each updated HTML file in browser to verify rendering
2. Check for broken links/images
3. Validate HTML structure using W3C validator or browser console
4. Test mobile responsiveness if applicable
5. Verify semantic HTML structure is maintained

## Technical Considerations

### Caching Issues
**Important**: Some checks to perform:
- Clear browser cache before capturing
- Use Ctrl+F5 to full refresh each page
- Check CDN headers and cache-control metadata
- Look for "Wayback Machine" links suggesting content is archived
- Verify all elements (images, iframes) are from current sources

### Content Freshness Indicators
Look for evidence of recent updates:
- Future dates (2026) in event listings
- "Last updated" text with recent timestamps
- News sections with recent articles
- Event calendars with upcoming dates

### Format Consistency
Aim to maintain:
- Consistent HTML5 doctype
- Standard meta tags structure
- Consistent header/footer organization
- Similar class naming conventions
- Preserved accessibility features

### Backup Plan
Before any updates, create backups:
```
copy index.html index.html.backup
copy membership.html membership.html.backup
# ... etc for all 7 files
```

## Deliverables

### Final Output
Updated directory structure with current content:
```
C:\Users\tk951\hubgit\cavallo-homepage\
├── index.html (updated)
├── membership.html (updated)
├── verein.html (updated)
├── kontakt.html (updated)
├── jam.html (updated)
├── composer-jam.html (updated)
├── archive.html (updated)
└── CAPTURE_PLAN.md (this file)
```

### Documentation Required
After completion, document:
- Which files were updated (and why)
- Any discrepancies found between old and new content
- Any issues encountered (broken links, missing resources)
- Adjustments made for formatting consistency

## Success Criteria
✅ All 7 HTML files reflect the exact current state of the live website
✅ No outdated or incorrect information remains
✅ All navigational elements work correctly
✅ Visual styling is preserved/consistent
✅ HTML validates and passes basic quality checks

## Priority Order
1. **CAPTURE CURRENT STATE** - Most critical
2. Update files accordingly  
3. Validate changes
4. Document process

## Notes
- **DO NOT trust cached versions** - verify actual live content is being captured
- If website uses JavaScript to load content dynamically, ensure we capture the fully rendered DOM
- Timebox this task to avoid endless refinement - capture what's visible TODAY
- Focus on textual/content updates rather than perfect visual pixel matching

## Estimated Timeline
- Phase 1: 30-60 minutes (7 pages × 5-10 minutes each)
- Phase 2: 15-30 minutes (quick diff-based updates)
- Phase 3: 15-20 minutes (validation and testing)
- **Total: 60-110 minutes** (approximately 1-2 hours)

---
*Plan created: 2026-09-11*  
*Status: Ready for execution*
