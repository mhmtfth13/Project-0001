from isyatirimhisse import StockData, Financials
import sqlalchemy
stock_data = StockData()

df = stock_data.get_data(
    symbols=['THYAO','PGSUS'],
    start_date = '02-01-2023',
    exchange='0',
    frequency='1w',
    observation='mean'
)
engine = sqlalchemy.create_engine('mssql+pyodbc://./VeriCekme?driver=ODBC+Driver+17+for+SQL+Server')
df.to_sql(name='HISSELER',con=engine,index=False,if_exists='fail')