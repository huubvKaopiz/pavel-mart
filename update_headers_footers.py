#!/usr/bin/env python3
# python3 update_headers_footers.py
"""
Script to update headers and footers in all HTML files to match index.html
"""

import re
import os

# List of HTML files to update (excluding index.html)
html_files = [
    'gioi-thieu.html',
    'hoat-dong-cong-dong.html',
    'tin-khuyen-mai.html',
    'uu-dai-dat-hang-online.html',
    'su-kien-tin-tuc.html',
    'khach-hang-thanh-vien.html',
    'thong-tin-lien-he.html',
    'he-thong-sieu-thi.html'
]

# Read index.html to extract header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (from <!-- Top Header Bar --> to </header>)
header_match = re.search(
    r'(<!-- Top Header Bar -->.*?</header>)',
    index_content,
    re.DOTALL
)
if not header_match:
    print("Error: Could not find header in index.html")
    exit(1)

new_header = header_match.group(1)

# Extract mobile menu (from <!-- Mobile Menu Modal --> to the closing script section before Hero)
mobile_menu_match = re.search(
    r'(<!-- Mobile Menu Modal -->.*?</div>\s*</div>)',
    index_content,
    re.DOTALL
)
if not mobile_menu_match:
    print("Error: Could not find mobile menu in index.html")
    exit(1)

new_mobile_menu = mobile_menu_match.group(1)

# Extract footer (from <!-- Footer --> to </footer>)
footer_match = re.search(
    r'(<!-- Footer -->.*?</footer>)',
    index_content,
    re.DOTALL
)
if not footer_match:
    print("Error: Could not find footer in index.html")
    exit(1)

new_footer = footer_match.group(1)

# Extract scroll to top button and scripts
scroll_and_scripts_match = re.search(
    r'(<!-- Scroll to Top Button -->.*?</script>)\s*</body>',
    index_content,
    re.DOTALL
)
if not scroll_and_scripts_match:
    print("Error: Could not find scripts in index.html")
    exit(1)

new_scripts = scroll_and_scripts_match.group(1)

# Update each HTML file
for filename in html_files:
    filepath = os.path.join('.', filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header
    content = re.sub(
        r'<!-- Top Header Bar -->.*?</header>',
        new_header,
        content,
        flags=re.DOTALL
    )
    
    # Replace or add mobile menu
    if '<!-- Mobile Menu Modal -->' in content:
        content = re.sub(
            r'<!-- Mobile Menu Modal -->.*?</div>\s*</div>(?=\s*<!--)',
            new_mobile_menu,
            content,
            flags=re.DOTALL
        )
    else:
        # Insert mobile menu after header
        content = re.sub(
            r'(</header>)',
            r'\1\n\n    ' + new_mobile_menu,
            content
        )
    
    # Replace footer
    content = re.sub(
        r'<!-- Footer -->.*?</footer>',
        new_footer,
        content,
        flags=re.DOTALL
    )
    
    # Replace scroll button and scripts
    content = re.sub(
        r'<!-- Scroll to Top Button -->.*?</script>\s*</body>',
        new_scripts + '\n  </body>',
        content,
        flags=re.DOTALL
    )
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {filename}")

print("\n✅ All files updated successfully!")
