import pandas as pd
from sqlalchemy import create_engine

chuoi_ket_noi = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = create_engine(chuoi_ket_noi)

print("---Day du lieu len protgresql---")
df_csv = pd.read_csv('iris.csv')

df_csv.to_sql('iris', engine, if_exists='replace', index=False)
print("Da day du lieu len PostgreSQL")

cau_lenh_sql = 'SELECT * FROM iris'

print("Dang doc du lieu tu CSDL PostgreSQL")
df = pd.read_sql(cau_lenh_sql, engine)

print("\nDu lieu da duoc doc xong:")
print(df.head())
print(f"\nTong so dong keo ve: {len(df)}")