# 🧾 Word to PDF Converter

Một công cụ chuyển đổi hàng loạt các file `.doc` và `.docx` sang định dạng PDF. Tự động chuẩn hóa tên file, sao chép vào thư mục tạm và xuất ra thư mục kết quả.

## 📦 Yêu cầu hệ thống

- Python 3.8+
- Windows (vì `docx2pdf` phụ thuộc vào Microsoft Word trên Windows)

## 📁 Cài đặt

### 1. Clone hoặc tải mã nguồn

```bash
git clone [https://github.com/yourusername/word2pdf-batch.git](https://github.com/thanhphamtmu/word2pdf-batch)
cd word2pdf-batch
```

### 2. Tạo virtual environment

```bash
python -m venv venv
```

### 3. Kích hoạt môi trường ảo

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS / Linux** _(⚠ Không hỗ trợ do phụ thuộc MS Word)_:

  ```bash
  source venv/bin/activate
  ```

### 4. Cài đặt các phụ thuộc

```bash
pip install -r requirements.txt
```

📄 _Tạo `requirements.txt` nếu chưa có:_

```bash
pip install docx2pdf
pip freeze > requirements.txt
```

## 🚀 Cách sử dụng

```bash
python word2pdf-batch.py
```

Sau đó nhập đường dẫn thư mục chứa các file `.doc` hoặc `.docx` cần chuyển đổi.

### Ví dụ

```bash
📁 Nhập đường dẫn thư mục chứa file Word: D:\Tài liệu\Báo cáo
```

- Các file sẽ được chuẩn hóa tên và sao chép vào thư mục `converted_tmp`.
- Kết quả PDF được lưu tại: `converted_pdf`.

## 🔐 Ghi chú

- Bỏ qua các file tạm bắt đầu bằng `~$`.
- Tên file sẽ được chuyển sang định dạng ASCII an toàn cho hệ thống.
- Thư mục gốc không bị thay đổi.

## 🧹 Dọn dẹp

Bạn có thể xóa thủ công thư mục `converted_tmp` sau khi chuyển đổi hoàn tất để giải phóng dung lượng.
