import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Chuẩn bị dữ liệu (Vẫn dùng Pandas để đọc như cũ)
df = pd.read_csv('Iris.csv')

# Bóc tách bảng dữ liệu thành 2 phần chuẩn mực:
# X (Đặc trưng/Features): Bỏ đi cột nhãn và cột ID (nếu có)
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
# y (Nhãn/Label): Chỉ lấy cột kết quả cuối cùng
y = df['Species']

# Cắt dữ liệu ra làm 2 phần: 80% để học, 20% để làm bài kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 2. KHỞI TẠO VÀ HUẤN LUYỆN MÔ HÌNH (SCIKIT-LEARN)
# ==========================================
print("Đang gọi AI và bắt đầu quá trình học tập...")

# Dòng 1: Khởi tạo mô hình KNN với K=5
mo_hinh_ai = KNeighborsClassifier(n_neighbors=5)

# Dòng 2: Ép mô hình học từ tập dữ liệu huấn luyện (Quá trình Fit)
mo_hinh_ai.fit(X_train, y_train)

# Dòng 3: Bắt AI làm bài kiểm tra trên tập dữ liệu Test chưa từng thấy
du_doan = mo_hinh_ai.predict(X_test)

# ==========================================
# 3. ĐÁNH GIÁ KẾT QUẢ VÀ SỬ DỤNG THỰC TẾ
# ==========================================
# Chấm điểm bài kiểm tra tự động
diem_so = accuracy_score(y_test, du_doan)
print(f"Độ chính xác của AI trên tập kiểm tra: {diem_so * 100}%")

# Bác nông dân mang đến bông hoa bí ẩn hôm trước: [6.1, 3.1, 5.2, 1.9]
hoa_bi_an = pd.DataFrame([[6.1, 3.1, 5.2, 1.9]], columns=X.columns)
ket_qua_hoa_moi = mo_hinh_ai.predict(hoa_bi_an)

print("\n=== KẾT QUẢ DỰ ĐOÁN THỰC TẾ ===")
print(f"Bông hoa bí ẩn được định danh là: {ket_qua_hoa_moi[0]}")