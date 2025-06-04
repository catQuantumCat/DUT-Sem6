Dữ liệu được crawl từ các websites sau:
- photo-ac.com
- unsplash.com
- freepik.com
- pixabay.com
Đối với photo-ac, sử dụng BeautifulSoup và PIL để thực hiện quá trình crawl, bao gồm:
- Xác định các query parameters để nhập tên của hình ảnh cần tìm
- Gửi GET request với user-agent là Mozilla/5.0 nhằm giả lặp trình duyệt
- Với mỗi thẻ \<img> tìm thấy được sau khi BeautifulSoup parse được HTML trả về:
	- Kiểm tra URL hợp lệ (phải bắt đầu bằng http/https)
	- Kiểm tra định dạng file (.jpg, .jpeg, .png, .gif)
	- Bỏ qua các ảnh chứa từ khóa trong URL không mong muốn (logo, ads, banner) nhằm loại bỏ các ảnh không phải là ảnh người
- Lưu ảnh nếu thỏa mãn tất cả điều kiện
```
https://en.photo-ac.com/search/happy%20person?page=1
```
Đối với Pixabay có cung cấp API key để thực hiện việc lấy ảnh: sử dụng thư viện Python và cung cấp API để tiến hành crawl.
- Pixabay: https://github.com/zzhanghub/crawler_pixabay
Đối với Unsplash và Freepik, các web không cung cấp API endpoint và có cơ chế bảo vệ crawl (403 khi dùng Selenium) -> sử dụng extension Image Downloader
![[Pasted image 20250527173016.png]]

Loại bỏ các ảnh có kích thước dưới (400x400)
## Nhận xét biểu đồ
Đối với từng cảm xúc, thực hiện crawl từ các nguồn như sau:
![[Pasted image 20250523233336.png]]
![[Pasted image 20250527172514.png]]
Sử dụng hash để loại bỏ các ảnh trùng lặp
	- Đọc toàn bộ nội dung file ảnh dưới dạng binary ("rb")
	- Sử dụng thuật toán MD5 để tạo hash
	- Chuyển đổi hash thành chuỗi hex
	- Lọc qua các hình, nếu hash giống nhau thì loại bỏ hình bị lặp đó
- Sử dụng face_recognition để phát hiện các bounding box trong các ảnh, bóc tách các mặt thành size 48x48

![[emotion_samples.png]]
- Sau đó tiến hành cắt các ảnh về dạng 40x40 và chuyển hệ màu về trắng đen
	- Giảm thiểu 2/3 kích cỡ data
	- Giúp model tập trung phân tích về biểu cảm và đường nét khuôn mặt, hơn là màu da hay điều kiện ánh sáng, dẫn đến giúp giảm bias
**![[bar_chart.png]]**
- Trang Unsplash cung cấp ảnh với độ phân giải cao nhất, nên không cần lọc nhiều ảnh với chất lượng thấp.
- Trang photo-ac cho phép crawl dễ dàng nhất, nhưng chất lượng ảnh không cao nên cần crawl nhiều để lấy số ảnh cần thiết
- Ở hầu hết các trang, cảm xúc giận dữ tìm được nhiều ảnh nhất, và cũng là cảm xúc với số lượng ảnh có chất lượng cao nhiều nhất.
![[emotion_summary.png]]
![/Users/quantumcat/Desktop/flights/bounding_box_distribution.png](file:///Users/quantumcat/Desktop/flights/bounding_box_distribution.png)
- Sau khi bóc tách khuôn mặt
	- Phần lớn số lượng hỉnh crawl được không phát hiện được khuôn mặt, do là ảnh asset, hoặc khuôn mặt không lộ rõ trong khuôn hình
	- Buồn bã có nhiều hình chỉ có 1 khuôn mặt
	- Hạnh phúc và giận dữ là 2 cảm xúc với nhiều hình mà trong đó có 2 người
![[Pasted image 20250525165709.png]]
![[Pasted image 20250525171409.png]]



