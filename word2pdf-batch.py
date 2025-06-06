import os
import re
import shutil
import unicodedata
import string
from collections import defaultdict
from docx2pdf import convert
from PIL import Image

SAFE_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')

def sanitize_filename(filename):
    normalized = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
    return ''.join(c for c in normalized if c in SAFE_CHARS)

def prepare_files(source_folder, temp_folder):
    os.makedirs(temp_folder, exist_ok=True)
    processed_files = []

    for fname in os.listdir(source_folder):
        if fname.startswith('~$'):
            continue

        is_doc = fname.lower().endswith(('.docx', '.doc'))
        is_image = fname.lower().endswith(IMAGE_EXTENSIONS)

        if not (is_doc or is_image):
            continue

        safe_name = sanitize_filename(fname)
        if not safe_name.lower().endswith(('.docx', '.doc') + IMAGE_EXTENSIONS):
            continue

        src_path = os.path.join(source_folder, fname)
        dst_path = os.path.join(temp_folder, safe_name)
        shutil.copy2(src_path, dst_path)
        processed_files.append((safe_name, dst_path))

    return processed_files

def extract_prefix(name):
    name_lower = name.lower()

    m = re.match(r"(.+?)-\d+", name)
    if m:
        return m.group(1)

    m = re.match(r"(.+?)copy", name, re.IGNORECASE)
    if m:
        return m.group(1)

    if '(' in name:
        return name.split('(')[0]
    if '_' in name:
        return name.split('_')[0]
    if '-' in name:
        return name.split('-')[0]

    return os.path.splitext(name)[0]


def group_images_by_prefix(image_files):
    groups = defaultdict(list)
    for fname in sorted(image_files):
        prefix = extract_prefix(os.path.splitext(fname)[0])
        groups[prefix.strip()].append(fname)
    return groups

def convert_batch(temp_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_files = []

    for fname in sorted(os.listdir(temp_folder)):
        fpath = os.path.join(temp_folder, fname)
        if fname.lower().endswith(('.docx', '.doc')):
            try:
                convert(fpath, output_folder)
                print(f"✅ Đã chuyển Word: {fname}")
            except Exception as e:
                print(f"❌ Lỗi khi chuyển Word {fname}: {e}")
        elif fname.lower().endswith(IMAGE_EXTENSIONS):
            image_files.append(fname)

    grouped = group_images_by_prefix(image_files)
    for prefix, fnames in grouped.items():
        try:
            images = [Image.open(os.path.join(temp_folder, f)).convert('RGB') for f in fnames]
            if not images:
                continue
            first, *rest = images
            output_path = os.path.join(output_folder, f"{prefix}.pdf")
            first.save(output_path, save_all=True, append_images=rest)
            print(f"✅ Đã gộp {len(images)} ảnh vào {prefix}.pdf")
        except Exception as e:
            print(f"❌ Lỗi khi gộp nhóm {prefix}: {e}")

if __name__ == "__main__":
    input_folder = input("📁 Nhập đường dẫn thư mục chứa file Word và ảnh: ").strip()
    temp_folder = os.path.join(input_folder, "converted_tmp")
    output_folder = os.path.join(input_folder, "converted_pdf")

    print("🔍 Đang kiểm tra và sao chép các file có tên hợp lệ...")
    valid_files = prepare_files(input_folder, temp_folder)
    print(f"✅ {len(valid_files)} file sẽ được xử lý.\n")

    print("🔄 Bắt đầu chuyển đổi sang PDF...")
    convert_batch(temp_folder, output_folder)

    print(f"\n📂 PDF đã lưu tại: {output_folder}")
