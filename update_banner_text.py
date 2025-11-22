#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to enhance banner text visibility and mobile responsiveness
"""

import re

def update_index_html():
    file_path = 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Slide 1 - Khai trương
    content = re.sub(
        r'(<div class="swiper-slide relative">[\s\S]*?photo-1578916171728-46686eac8d58[\s\S]*?)\s*<div class="absolute inset-0 bg-gradient-to-r from-black/40 via-black/20 to-transparent',
        r'\1\n          <div class="absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20',
        content,
        count=1
    )
    
    # Update badge Slide 1
    content = re.sub(
        r'(<div class="inline-block bg-gradient-to-r from-red-500 to-orange-500 text-white )px-5 py-2\.5 rounded-full text-sm font-bold mb-4(.*?KHAI TRƯƠNG)',
        r'\1px-4 md:px-5 py-2 md:py-2.5 rounded-full text-xs md:text-sm font-black mb-3 md:mb-4\2',
        content,
        count=1
    )
    
    # Update h1 Slide 1
    content = re.sub(
        r'(<h1 class=")text-3xl md:text-5xl(.*?>[\s\S]*?Tưng Bừng Khai Trương)',
        r'\1text-2xl sm:text-3xl md:text-5xl lg:text-6xl\2',
        content,
        count=1
    )
    
    # Update text-shadow Slide 1
    content = re.sub(
        r'(style="text-shadow:) 3px 3px 8px rgba\(0,0,0,0\.8\), 0 0 20px rgba\(0,0,0,0\.5\);"(>[\s\S]*?Pavel Mart)',
        r'\1 4px 4px 12px rgba(0,0,0,0.9), 0 0 30px rgba(0,0,0,0.7), 2px 2px 4px rgba(0,0,0,1);"\2',
        content,
        count=1
    )
    
    # Update p text Slide 1
    content = re.sub(
        r'(<p class=")text-xl md:text-2xl mb-8 text-gray-200("[\s\S]*?Giảm đến 50%)',
        r'\1text-base sm:text-lg md:text-xl lg:text-2xl mb-6 md:mb-8 font-bold leading-relaxed" style="text-shadow: 3px 3px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7);"\2',
        content,
        count=1
    )
    
    # Add yellow highlight to 50%
    content = re.sub(
        r'Giảm đến 50% toàn bộ',
        r'Giảm đến <span class="text-yellow-300 text-xl sm:text-2xl md:text-3xl">50%</span> toàn bộ',
        content,
        count=1
    )
    
    # Update buttons Slide 1
    content = re.sub(
        r'(<div class="flex flex-wrap )gap-4',
        r'\1gap-3 md:gap-4',
        content,
        count=1
    )
    
    content = re.sub(
        r'(bg-gradient-to-r from-red-500[\s\S]{20,60})px-8 py-4 rounded-full font-bold inline',
        r'\1px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base inline',
        content,
        count=1
    )
    
    content = re.sub(
        r'(<svg class=")w-5 h-5( ml-2"[\s\S]{1,100}Nhận ưu đãi)',
        r'\1w-4 h-4 md:w-5 md:h-5\2',
        content,
        count=1
    )
    
    content = re.sub(
        r'(bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white )px-8 py-4 rounded-full font-bold transition',
        r'bg-white/30 backdrop-blur-md hover:bg-white/40 text-white px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base transition',
        content,
        count=1
    )
    
    # Add border to second button
    content = re.sub(
        r'(backdrop-blur-md hover:bg-white/40 text-white px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base transition transform hover:scale-105)(">[\s\S]{1,30}Tìm siêu thị)',
        r'\1 shadow-xl border-2 border-white/50\2',
        content,
        count=1
    )
    
    print("✅ Updated Slide 1 - Khai trương")
    
    # Similar updates for Slides 2, 3, 4 with appropriate selectors
    # Slide 2 - Ưu đãi thành viên
    content = re.sub(
        r'(photo-1604719312566-8912e9227c6a[\s\S]*?)\s*<div class="absolute inset-0 bg-gradient-to-r from-black/40 via-black/20 to-transparent([\s\S]*?Ưu Đãi)',
        r'\1\n          <div class="absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20\2',
        content,
        count=1
    )
    
    # Update h1 and text for all remaining slides with similar patterns
    content = re.sub(
        r'text-4xl md:text-6xl font-black mb-4 leading-tight',
        r'text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-black mb-3 md:mb-4 leading-tight',
        content
    )
    
    # Update all badge styles
    content = re.sub(
        r'(bg-blue-500 text-white |bg-red-500 text-white |bg-green-500 text-white )px-5 py-2\.5 rounded-full text-sm font-bold mb-4',
        r'\1px-4 md:px-5 py-2 md:py-2.5 rounded-full text-xs md:text-sm font-black mb-3 md:mb-4',
        content
    )
    
    # Update all paragraph text styles
    content = re.sub(
        r'<p class="text-xl md:text-2xl mb-8 text-gray-200">',
        r'<p class="text-base sm:text-lg md:text-xl lg:text-2xl mb-6 md:mb-8 font-bold leading-relaxed" style="text-shadow: 3px 3px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7);">',
        content
    )
    
    # Update all button sizes
    content = re.sub(
        r'px-8 py-4 rounded-full font-bold inline',
        r'px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base inline',
        content
    )
    
    # Update all svg sizes in buttons
    content = re.sub(
        r'<svg class="w-5 h-5 ml-2"',
        r'<svg class="w-4 h-4 md:w-5 md:h-5 ml-2"',
        content
    )
    
    # Update shadow for all h1
    content = re.sub(
        r'style="text-shadow: 3px 3px 8px rgba\(0,0,0,0\.8\), 0 0 20px rgba\(0,0,0,0\.5\);"',
        r'style="text-shadow: 4px 4px 12px rgba(0,0,0,0.9), 0 0 30px rgba(0,0,0,0.7), 2px 2px 4px rgba(0,0,0,1);"',
        content
    )
    
    # Improve color contrast for spans
    content = re.sub(
        r'<span class="text-blue-400">',
        r'<span class="text-blue-300">',
        content
    )
    
    content = re.sub(
        r'<span class="text-red-400">',
        r'<span class="text-red-300">',
        content
    )
    
    content = re.sub(
        r'<span class="text-green-400">',
        r'<span class="text-green-300">',
        content
    )
    
    print("✅ Updated all slides for better visibility and responsiveness")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🎉 Banner text enhancement complete!")
    print("✓ Darker background overlay (from-black/70)")
    print("✓ Stronger text shadows for better visibility")
    print("✓ Responsive font sizes (sm:, md:, lg: breakpoints)")
    print("✓ Mobile-optimized button and badge sizes")
    print("✓ Enhanced color contrast")

if __name__ == "__main__":
    update_index_html()
