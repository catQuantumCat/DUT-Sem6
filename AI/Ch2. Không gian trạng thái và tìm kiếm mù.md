## Không gian trạng thái
Tập hợp các khả năng (trạng thái) xảy ra để giải quyết của vấn đề (đạt được trạng thái đích từ trạng thái đầu)

## Tìm kiếm trên không gian trạng thái
Nguyên tắc tìm trên cây trạng thái
- Trên xuống
- Trái sang phải/phải sang trái
### Tìm kiếm chiều rộng - tìm kiếm mù
FIFO - queue
Chia thành 3 nhóm:
- Chưa xét
- Đang xét
- Đã xét
![[Pasted image 20250113153435.png]]
#### Đánh giá thuật toán:
- Thời gian: o(b \*d) (b = số con nhiều nhất, d = chiều sâu)

## Đặc điểm
- **Thuật toán luôn tìm được nghiệm** (nếu có nghiệm để tìm)
- Chiếm bộ nhớ lớn hơn chiều sâu với cùng d, b và số node

### Tìm kiếm chiều sâu
FILO - stack
Vào trước tính sau
Chia thành 3 nhóm:
- Chưa xét
- Đang xét
- Đã xét

![[Pasted image 20250210150928.png]]

(bỏ ý 2 - độ phức tạp thời gian)
- m: Độ sâu mà tìm được nghiệm đầu tiên

### Đặc điểm:
- Chiếm bộ nhớ nhỏ hơn nhiều so với chiều rộng với cùng d, b và số node
- **Chỉ tìm được nghiệm khi không gian tìm kiếm hữu hạn**


### Chiều sâu có giới hạn
- Đặt giới hạn L - độ sâu để tìm theo chiều sâu
- L  = 0 -> duyệt 1 phần từ![[8318dd8d55b0366ceb103a7e6252613a59689e23f86f930e57b5c35c9a0a11b4.png]]![[1a10785ac4db02dc3a0cc1676b6ea97559343291fde1aaf80cc450cec3c1b11b.png]]