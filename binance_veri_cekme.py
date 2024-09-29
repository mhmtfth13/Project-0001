# import json
# import requests
# import pandas as pd
# from datetime import datetime
# import sqlalchemy

# # API anahtarlarını yükle
# with open(r'C:\Users\Administrator\Desktop\Projeler\TEST1\binanceTest1\keys.json', "r") as f:
#     api_config = json.load(f)

# headers = api_config.get("headers", {})
# url = "https://api.binance.com/api/v3/klines"

# # Semboller
# symbols = ["BNBUSDT", "BTCUSDT", "ETHUSDT"]

# # Tarihleri belirle
# start_time = int(datetime(2024, 1, 1).timestamp() * 1000)  # 1 Ocak 2024
# end_time = int(datetime.now().timestamp() * 1000)  # Şu anki zaman

# # Verileri depolamak için bir liste
# all_data = []

# for symbol in symbols:
#     params = {
#         "symbol": symbol,
#         "interval": "1h",
#         'limit': '1000',
#         'startTime': start_time,
#         'endTime': end_time
#     }
    
#     # İsteği gönder
#     response = requests.get(url, headers=headers, params=params)
    
#     # Yanıtı kontrol et
#     if response.status_code == 200:
#         responseData = response.json()
        
#         # DataFrame'e dönüştür
#         df = pd.DataFrame(responseData)
#         df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume", 
#                        "Close Time", "Quote Asset Volume", "Number of Trades", 
#                        "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "IGNORE"]
        
#         # Zaman damgalarını datetime formatına dönüştür
#         df["Open Time"] = pd.to_datetime(df["Open Time"], unit='ms')
#         df["Close Time"] = pd.to_datetime(df["Close Time"], unit='ms')
        
#         # İlgili sütunları seç
#         df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]
        
#         # Sembol sütunu ekle
#         df["Symbol"] = symbol
        
#         # DataFrame'i listeye ekle
#         all_data.append(df)
#     else:
#         print(f"Hata ({symbol}): {response.status_code} - {response.text}")

# # Tüm verileri birleştir
# final_df = pd.concat(all_data, ignore_index=True)

# # SQL Server bağlantısını oluştur
# try:
#     engine = sqlalchemy.create_engine('mssql+pyodbc://./VeriCekme?driver=ODBC+Driver+17+for+SQL+Server')

#     # Verileri SQL Server'a yaz
#     final_df.to_sql(name='BinanceVeri', con=engine, index=False, if_exists='fail')
#     print("Veriler başarıyla SQL Server'a yazıldı.")
# except Exception as e:
#     print(f"SQL Server'a bağlanırken bir hata oluştu: {e}")


# Yukaridaki kod sql'e 



import json
import requests
import pandas as pd
from datetime import datetime

# API anahtarlarını yükle
with open(r'C:\Users\Administrator\Desktop\Projeler\TEST1\binanceTest1\keys.json', "r") as f:
    api_config = json.load(f)

headers = api_config.get("headers", {})
url = "https://api.binance.com/api/v3/klines"

# Semboller
symbols = ["BNBUSDT", "BTCUSDT", "ETHUSDT"]

# Tarihleri belirle
start_time = int(datetime(2024, 1, 1).timestamp() * 1000)  # 1 Ocak 2024
end_time = int(datetime.now().timestamp() * 1000)  # Şu anki zaman

# Verileri depolamak için bir liste
all_data = []

for symbol in symbols:
    params = {
        "symbol": symbol,
        "interval": "1h",
        'limit': '1000',
        'startTime': start_time,
        'endTime': end_time
    }
    
    # İsteği gönder
    response = requests.get(url, headers=headers, params=params)
    
    # Yanıtı kontrol et
    if response.status_code == 200:
        responseData = response.json()
        
        # DataFrame'e dönüştür
        df = pd.DataFrame(responseData)
        df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume", 
                       "Close Time", "Quote Asset Volume", "Number of Trades", 
                       "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "IGNORE"]
        
        # Zaman damgalarını datetime formatına dönüştür
        df["Open Time"] = pd.to_datetime(df["Open Time"], unit='ms')
        df["Close Time"] = pd.to_datetime(df["Close Time"], unit='ms')
        
        # İlgili sütunları seç
        df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]
        
        # Sembol sütunu ekle
        df["Symbol"] = symbol
        
        # DataFrame'i listeye ekle
        all_data.append(df)
    else:
        print(f"Hata ({symbol}): {response.status_code} - {response.text}")

# Tüm verileri birleştir
final_df = pd.concat(all_data, ignore_index=True)

# Verileri Excel dosyasına kaydet
excel_path = r'C:\Users\Administrator\Desktop\Projeler\TEST1\binance_data.xlsx'
final_df.to_excel(excel_path, index=False)

print(f"Veriler başarıyla {excel_path} dosyasına kaydedildi.")