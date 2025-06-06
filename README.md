# 🧾 Word & Image to PDF Converter

Công cụ chuyển đổi hàng loạt:
- Chuyển file Word (`.doc`, `.docx`) sang PDF
- Gộp nhiều ảnh (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`) thành một PDF
- Tự động chuẩn hóa tên file, sao chép vào thư mục tạm và xuất ra thư mục kết quả

## 📦 Yêu cầu hệ thống

- Python 3.8+
- Windows (vì `docx2pdf` phụ thuộc vào Microsoft Word trên Windows)
- Thư viện PIL (Python Imaging Library) để xử lý ảnh

## 📁 Cài đặt

### 1. Clone hoặc tải mã nguồn

```bash
git clone https://github.com/thanhphamtmu/word2pdf-batch.git
cd word2pdf-batch
```

### 2. Tạo virtual environment

```bash
python -m venv venv
```

### 3. Kích hoạt môi trường ảo

```bash
venv\Scripts\activate
```

### 4. Cài đặt các phụ thuộc

```bash
pip install -r requirements.txt
```

📄 _Tạo `requirements.txt` nếu chưa có:_

```bash
pip install docx2pdf Pillow
pip freeze > requirements.txt
```

## 🚀 Cách sử dụng

```bash
python word2pdf-batch.py
```

Nhập đường dẫn thư mục chứa các file cần chuyển đổi (Word và/hoặc ảnh).

### Quy tắc gộp ảnh

- Các ảnh có cùng tiền tố sẽ được gộp vào một file PDF
- Tiền tố được xác định bởi:
  - Phần trước dấu `-` và số (vd: `scan-1.jpg`, `scan-2.jpg` → `scan.pdf`)
  - Phần trước từ "copy" (không phân biệt hoa thường)
  - Phần trước dấu `(`, `_` hoặc `-`
  - Tên file không có các ký tự trên

### Ví dụ

```bash
📁 Nhập đường dẫn thư mục chứa file: D:\Tài liệu\Báo cáo
```

Kết quả:
- File gốc không bị thay đổi
- File trung gian được lưu tại: `converted_tmp`
- File PDF được lưu tại: `converted_pdf`

## 🔐 Ghi chú

- Bỏ qua các file tạm bắt đầu bằng `~$`
- Tên file được chuyển sang định dạng ASCII an toàn
- Tự động nhóm và gộp các ảnh có cùng tiền tố
- Hỗ trợ các định dạng ảnh: PNG, JPG, JPEG, BMP, TIFF

## 🧹 Dọn dẹp

Có thể xóa thư mục `converted_tmp` sau khi chuyển đổi để giải phóng dung lượng.
