# Ontology/KG-RAG mapping review: GitHub upload candidate

Đây là gói staging đã lựa chọn theo hướng dẫn tiếng Việt, chưa phải bản phát
hành cuối cùng. Gói không chứa PDF nguồn, thư mục Backup, review queue hoặc biểu
mẫu human verification chưa hoàn thành.

## Nội dung hiện có

- 112 public records cho mỗi Pass 1 và Pass 2;
- codebook, freeze manifest, override log và validation report;
- paired labels, agreement metrics, tier confusion và final-label alignment;
- consensus 112 nghiên cứu và crosswalk;
- semantic map, summary, appendix rows và tám hình kết quả;
- script xây dựng, kiểm tra và tính lại agreement.

## Chưa đủ điều kiện phát hành cuối cùng

- thiếu `data/search/search_log_1367.csv`;
- thiếu `data/extraction/structured_extraction_112.csv`;
- chưa lựa chọn `LICENSE`;
- cần chạy kiểm tra từ một clean clone trước khi gắn release tag.

Chạy `python scripts/validate_github_upload_candidate.py`. Chế độ
`--final` chỉ thành công sau khi toàn bộ điều kiện phát hành được đáp ứng.