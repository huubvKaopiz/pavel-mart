#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to update Tailwind config and styles across all HTML pages
Updates brand colors, fonts, and animations to match index.html
"""

import os
import re
from pathlib import Path

# Configuration from index.html
TAILWIND_CONFIG = '''    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              green: {
                50: "#F0F9E8",   // Very light green for backgrounds
                100: "#E1F3D1",  // Light green for badges/decorative
                200: "#C3E7A3",  // Light green for placeholders
                300: "#A5DB75",  // Medium light
                400: "#81CF01",  // Primary brand green (PANTONE)
                500: "#81CF01",  // Primary brand green (PANTONE)
                600: "#6BB301",  // Darker for hover states
                700: "#227041",  // Dark brand green (PANTONE)
                800: "#227041",  // Dark brand green (footer/header)
                900: "#1A5832",  // Even darker for emphasis
              },
              dark: {
                900: "#333333",  // Brand text color
              },
            },
            fontFamily: {
              sans: ["Montserrat", "sans-serif"],
            },
          },
        },
      };
    </script>'''

CUSTOM_STYLES = '''    <style>
      * {
        font-family: "Montserrat", sans-serif;
      }
      
      body {
        font-family: "Montserrat", sans-serif;
      }
      
      h1, h2, h3, h4, h5, h6 {
        font-family: "Montserrat", sans-serif;
        font-weight: 800;
      }

      /* Hero Banner Slider */
      .swiper-hero {
        width: 100%;
        height: 650px;
      }

      @media (max-width: 768px) {
        .swiper-hero {
          height: 450px;
        }
      }

      .swiper-slide {
        overflow: hidden;
      }

      .swiper-slide img {
        width: 100% !important;
        height: 100% !important;
        object-fit: cover !important;
        object-position: center !important;
        display: block;
      }

      .swiper-pagination-bullet {
        background: white;
        opacity: 0.7;
        width: 14px;
        height: 14px;
      }

      .swiper-pagination-bullet-active {
        opacity: 1;
        background: #81CF01;
        transform: scale(1.3);
      }

      .swiper-button-next,
      .swiper-button-prev {
        color: white;
        background: rgba(129, 207, 1, 0.9);
        width: 55px;
        height: 55px;
        border-radius: 50%;
        transition: all 0.3s ease;
      }

      .swiper-button-next:hover,
      .swiper-button-prev:hover {
        background: rgba(129, 207, 1, 1);
        transform: scale(1.1);
      }

      .swiper-button-next:after,
      .swiper-button-prev:after {
        font-size: 22px;
        font-weight: 900;
      }

      .hero-gradient {
        background: linear-gradient(135deg, #227041 0%, #81CF01 100%);
      }
      
      .card-hover {
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
      }
      
      .card-hover:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(129, 207, 1, 0.2);
      }

      .card-hover::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
      }

      .card-hover:hover::before {
        left: 100%;
      }
      
      .section-divider {
        background: linear-gradient(to right, transparent, #81CF01, transparent);
        height: 3px;
      }

      /* Promotional Cards with Animation */
      .promo-card {
        background: linear-gradient(135deg, #81CF01 0%, #227041 100%);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
      }

      .promo-card::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
      }

      @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }

      .promo-card:hover {
        transform: scale(1.05);
        box-shadow: 0 30px 60px rgba(129, 207, 1, 0.3);
      }

      /* Product Card Animation */
      .product-card {
        transition: all 0.3s ease;
        border-radius: 20px;
        overflow: hidden;
        background: white;
      }

      .product-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
      }

      .product-card img {
        transition: transform 0.5s ease;
      }

      .product-card:hover img {
        transform: scale(1.15) rotate(2deg);
      }

      /* Badge Pulse Animation */
      @keyframes pulse {
        0%, 100% {
          transform: scale(1);
          opacity: 1;
        }
        50% {
          transform: scale(1.1);
          opacity: 0.8;
        }
      }

      .badge-pulse {
        animation: pulse 2s infinite;
      }

      /* Smooth Scroll */
      html {
        scroll-behavior: smooth;
      }

      /* Loading Animation */
      @keyframes fadeInUp {
        from {
          opacity: 0;
          transform: translateY(30px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      .animate-fade-in-up {
        animation: fadeInUp 0.8s ease-out;
      }

      /* Floating Animation */
      @keyframes float {
        0%, 100% {
          transform: translateY(0px);
        }
        50% {
          transform: translateY(-15px);
        }
      }

      .animate-float {
        animation: float 3s ease-in-out infinite;
      }

      /* Gradient Text */
      .gradient-text {
        background: linear-gradient(135deg, #81CF01 0%, #227041 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
      }

      /* Slide In Animation */
      @keyframes slideInLeft {
        from {
          opacity: 0;
          transform: translateX(-50px);
        }
        to {
          opacity: 1;
          transform: translateX(0);
        }
      }

      @keyframes slideInRight {
        from {
          opacity: 0;
          transform: translateX(50px);
        }
        to {
          opacity: 1;
          transform: translateX(0);
        }
      }

      .animate-slide-in-left {
        animation: slideInLeft 0.8s ease-out;
      }

      .animate-slide-in-right {
        animation: slideInRight 0.8s ease-out;
      }

      /* Scale Animation */
      @keyframes scaleIn {
        from {
          opacity: 0;
          transform: scale(0.9);
        }
        to {
          opacity: 1;
          transform: scale(1);
        }
      }

      .animate-scale-in {
        animation: scaleIn 0.6s ease-out;
      }

      /* Parallax Effect */
      .parallax-section {
        transition: transform 0.5s ease-out;
      }

      /* Image Brightness */
      .brightness-110 {
        filter: brightness(1.1);
      }

      /* Smooth Section Transitions */
      section {
        position: relative;
        transition: all 0.3s ease;
      }

      /* Wave SVG Animation */
      @keyframes wave {
        0% {
          transform: translateX(0);
        }
        50% {
          transform: translateX(-25px);
        }
        100% {
          transform: translateX(0);
        }
      }

      .wave-animate {
        animation: wave 10s ease-in-out infinite;
      }

      /* Active navigation styles */
      .nav-link {
        position: relative;
        transition: all 0.3s ease;
      }

      .nav-link.active {
        color: #81CF01 !important;
        font-weight: 600;
      }

      .nav-link.active::after {
        content: "";
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 100%;
        height: 3px;
        background: #81CF01;
        border-radius: 2px;
      }

      .nav-link:not(.active):hover {
        color: #81CF01;
      }

      /* Dropdown active styles */
      .dropdown-link.active {
        background-color: #f0f9f0;
        color: #81CF01 !important;
        font-weight: 600;
      }

      /* Mobile navigation active styles */
      .mobile-nav-link.active {
        color: #81CF01 !important;
        font-weight: 600;
        background-color: #f0f9f0;
        border-left: 4px solid #81CF01;
        padding-left: calc(1rem - 4px);
      }

      .mobile-dropdown-link.active {
        color: #81CF01 !important;
        font-weight: 600;
        background-color: #f0f9f0;
      }


    </style>'''

# List of HTML files to update (excluding index.html)
HTML_FILES = [
    'gioi-thieu.html',
    'he-thong-sieu-thi.html',
    'hoat-dong-cong-dong.html',
    'khach-hang-thanh-vien.html',
    'su-kien-tin-tuc.html',
    'thong-tin-lien-he.html',
    'tin-khuyen-mai.html',
    'uu-dai-dat-hang-online.html',
]

def update_html_file(file_path):
    """Update a single HTML file with new config and styles"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace Tailwind config script
        # Pattern to match <script>tailwind.config = {...}</script>
        script_pattern = r'<script>\s*tailwind\.config\s*=\s*\{[\s\S]*?\};\s*</script>'
        
        if re.search(script_pattern, content):
            content = re.sub(script_pattern, TAILWIND_CONFIG, content)
            print(f"  ✓ Updated Tailwind config in {os.path.basename(file_path)}")
        else:
            # If pattern not found, insert after Swiper script
            swiper_script = '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>'
            if swiper_script in content:
                content = content.replace(swiper_script, swiper_script + '\n' + TAILWIND_CONFIG)
                print(f"  ✓ Inserted Tailwind config in {os.path.basename(file_path)}")
        
        # Find and replace custom styles
        # Pattern to match <style>...</style>
        style_pattern = r'<style>[\s\S]*?</style>'
        
        if re.search(style_pattern, content):
            content = re.sub(style_pattern, CUSTOM_STYLES, content, count=1)
            print(f"  ✓ Updated custom styles in {os.path.basename(file_path)}")
        else:
            # If pattern not found, insert after Tailwind config
            content = content.replace(TAILWIND_CONFIG, TAILWIND_CONFIG + '\n' + CUSTOM_STYLES)
            print(f"  ✓ Inserted custom styles in {os.path.basename(file_path)}")
        
        # Write updated content back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    except Exception as e:
        print(f"  ✗ Error updating {os.path.basename(file_path)}: {str(e)}")
        return False

def main():
    """Main function to update all HTML files"""
    print("🎨 Updating Tailwind config and styles across all pages...\n")
    
    current_dir = Path(__file__).parent
    updated_count = 0
    failed_count = 0
    
    for html_file in HTML_FILES:
        file_path = current_dir / html_file
        
        if not file_path.exists():
            print(f"  ⚠ File not found: {html_file}")
            failed_count += 1
            continue
        
        print(f"📄 Processing {html_file}...")
        
        if update_html_file(file_path):
            updated_count += 1
        else:
            failed_count += 1
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"✅ Successfully updated: {updated_count} files")
    if failed_count > 0:
        print(f"❌ Failed to update: {failed_count} files")
    print("=" * 60)
    print("\n🎉 Style update complete!")
    print("\nUpdated:")
    print("  • Tailwind config with brand colors (PANTONE #81CF01, #227041)")
    print("  • Montserrat font family")
    print("  • All custom animations and effects")
    print("  • Active navigation styles")
    print("  • Swiper slider styles")

if __name__ == "__main__":
    main()
