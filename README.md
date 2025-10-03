# Keylogger (**dùng cho mục đích học tập**)

## Giới thiệu
Đây là project em làm để **tìm hiểu rõ hơn về cơ chế hoạt động của mã độc keylogger**.  
Mục đích/ứng dụng:
- Hiểu cách hoạt động cơ bản của keylogger (thu thập phím).
- Thực hành lập trình Python và xử lý file/log trong môi trường kiểm soát.

## Chức năng chính
- Ghi lại các phím nhấn và lưu vào file log (`log.txt`).
- Lưu log **cục bộ** — phiên bản này **không gửi dữ liệu ra mạng**.

## Yêu cầu (Prerequisites)
- Python 3.8+ (khuyến nghị 3.8 — 3.11).  
- Virtual environment (`venv`) để cô lập phụ thuộc.  
- Thư viện: `pynput` (dùng để bắt sự kiện bàn phím).
