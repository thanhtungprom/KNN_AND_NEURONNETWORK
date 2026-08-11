import csv
import math
from pickletools import dis

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i]-point2[i])**2
    return math.sqrt(distance)

def load_data(file_path):
    dataset = []
    with open(file_path,'r') as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            if len(row) >=5 :
                features = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
                label = row[5]
                dataset.append((features, label))
    return dataset

def predict_knn(data, new_flower_features, k):
    distance = []
    for features, label in data:
        dist = euclidean_distance(new_flower_features, features)
        distance.append((dist, label))
    distance.sort(key = lambda x:x[0])
    neighbors = distance[:k]

    votes = {}
    
    for dist, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    
    predict_label = None
    max_votes = 0
    for label, count in votes.items():
        if count > max_votes:
            max_votes = count
            predict_label = label
    return predict_label



if __name__ == "__main__":
    data = load_data('Iris.csv')
    print(f"Number of read samples: {len(data)}")

    new_flower_features = [5.1, 3.5, 1.4, 0.2]
    k = 3
    predicted_label = predict_knn(data, new_flower_features, k)
    print(f"Predicted label for the new flower: {predicted_label}")
