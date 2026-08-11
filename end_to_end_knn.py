import pandas as pd
import numpy as np
from sqlalchemy import create_engine

chuoi_ket_noi = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = create_engine(chuoi_ket_noi)

print("1. Dang ket noi du lieu tu SQL server")
df_sql = pd.read_sql('SELECT * FROM iris', engine)

training_data = []
for index, row in df_sql.iterrows():
    features = [
        row['SepalLengthCm'],
        row['SepalWidthCm'], 
        row['PetalLengthCm'], 
        row['PetalWidthCm']
        ]
    label = row['Species']
    training_data.append((features, label))

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

def predict_knn(training_data, new_flower_features, k):
    distances = []

    for features, label in training_data:
        dist = euclidean_distance(new_flower_features, features)
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])
    
    k_nearest_neighbors = distances[:k]

    votes = {}
    for dist, label in k_nearest_neighbors:
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1
    
    max_votes = 0
    predict_knn = ''
    for label, count in votes.items():
        if count > max_votes:
            max_votes = count
            predicted_label = label

    return predicted_label

hoa_bi_an = [6.1, 3.1, 5.2, 1.9] 
k = 5

print(f"2. Bắt đầu dùng KNN phân tích {len(training_data)} bông hoa...")
ket_qua = predict_knn(training_data, hoa_bi_an, k)

print("\n=== KẾT QUẢ DỰ ĐOÁN ===")
print(f"Bông hoa với kích thước {hoa_bi_an} được AI dự đoán là giống: {ket_qua}")