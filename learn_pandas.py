import pandas as pd

# 1. Đọc toàn bộ file CSV chỉ với 1 dòng lệnh
# Lưu ý: Sửa tên 'Iris.csv' cho đúng với file của bạn nếu cần
df = pd.read_csv('Iris.csv')

# 2. Xem 5 dòng đầu tiên
print("--- 5 DÒNG DỮ LIỆU ĐẦU TIÊN ---")
print(df.head())

# 3. Phân tích cấu trúc dữ liệu
print("\n--- THÔNG TIN CẤU TRÚC (INFO) ---")
df.info()

# 4. Thống kê toán học tự động
print("\n--- THỐNG KÊ TOÁN HỌC (DESCRIBE) ---")
print(df.describe())

# 5. Giải quyết thử thách: Lọc dữ liệu nâng cao
print("\n--- KẾT QUẢ LỌC DỮ LIỆU ---")
# Cú pháp lọc: df[(Điều kiện 1) & (Điều kiện 2)]
# Giả sử cột tên loài là 'Species' và cột chiều dài đài hoa là 'SepalLengthCm'
loc_hoa = df[(df['Species'] == 'Iris-setosa') & (df['SepalLengthCm'] > 5.0)]

print(f"Tìm thấy {len(loc_hoa)} bông hoa thỏa mãn điều kiện:")
print(loc_hoa[['SepalLengthCm', 'Species']].head())