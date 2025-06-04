### Định nghĩa:
- Học máy: thuật toán/chương trình có khả năng tự học theo thời gian
- 2 loại bài toán về học máy
	- Có nhãn: dữ liệu với nhãn kèm theo
		- Hồi quy: giá trị đầu ra trên 1 miền trùng với miền đầu vào
		- Phân lớp: giá trị đầu ra chia thành enum
	- Không nhãn:
		- Phân cụm
		- Giảm chiều

### Hồi quy tuyến tính
Xây dựng hàm $f_x$ tuyến tính để khi nhận dữ liệu $x$ thì cho ra $y'$ sát với nhãn $y$ nhất có thể

- **Mục tiêu**: tìm $f_{x}$ sao cho trên mỗi điểm dữ liệu $x$, $f(x) = \hat{y}$ sát $y$ nhất có thể
- ![[Pasted image 20250224152515.png]] là nhỏ nhất
- Hàm độ lệch của hàm hai biến: $$
\begin{align}
R &= \Sigma_{i = 1}^{n} (y_{i} - \hat{y}_{i})^2 \\
&= \Sigma_{i = 1}^{n} (y_i - (\beta_{0}x_{0} + \beta_{1}x_{1}))
\end{align}
$$
- $R$ nhỏ nhất tức độ lệch dự đoán nhỏ nhất, tức đi đạo hàm: $$
x^{2}
$$

### Chiến thuật cập nhật mẫu
Việc training -> tìm $\beta$, data mới có thể được tính theo 3 chiến thuật:
- Cập nhật một mẫu
- Cập nhật $m$ mẫu với $m < n$
- Cập nhật toàn bộ $n$ mẫu

### Chuẩn hóa dữ liệu
Các giá trị $\beta$ bản chất là sức ảnh hưởng của đối tượng đó lên việc đưa ra quyết định
$\beta$ sẽ nằm trong khoảng $[-1,1]$ -> **nếu lớn hơn thì phải chuẩn hóa về khoảng này**
