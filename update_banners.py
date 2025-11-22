#!/usr/bin/env python3
"""
Script to update banner sections for multiple pages to match index.html style
"""

import re

# Banner configurations for each page
BANNER_CONFIGS = {
    'tin-khuyen-mai.html': {
        'title': 'Tin Khuyến Mãi',
        'subtitle': 'Ưu Đãi Hấp Dẫn',
        'description': 'Cập nhật liên tục các chương trình khuyến mãi<br/>Giảm giá sốc - Quà tặng hấp dẫn mỗi ngày',
        'badge': '🎁 KHUYẾN MÃI ĐẶC BIỆT',
        'badge_color': 'from-red-500 to-orange-500',
        'title_color': 'text-yellow-300',
        'image': 'https://images.unsplash.com/photo-1607082349566-187342175e2f?w=1920&h=1080&fit=crop',
        'button_text': 'Xem ngay',
        'button_link': '#promotions'
    },
    'uu-dai-dat-hang-online.html': {
        'title': 'Đặt Hàng Online',
        'subtitle': 'Giao Hàng Tận Nơi',
        'description': 'Đặt hàng online - Giao tận nhà trong 2h<br/>Miễn phí ship cho đơn từ 500K',
        'badge': '🛍️ MUA SẮM ONLINE',
        'badge_color': 'from-blue-500 to-cyan-500',
        'title_color': 'text-cyan-300',
        'image': 'https://images.unsplash.com/photo-1557821552-17105176677c?w=1920&h=1080&fit=crop',
        'button_text': 'Đặt hàng ngay',
        'button_link': '#order-online'
    },
    'su-kien-tin-tuc.html': {
        'title': 'Sự Kiện & Tin Tức',
        'subtitle': 'Cập Nhật Mới Nhất',
        'description': 'Thông tin sự kiện, tin tức mới nhất<br/>Hoạt động cộng đồng, trách nhiệm xã hội',
        'badge': '📰 TIN TỨC MỚI',
        'badge_color': 'from-purple-500 to-pink-500',
        'title_color': 'text-pink-300',
        'image': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=1920&h=1080&fit=crop',
        'button_text': 'Xem tin tức',
        'button_link': '#news'
    },
    'khach-hang-thanh-vien.html': {
        'title': 'Khách Hàng Thành Viên',
        'subtitle': 'Ưu Đãi Đặc Biệt',
        'description': 'Tích điểm mỗi lần mua sắm<br/>Giảm giá độc quyền cho hội viên thân thiết',
        'badge': '💳 THÀNH VIÊN VIP',
        'badge_color': 'from-yellow-500 to-amber-500',
        'title_color': 'text-amber-300',
        'image': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=1920&h=1080&fit=crop',
        'button_text': 'Đăng ký ngay',
        'button_link': '#register'
    }
}

def create_banner_html(config):
    """Create banner HTML based on configuration"""
    return f"""    <!-- Hero Banner -->
    <section class="relative overflow-hidden" style="height: 500px;">
      <div class="absolute inset-0">
        <img src="{config['image']}" alt="{config['title']}" class="w-full h-full object-cover" style="filter: brightness(1.2) contrast(1.15) saturate(1.4);" />
        <div class="absolute inset-0 bg-gradient-to-r from-black/70 via-black/40 to-black/20"></div>
      </div>
      
      <div class="relative h-full flex items-center">
        <div class="container mx-auto px-4 md:px-8">
          <div class="max-w-2xl text-white animate-fade-in-up">
            <div class="inline-block bg-gradient-to-r {config['badge_color']} text-white px-4 md:px-5 py-2 md:py-2.5 rounded-full text-xs md:text-sm font-black mb-3 md:mb-4 badge-pulse shadow-2xl border-2 border-white/50">
              {config['badge']}
            </div>
            <h1 class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-black mb-3 md:mb-4 leading-tight" style="text-shadow: 4px 4px 12px rgba(0,0,0,0.9), 0 0 30px rgba(0,0,0,0.7), 2px 2px 4px rgba(0,0,0,1);">
              {config['subtitle']}<br/>
              <span class="{config['title_color']}">{config['title']}</span>
            </h1>
            <p class="text-base sm:text-lg md:text-xl lg:text-2xl mb-6 md:mb-8 font-bold leading-relaxed" style="text-shadow: 3px 3px 8px rgba(0,0,0,0.9), 0 0 20px rgba(0,0,0,0.7);">
              {config['description']}
            </p>
            <div class="flex flex-wrap gap-3 md:gap-4">
              <a href="{config['button_link']}" class="bg-gradient-to-r {config['badge_color']} hover:opacity-90 text-white px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base inline-flex items-center transition transform hover:scale-105 shadow-2xl">
                {config['button_text']}
                <svg class="w-4 h-4 md:w-5 md:h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                </svg>
              </a>
              <a href="index.html" class="bg-white/30 backdrop-blur-md hover:bg-white/40 text-white px-6 md:px-8 py-3 md:py-4 rounded-full font-black text-sm md:text-base transition transform hover:scale-105 shadow-xl border-2 border-white/50">
                Trang chủ
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>"""

def update_banner(filename):
    """Update banner section in HTML file"""
    if filename not in BANNER_CONFIGS:
        print(f"No configuration for {filename}")
        return
    
    config = BANNER_CONFIGS[filename]
    new_banner = create_banner_html(config)
    
    # Read file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace banner section
    # Pattern to match from <!-- Hero Banner --> to end of section
    pattern = r'<!-- Hero Banner.*?</section>'
    
    # Try to find the banner section
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        updated_content = content[:match.start()] + new_banner + content[match.end():]
        
        # Write updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Updated banner in {filename}")
    else:
        print(f"❌ Could not find banner section in {filename}")

def main():
    """Update banners for all configured pages"""
    print("🚀 Updating banners for multiple pages...\n")
    
    for filename in BANNER_CONFIGS.keys():
        update_banner(filename)
    
    print("\n✨ Banner update completed!")

if __name__ == '__main__':
    main()
