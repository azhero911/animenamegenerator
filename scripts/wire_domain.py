#!/usr/bin/env python3
"""
wire_domain.py
Configures domain across all HTML pages, canonicals, sitemap, and robots.txt.
Removes noindex, nofollow and opens site for search indexing upon launch.

Usage:
  python scripts/wire_domain.py https://animenamevault.com
"""

import sys
import os
import re
import glob

def wire_domain(domain):
    if not domain:
        print("Error: Please provide a domain name (e.g. https://animenamevault.com)")
        sys.exit(1)

    # Normalize domain
    domain = domain.strip().rstrip('/')
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = f"https://{domain}"

    print(f"Wiring domain: {domain}")

    # Base domain without scheme
    clean_domain = domain.replace("https://", "").replace("http://", "")

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_files = glob.glob(os.path.join(root_dir, "*.html"))

    # 1. Update HTML files
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update canonical URLs
        content = re.sub(r'https://animenamevault\.com', domain, content)

        # Remove noindex, nofollow -> replace with index, follow
        content = re.sub(
            r'<meta name="robots" content="noindex, nofollow">',
            '<meta name="robots" content="index, follow">',
            content
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {os.path.basename(file_path)}")

    # 2. Update sitemap.xml
    sitemap_path = os.path.join(root_dir, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            s_content = f.read()
        s_content = re.sub(r'https://animenamevault\.com', domain, s_content)
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(s_content)
        print("Updated sitemap.xml")

    # 3. Update robots.txt
    robots_path = os.path.join(root_dir, "robots.txt")
    if os.path.exists(robots_path):
        new_robots = f"""# Production robots.txt
User-agent: *
Disallow:

Sitemap: {domain}/sitemap.xml
"""
        with open(robots_path, "w", encoding="utf-8") as f:
            f.write(new_robots)
        print("Updated robots.txt (search indexing enabled)")

    print(f"\n[SUCCESS] Successfully wired domain to {domain}!")
    print(f"- All HTML canonicals and OG tags updated to {domain}")
    print(f"- Pre-launch noindex tags removed (set to 'index, follow')")
    print(f"- robots.txt opened and sitemap declared at {domain}/sitemap.xml")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else ""
    wire_domain(target)
