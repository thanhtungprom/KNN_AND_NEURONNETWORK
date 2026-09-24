# KNN on Iris Dataset 🌸

## 📝 Giới thiệu
Dự án này triển khai thuật toán **K-Nearest Neighbors (KNN)** để phân loại các giống hoa Iris. Thay vì chỉ chạy mô hình cơ bản, dự án bao quát toàn bộ vòng đời của dữ liệu: từ việc kết nối và lưu trữ trên cơ sở dữ liệu PostgreSQL, phân tích khám phá dữ liệu (EDA) với Pandas, tối ưu hóa tính toán với Numpy, cho đến việc tự xây dựng thuật toán KNN từ đầu và so sánh với mô hình của thư viện Scikit-Learn.

## ✨ Tính năng nổi bật
* **Database Integration:** Đọc file CSV, đẩy dữ liệu lên PostgreSQL và truy vấn ngược lại bằng thư viện `sqlalchemy`.
* **Custom KNN:** Thuật toán K-Nearest Neighbors được tự xây dựng bằng Python thuần để hiểu rõ bản chất toán học (tính khoảng cách Euclidean và cơ chế voting).
* **Machine Learning Pipeline:** Sử dụng `scikit-learn` để chia tập dữ liệu (train/test), huấn luyện mô hình và đánh giá độ chính xác.
* **Data Visualization:** Trực quan hóa phân bố các giống hoa (Setosa, Versicolor, Virginica) trong không gian 2D thông qua `matplotlib`.
* **Performance Benchmarking:** Đo lường và so sánh tốc độ xử lý khoảng cách vector trên tập dữ liệu lớn bằng `numpy`.

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.x
* **Thư viện xử lý & trực quan hóa:** `pandas`, `numpy`, `matplotlib`
* **Thư viện Machine Learning:** `scikit-learn`
* **Cơ sở dữ liệu:** PostgreSQL, `sqlalchemy`, `psycopg2` (khuyến nghị)

## 📂 Cấu trúc dự án
* `Iris.csv`: Tập dữ liệu gốc chứa thông tin kích thước đài hoa và cánh hoa.
* `connect_db.py`: Script khởi tạo kết nối, đưa dữ liệu từ file CSV lên PostgreSQL và đọc dữ liệu về DataFrame.
* `learn_pandas.py` & `learn_numpy.py`: Các kịch bản phân tích dữ liệu, lọc thông tin và đo lường hiệu năng tính toán ma trận.
* `draw_iris.py`: Vẽ biểu đồ phân tán (scatter plot) để phân tích trực quan các đặc trưng của hoa.
* `knn.py`: Triển khai thuật toán KNN thủ công, đọc dữ liệu trực tiếp từ file CSV.
* `end_to_end_knn.py`: Pipeline hoàn chỉnh lấy dữ liệu từ SQL Server, định dạng lại và đưa ra dự đoán bằng hàm KNN tự viết.
* `sklearn_knn.py`: Quy trình huấn luyện KNN tiêu chuẩn sử dụng `scikit-learn`, in ra độ chính xác trên tập test.

## 🚀 Hướng dẫn cài đặt và chạy thử

**1. Cài đặt môi trường**
Cài đặt các thư viện cần thiết thông qua pip:
```bash
pip install pandas numpy matplotlib scikit-learn sqlalchemy
```

**2. Cấu hình Cơ sở dữ liệu (Tùy chọn)**
Để chạy các file `connect_db.py` và `end_to_end_knn.py`, bạn cần có PostgreSQL chạy ở localhost với thông tin mặc định:
* User: `postgres`
* Password: `admin`
* Port: `5432`

**3. Chạy các tính năng**
* Kiểm tra thuật toán KNN bằng Scikit-Learn:
  ```bash
  python sklearn_knn.py
  ```
* Chạy mô hình phân tích tự xây dựng:
  ```bash
  python knn.py
  ```
* Xem biểu đồ phân bố:
  ```bash
  python draw_iris.py
  ```
