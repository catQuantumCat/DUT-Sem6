### Định nghĩa
Sử dụng **dữ liệu mẫu để đưa ra suy luận về một tổng thể** - hay liệu có đủ bằng chứng trong mẫu của mình để bác bỏ một tuyên bố (giả thuyết gốc) về toàn bộ tổng thể hay không.

#### Các thành phần
1. **Giả thuyết:**
    - **Giả thuyết Gốc (H₀ - Null Hypothesis):** Giả định ban đầu của bài toàn, rằng không có khác biệt nào giữa các quan hệ.
	- **Ví dụ:**
		- "Chiều cao trung bình của nam và nữ là như nhau."
		- "Không có mối quan hệ giữa tập thể dục và giảm cân."
		- "Thuốc mới không có tác dụng đối với huyết áp."
    - **Giả thuyết Đối (H₁ ):** Mâu thuẫn với H0, rằng có khác biệt trong các quan hệ, gồm 2 loại:
        - **Hai phía (≠):** Không rõ hướng.
            - Ví dụ: "Chiều cao trung bình của nam và nữ là _khác nhau_."
        - **Một phía (trái phải):** Có rõ hướng.
            - Ví dụ trái: "Chiều cao trung bình của nữ _thấp hơn_ chiều cao trung bình của nam."
            - Ví dụ phải: "Chiều cao trung bình của nam _cao hơn_ chiều cao trung bình của nữ."
2. **Mức Ý nghĩa - ngưỡng sai(α):**
	- Thường là 5% hoặc 1%
    - Nó thể hiện **xác suất mắc phải Lỗi Loại I** - xác suất kết luận sai H0
    - Có thể hiểu là ngưỡng sai sót nếu kết luận sai H0
	    - Nếu α = 0.05, chấp nhận 5% khả năng bác bỏ sai giả thuyết gốc khi nó thực sự đúng.
3. **Các phương pháp thống kê Kiểm định:**
    - Các phương pháp thống kê kiểm định phụ thuộc vào loại dữ liệu và kiểm định giả thuyết bạn đang thực hiện (ví dụ: thống kê z, thống kê t, thống kê F, thống kê khi bình phương).
    - Các phương pháp này sẽ cho ra tóm tắt mức độ dữ liệu mẫu ban đầu khác biệt so với những gì mong đợi H0 đúng.
4. **Giá trị P (P-value):**
	- Giả sử H_0 đúng - P là xác suất trong thực tế có thể thu thập được dữ liệu có mức độ cực đoan bằng hoặc hơn so với mức độ cực đoan của bộ dữ liệu đã thu thập được để phân tích.
    - Được tính toán dựa trên kết quả từ một trong các phương pháp thống kê và phân phối của thống kê đó theo giả thuyết gốc.
    - P nhỏ -> khả năng tìm được dữ liệu cực đoan bằng hoặc hơn dữ liệu hiện tại là thấp -> góp phần chống lại H0
    - P nhỏ -> khả năng tìm được dữ liệu cực đoan bằng hoặc hơn dữ liệu hiện tại là cao ->   không góp phần chống lại H0
5. **Quy tắc Quyết định (So sánh giá trị p với α):**
    - **Nếu giá trị p ≤ α:**  **Bác bỏ H₀** hay đủ bằng chứng để ủng hộ H1 với mức sai số $\alpha$
    - **Nếu giá trị p > α**: **Không bác bỏ H₀**

#### Các Loại Lỗi
- **Lỗi Loại I (False positive):** Bác bỏ H0 khi H0 đúng trong thực tế
    - **Xác suất:** Xác suất mắc Lỗi Loại I bằng với mức ý nghĩa (α), thường là giá trị nhỏ. 
- **Lỗi Loại II (False negative):** Không bác bỏ H0 khi H0 sai trong thực tế
    - **Xác suất:** Xác suất mắc Lỗi Loại II được ký hiệu là β (beta). β thường không xác định và khó tính toán trực tiếp hơn.

#### Các Bước trong Kiểm định Giả thuyết
6. **Phát biểu Giả thuyết:**
    - Xác định rõ ràng H₀ và giả thuyết đối H₁. Quyết định xem đó là kiểm định một phía hay hai phía.
7. **Đặt Mức Ý nghĩa (α):**
    - Thường là 1% hoặc 5%
8. **Chọn phương pháp và tính Thống kê Kiểm định:**
    - Chọn thống kê kiểm định phù hợp dựa trên dữ liệu và giả thuyết.
    - Tính thống kê kiểm định từ dữ liệu mẫu của bạn.
9. **Xác định Giá trị P:**
    - Tính giá trị p liên quan đến thống kê kiểm định.
10. **Đưa ra Quyết định:**
    - So sánh giá trị p với mức ý nghĩa (α).
    - Nếu giá trị p ≤ α, bác bỏ H₀.
    - Nếu giá trị p > α, không bác bỏ H₀.
11. **Rút ra Kết luận:**
    - Phát biểu kết luận của bạn trong bối cảnh câu hỏi nghiên cứu ban đầu. Giải thích ý nghĩa thực tế của quyết định của bạn. Tránh nói rằng bạn "chấp nhận" H₀; thay vào đó, hãy nói rằng bạn "không bác bỏ" H₀.

#### Các phương pháp thống kê kiểm định
**1. Thống kê Z (Z-statistic)**
- **Công thức
    
    $$ Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} $$
	- xˉ: Trung bình mẫu (sample mean)
	- μ0​: Giá trị trung bình tổng thể được giả định trong giả thuyết gốc (population mean under H₀)
	- σ: Độ lệch chuẩn của tổng thể (population standard deviation)
	- n: Kích thước mẫu (sample size)
- Thống kê Z đo lường số lượng độ lệch chuẩn mà trung bình mẫu (xˉ) cách xa giá trị trung bình tổng thể giả định (μ0​) theo giả thuyết gốc.

**2. Thống kê T (T-statistic)**    
- **Công thức LaTeX:**
    
    $$ t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} $$
	- xˉ: Trung bình mẫu (sample mean)
	- μ0​: Giá trị trung bình tổng thể được giả định trong giả thuyết gốc (population mean under H₀)
	- s: Độ lệch chuẩn mẫu (sample standard deviation)
	- n: Kích thước mẫu (sample size)
- Tương tự như thống kê Z, thống kê T cũng đo lường số lượng "sai số chuẩn" (standard errors) mà trung bình mẫu (xˉ) cách xa giá trị trung bình tổng thể giả định (μ0​) theo giả thuyết gốc. Tuy nhiên, nó sử dụng độ lệch chuẩn mẫu (s) thay vì độ lệch chuẩn tổng thể (σ).

**3. Thống kê Chi bình phương (χ2)**    
- **Công thức**
    
    $$ \chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} $$
	- χ2: Thống kê Khi bình phương
	- ∑: Ký hiệu tổng
	- k: Số lượng danh mục hoặc nhóm (number of categories)
	- Oi​: Tần số quan sát được (observed frequency) cho danh mục thứ i
	- Ei​: Tần số mong đợi (expected frequency) cho danh mục thứ i theo giả thuyết gốc
- Kiểm định tính phù hợp của Khi bình phương đo lường sự khác biệt giữa tần số quan sát được trong các danh mục và tần số mong đợi nếu một phân phối hoặc tỷ lệ cụ thể (được nêu trong giả thuyết gốc) là đúng cho tổng thể. Thống kê χ2 lớn cho thấy sự khác biệt lớn giữa quan sát và mong đợi.