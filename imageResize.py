import os
from PIL import Image, ImageOps

# 이미지 파일들이 저장된 디렉토리 경로
image_directory = '/Users/johangmin/Desktop/allData'
# 이미지 크기를 저장할 리스트
widths = []
heights = []

# 디렉토리 내의 모든 파일에 대해 반복하여 평균 크기 계산
for filename in os.listdir(image_directory):
    if filename.lower().endswith('.jpg'):
        with Image.open(os.path.join(image_directory, filename)) as img:
            widths.append(img.width)
            heights.append(img.height)

# 평균 크기 계산
average_width = int(sum(widths) / len(widths))
average_height = int(sum(heights) / len(heights))

print(f"Average width: {average_width}")
print(f"Average height: {average_height}")

# for filename in os.listdir(image_directory):
#     if filename.lower().endswith('.jpg'):
#         with Image.open(os.path.join(image_directory, filename)) as img:
#             # 이미지가 팔레트 모드(P)인지 확인하고, RGB 모드로 변환
#             if img.mode == 'P':
#                 img = img.convert('RGB')
#
#             # 이미지의 종횡비 유지하며 리사이즈
#             img.thumbnail((average_width, average_height), Image.Resampling.LANCZOS)
#
#             # 패딩 추가
#             delta_w = average_width - img.width
#             delta_h = average_height - img.height
#             padding = (delta_w // 2, delta_h // 2, delta_w - (delta_w // 2), delta_h - (delta_h // 2))
#             padded_img = ImageOps.expand(img, padding, (0, 0, 0))  # 검정색 패딩, 원하는 색으로 변경 가능
#
#             # RGBA 모드를 RGB 모드로 변환
#             if padded_img.mode != 'RGB':
#                 padded_img = padded_img.convert('RGB')
#
#             padded_img.save(os.path.join(image_directory, filename))  # 원본 파일을 덮어씁니다. 필요 시 백업을 권장