# Anime Name Generator (Sumi & Shu Edition)

A high-performance, zero-dependency, pure static website built for authentic Japanese anime character name generation, onomastic research, and aesthetic usernames.

---

## 1. Page Map & Keyword Strategy

| # | URL | Primary Keyword | Secondary Keywords | Title Tag | H1 |
|---|-----|-----------------|--------------------|-----------|----|
| 1 | `/` | anime name generator | random anime name generator, anime character name generator, japanese anime name generator, anime oc name generator | Anime Name Generator: Random Japanese Names + Kanji | Anime Name Generator |
| 2 | `/anime-username-generator` | anime username generator | cool anime usernames, aesthetic anime usernames, anime username ideas | Anime Username Generator: Cool & Aesthetic Usernames | Anime Username Generator |
| 3 | `/anime-usernames-for-tiktok` | anime usernames for tiktok | anime tiktok names, anime tiktok username ideas | Anime Usernames for TikTok: Free Generator & Ideas | Anime Usernames for TikTok |
| 4 | `/anime-usernames-for-discord` | anime usernames for discord | anime discord names, anime discord nicknames | Anime Usernames for Discord: Free Generator & Ideas | Anime Usernames for Discord |
| 5 | `/anime-names-with-meaning` | anime names with meaning | anime names and meanings, anime name generator with kanji, japanese names with meanings | Anime Names With Meaning: Kanji, Romaji and Origins | Anime Names With Meaning |
| 6 | `/anime-last-name-generator` | anime last name generator | anime surname generator, anime surnames, japanese last names | Anime Last Name Generator: Japanese Surnames + Kanji | Anime Last Name Generator |
| 7 | `/anime-villain-name-generator` | anime villain name generator | anime villain names, dark anime names, evil anime names | Anime Villain Name Generator: Dark, Evil Names + Kanji | Anime Villain Name Generator |
| 8 | `/anime-boy-names` | anime boy names | anime name generator male, anime male names, japanese boy names | Anime Boy Names: Cool Japanese Male Names with Kanji | Anime Boy Names |
| 9 | `/anime-girl-names` | anime girl names | anime name generator female, anime female names, japanese girl names | Anime Girl Names: Cute Japanese Female Names with Kanji | Anime Girl Names |

### Trust & Housekeeping Pages
- `/about` - Mission statement, linguistic methodology, zero-dependency pledge.
- `/privacy` - Privacy-first policy: zero data collection, zero cookies, zero third-party trackers.
- `404.html` - Clean error page with noindex and direct links back to all generators.

---

## 2. Technical Architecture

- **Pure Static:** 100% Vanilla HTML5, CSS3, and JavaScript (ES6). No npm, no webpack, no build steps required.
- **Zero Dependencies:** No external CDNs, no third-party webfonts (system font stack with `font-display: swap`), no analytics scripts.
- **Pre-Rendered Fallback:** All pages load pre-filled name cards directly in the raw HTML. The page functions 100% even if JavaScript is disabled.
- **Accessibility:** WCAG AA compliant contrast ratios, visible `:focus-visible` rings, `aria-live` screen reader announcements, and native `<button>` controls.
- **Sumi & Shu Aesthetic:** Minimalist Japanese ink (`#111215`) and vermilion cinnabar (`#C8392B`) styling, authentic Hanko seals, and responsive typography.

---

## 3. SEO & Structured Data (JSON-LD)

- **Strict Length Validation:**
  - Titles: Strictly between 50 and 59 characters.
  - Meta Descriptions: Strictly between 144 and 160 characters, each containing the primary keyword once.
- **Structured Data:**
  - `WebSite` & `Organization` on homepage.
  - `WebApplication` on all 9 generator pages (Price: $0).
  - `BreadcrumbList` on all subpages (Home > Page Name).
  - `FAQPage` on all pages, matching visible FAQs word-for-word.
- **Zero Cross-Page Duplicate Names:** Over 225 curated names across 9 static tables with 0 overlap.

---

## 4. Pre-Launch Protection

All pages currently ship with:
- `<meta name="robots" content="noindex, nofollow">`
- `robots.txt` set to `Disallow: /`

This ensures that test deployments on staging or temporary domains (e.g., `*.vercel.app`) are never indexed by search engines.

---

## 5. Domain Launch Wiring Script

When you are ready to point the project to your live domain (e.g., `https://animenamevault.com`), run the wiring script:

### Linux / macOS / Git Bash:
```bash
./wire-domain.sh https://yourdomain.com
```

### Windows PowerShell:
```powershell
.\wire-domain.ps1 -Domain "https://yourdomain.com"
```

### What the script automates:
1. Updates all self-referencing canonical links and Open Graph tags across all HTML files.
2. Removes the `noindex, nofollow` tag and switches it to `index, follow`.
3. Opens `robots.txt` (`Disallow:`) and activates `Sitemap: https://yourdomain.com/sitemap.xml`.
4. Replaces placeholder URLs in `sitemap.xml` with your live domain.

---

## 6. How to Deploy to GitHub & Vercel

### Step A: Push to GitHub
```bash
git init
git add .
git commit -m "feat: complete anime name generator 9-page static suite"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/anime-name-generator.git
git push -u origin main
```

### Step B: Deploy to Vercel
1. Log in to [Vercel](https://vercel.com).
2. Click **Add New Project** and import the GitHub repository.
3. Framework Preset: **Other** (Static HTML).
4. Click **Deploy**. Vercel will automatically read `vercel.json` for clean URLs, security headers, and asset caching.
5. Once your custom domain is connected and DNS propagates, run `./wire-domain.sh https://yourdomain.com` and push the commit to open search indexing.
