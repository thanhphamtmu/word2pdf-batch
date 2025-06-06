import os
import shutil
import unicodedata
import string
from docx2pdf import convert

SAFE_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)

def sanitize_filename(filename):
    normalized = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
    return ''.join(c for c in normalized if c in SAFE_CHARS)

def prepare_files(source_folder, temp_folder):
    os.makedirs(temp_folder, exist_ok=True)
    processed_files = []

    for fname in os.listdir(source_folder):
        if not fname.lower().endswith(('.docx', '.doc')) or fname.startswith('~$'):
            continue

        safe_name = sanitize_filename(fname)
        if not safe_name.endswith(('.docx', '.doc')):
            continue  # loại bỏ nếu mất phần mở rộng

        src_path = os.path.join(source_folder, fname)
        dst_path = os.path.join(temp_folder, safe_name)
        shutil.copy2(src_path, dst_path)
        processed_files.append((safe_name, dst_path))

    return processed_files

def convert_batch(temp_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for fname in os.listdir(temp_folder):
        fpath = os.path.join(temp_folder, fname)
        try:
            convert(fpath, output_folder)
            print(f"✅ Đã chuyển: {fname}")
        except Exception as e:
            print(f"❌ Lỗi khi chuyển {fname}: {e}")

if __name__ == "__main__":
    input_folder = input("📁 Nhập đường dẫn thư mục chứa file Word: ").strip()
    temp_folder = os.path.join(input_folder, "converted_tmp")
    output_folder = os.path.join(input_folder, "converted_pdf")

    print("🔍 Đang kiểm tra và sao chép các file có tên hợp lệ...")
    valid_files = prepare_files(input_folder, temp_folder)
    print(f"✅ {len(valid_files)} file sẽ được xử lý.\n")

    print("🔄 Bắt đầu chuyển đổi sang PDF...")
    convert_batch(temp_folder, output_folder)

    print(f"\n📂 PDF đã lưu tại: {output_folder}")
