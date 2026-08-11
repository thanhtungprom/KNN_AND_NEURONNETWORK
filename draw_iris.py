import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

setosa = df[df['Species'] == 'Iris-setosa']
versicolor = df[df['Species'] == 'Iris-versicolor']
virginica = df[df['Species'] == 'Iris-virginica']

plt.figure(figsize = (10,6))

plt.scatter(setosa['PetalLengthCm'],setosa['PetalWidthCm'], color = 'red', label = 'Setosa', alpha = 0.7)
plt.scatter(versicolor['PetalLengthCm'],versicolor['PetalWidthCm'], color = 'green', label = 'Versicolor', alpha = 0.7)
plt.scatter(virginica['PetalLengthCm'],virginica['PetalWidthCm'], color = 'blue', label = 'Virginica', alpha = 0.7)

plt.title('Phan bo cac giong hoa Iris trong khong gian 2D',fontsize = 14)
plt.xlabel('Chieu dai canh hoa')
plt.ylabel('Chieu rong canh hoa')
plt.legend()
plt.grid(True, linestyle='--', alpha = 0.5)

print("Dang mo cua so bieu do")
plt.show()

