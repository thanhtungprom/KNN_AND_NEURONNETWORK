import numpy as np
import time

hoa_moi = np.array([5.1, 3.5, 1.4, 0.2])

print("Dang tao 1 trieu diem du lieu ao")
kho_du_lieu = np.random.rand(1000000,4) * 10

print("\nBat dau do thoi gian Numpy tinh 1 trieu khoang cach")
start_time = time.time()

khoang_cach_mang = np.sqrt(np.sum((kho_du_lieu - hoa_moi)**2, axis = 1))

thoi_gian_ket_thuc = time.time()

thoi_gian_chay = thoi_gian_ket_thuc - start_time
print(f"Da tinh xong {len(khoang_cach_mang)} khoang cach")
print("Thoi gian Numpy tinh 1 trieu khoang cach:", thoi_gian_chay)

print("\n5 khoang cach dau tien")
print(khoang_cach_mang[:5])