# A&T Solutions SEO deployment notes

## What this package changes

The visible page body/layout is unchanged. SEO work is limited to page `<head>` metadata plus root support files.

### Implemented now
- Unique keyword-focused `<title>` and meta descriptions for all 3 pages.
- Explicit `robots` meta directives.
- Canonical URLs for the currently live GitHub Pages site.
- Open Graph and Twitter Card metadata.
- JSON-LD structured data: WebSite, Organization, WebPage/AboutPage/CollectionPage, BreadcrumbList, OfferCatalog and relevant Service items.
- `robots.txt` and `sitemap.xml`.
- Crawl-friendly internal HTML links already present in the original pages are preserved.
- Lightweight SVG favicon and `.nojekyll`.
- Contact form intentionally left unchanged.

## Target keyword plan

### Home (`index.html`)
Primary: security consulting; tactical training; security training; risk assessment.
Secondary: civilian critical response training; rapid-response teams; threat assessment; emergency preparedness; on-site security assessment; global security consulting.

### Training Programs (`programs.html`)
Primary: civilian critical response training; tactical training programs.
Secondary: situational awareness training; threat and vulnerability assessment; self-defense training; tactical medicine training; scene management training; CQB training; active shooter drills; non-lethal response training; civilian emergency preparedness.

### Who We Are (`who-we-are.html`)
Primary: security training experts; tactical training company; security consultants.
Secondary: civilian preparedness; community security training; rapid-response team formation; experienced security instructors; operational security experience.

No `meta keywords` tag is added; modern Google Search does not use it for ranking. The keyword plan is implemented through relevant page titles/descriptions and the existing page copy, which already naturally contains these concepts.

## Current canonical URL vs future domain

Until the custom domain actually serves this site, canonical/sitemap URLs point to:

`https://erezoren.github.io/A-T-SOLUTIONS/`

Future domain:

`https://attacticalsolutions.com/`

After DNS and GitHub Pages custom-domain setup are ready, run from the repo root:

```bash
python3 switch-to-domain.py
```

That rewrites canonical/Open Graph/JSON-LD/robots/sitemap URLs and activates the prepared `CNAME`. Commit and push the changes, then enable **Enforce HTTPS** in GitHub Pages.

## Google Search Console

This cannot be completed without ownership verification in the user's Google account. Once the live URL is deployed:
1. Add/verify the property in Google Search Console. For the future domain, prefer a Domain property.
2. Submit `https://erezoren.github.io/A-T-SOLUTIONS/sitemap.xml` now; after domain migration submit `https://attacticalsolutions.com/sitemap.xml`.
3. Use URL Inspection for the home page, `programs.html`, and `who-we-are.html`, then request indexing.
4. After the custom domain is live, keep the GitHub Pages version redirected/canonicalized to the custom domain through GitHub Pages' custom-domain behavior.

## Analytics

No analytics script is inserted because a real GA4 Measurement ID (or another analytics account/site ID) was not provided; inventing one would not collect data. When you have a GA4 Measurement ID such as `G-XXXXXXXXXX`, add the official Google tag to all three pages.

## Validation after deploy
- Confirm all 3 URLs return HTTP 200.
- Check `robots.txt` and `sitemap.xml` from the public site.
- Validate JSON-LD using Google's Rich Results Test and Schema.org validator.
- Run PageSpeed Insights/Core Web Vitals.
- Confirm canonical URL in Search Console URL Inspection.

## Suggested next organic SEO work (does change/add visible content, so intentionally NOT included)
- Add dedicated landing pages for major intent clusters (security consulting, risk assessment, civilian critical-response training, community/security-team training).
- Add proof/case studies, instructor credentials, FAQs, client sectors, and useful evergreen articles.
- Build legitimate relevant backlinks/mentions from partner organizations, training venues, industry directories, and client sites.
