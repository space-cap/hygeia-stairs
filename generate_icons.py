import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_hygeia_icon(size=1024):
    # 1024x1024 고해상도 캔버스 생성
    img = Image.new("RGBA", (size, size), (15, 23, 42, 255)) # #0f172a
    draw = ImageDraw.Draw(img)

    # 1. 배경 그라데이션 (방사형 틸 글로우)
    cx, cy = size // 2, size // 2
    for r in range(size // 2, 0, -8):
        alpha = int(60 * (1 - r / (size // 2)))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(13, 148, 136, alpha))

    # 2. 방패 (Shield) 패스 그리기
    # 방패 좌표 계산
    shield_top = int(size * 0.18)
    shield_bottom = int(size * 0.76)
    shield_left = int(size * 0.22)
    shield_right = int(size * 0.78)
    shield_w = shield_right - shield_left
    shield_h = shield_bottom - shield_top

    # 방패 외곽 그림자
    shadow_offset = 12
    shadow_pts = [
        (shield_left + shadow_offset, shield_top + shadow_offset),
        (shield_right + shadow_offset, shield_top + shadow_offset),
        (shield_right + shadow_offset, int(shield_top + shield_h * 0.55) + shadow_offset),
        (cx + shadow_offset, shield_bottom + shadow_offset),
        (shield_left + shadow_offset, int(shield_top + shield_h * 0.55) + shadow_offset)
    ]
    draw.polygon(shadow_pts, fill=(0, 0, 0, 120))

    # 방패 본체 (틸 그린 그라데이션 느낌)
    shield_pts = [
        (shield_left, shield_top),
        (shield_right, shield_top),
        (shield_right, int(shield_top + shield_h * 0.55)),
        (cx, shield_bottom),
        (shield_left, int(shield_top + shield_h * 0.55))
    ]
    draw.polygon(shield_pts, fill=(13, 148, 136, 255)) # #0d9488

    # 방패 테두리 (밝은 민트 #2dd4bf)
    draw.polygon(shield_pts, outline=(45, 212, 191, 255), width=int(size * 0.022))

    # 방패 안쪽 하이라이트 라인
    inner_inset = int(size * 0.035)
    inner_pts = [
        (shield_left + inner_inset, shield_top + inner_inset),
        (shield_right - inner_inset, shield_top + inner_inset),
        (shield_right - inner_inset, int(shield_top + shield_h * 0.55) - inner_inset // 2),
        (cx, shield_bottom - inner_inset * 1.4),
        (shield_left + inner_inset, int(shield_top + shield_h * 0.55) - inner_inset // 2)
    ]
    draw.polygon(inner_pts, outline=(94, 234, 212, 160), width=int(size * 0.008))

    # 3. 방패 중앙의 대문자 'H' 심볼 (두껍고 정갈한 산세리프)
    h_top = int(size * 0.28)
    h_bottom = int(size * 0.58)
    h_left = int(size * 0.35)
    h_right = int(size * 0.65)
    bar_w = int(size * 0.065)
    cross_h = int(size * 0.055)
    cross_y = (h_top + h_bottom) // 2

    # H 좌측 기둥
    draw.rounded_rectangle([h_left, h_top, h_left + bar_w, h_bottom], radius=6, fill=(255, 255, 255, 255))
    # H 우측 기둥
    draw.rounded_rectangle([h_right - bar_w, h_top, h_right, h_bottom], radius=6, fill=(255, 255, 255, 255))
    # H 가로 연결 바
    draw.rounded_rectangle([h_left, cross_y - cross_h // 2, h_right, cross_y + cross_h // 2], radius=4, fill=(255, 255, 255, 255))

    # 4. 우측 상단 골든 스파클 (✨ 반짝임 4각 별)
    sparkle_cx = int(size * 0.76)
    sparkle_cy = int(size * 0.22)
    sp_r_long = int(size * 0.075)
    sp_r_short = int(size * 0.02)

    # 4각 별 그리기
    star_pts = []
    for i in range(8):
        angle = i * (math.pi / 4)
        r = sp_r_long if i % 2 == 0 else sp_r_short
        star_pts.append((sparkle_cx + r * math.cos(angle), sparkle_cy + r * math.sin(angle)))
    draw.polygon(star_pts, fill=(250, 204, 21, 255)) # #facc15
    # 스파클 중심 광채
    draw.ellipse([sparkle_cx - 8, sparkle_cy - 8, sparkle_cx + 8, sparkle_cy + 8], fill=(255, 255, 255, 255))

    # 5. 하단 텍스트 "HYGEIA" (폰트 없을 시 기하학적 도형으로 렌더링)
    # 글자 "HYGEIA"를 직접 벡터로 그리기 (시스템 폰트 의존도 제로)
    text_y = int(size * 0.83)
    text_h = int(size * 0.045)
    letter_w = int(size * 0.038)
    gap = int(size * 0.022)
    start_x = int(size * 0.31)
    
    # 폰트 로드 시도
    font_loaded = False
    for font_name in ["arialbd.ttf", "malgunbd.ttf", "seguiemb.ttf", "Arial Bold.ttf"]:
        try:
            f = ImageFont.truetype(font_name, int(size * 0.055))
            # 텍스트 중앙 정렬
            bbox = draw.textbbox((0, 0), "HYGEIA", font=f)
            tw = bbox[2] - bbox[0]
            tx = (size - tw) // 2
            draw.text((tx, text_y), "HYGEIA", fill=(255, 255, 255, 240), font=f)
            
            # 서브 텍스트
            f_sub = ImageFont.truetype(font_name, int(size * 0.026))
            bbox_sub = draw.textbbox((0, 0), "PREMIUM STAIRS CARE", font=f_sub)
            tw_sub = bbox_sub[2] - bbox_sub[0]
            tx_sub = (size - tw_sub) // 2
            draw.text((tx_sub, text_y + int(size * 0.065)), "PREMIUM STAIRS CARE", fill=(94, 234, 212, 220), font=f_sub)
            font_loaded = True
            break
        except Exception:
            continue

    if not font_loaded:
        # 폰트 로드 실패 시 기본 폰트로
        draw.text((size // 2 - 60, text_y), "HYGEIA", fill=(255, 255, 255, 240))

    return img

# 메인 실행
if __name__ == "__main__":
    base_img = create_hygeia_icon(1024)

    # 1. apple-touch-icon.png (180x180) - iOS 홈화면 표준
    icon_180 = base_img.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save("apple-touch-icon.png", "PNG")
    icon_180.save("assets/apple-touch-icon.png", "PNG")

    # 2. icon-192.png (192x192) - 안드로이드 홈화면 표준
    icon_192 = base_img.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192.save("assets/icon-192.png", "PNG")

    # 3. icon-512.png (512x512) - 고해상도 PWA 스플래시 표준
    icon_512 = base_img.resize((512, 512), Image.Resampling.LANCZOS)
    icon_512.save("assets/icon-512.png", "PNG")

    # 4. favicon-32.png & favicon.ico
    icon_32 = base_img.resize((32, 32), Image.Resampling.LANCZOS)
    icon_32.save("assets/favicon-32.png", "PNG")
    icon_32.save("favicon.ico", "ICO")

    print("✅ All icons generated successfully!")
