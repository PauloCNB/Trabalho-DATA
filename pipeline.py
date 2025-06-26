import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('temperature.csv')
engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')
df.to_sql('temperature_readings', con=engine, if_exists='replace', index=False)
print("Dados inseridos com sucesso!")