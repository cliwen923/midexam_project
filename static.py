import requests
import json
import csv
from datetime import datetime
import os

def scrape_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "BTCUSDT"}  # 您可以更改交易對，例如 BTCEUR

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 如果發生錯誤，例如 404 或 500，會拋出異常
        data = response.json()
        price = data["price"]
        timestamp = datetime.now().isoformat()
        return {"timestamp": timestamp, "price": price}
    except requests.exceptions.RequestException as e:
        print(f"抓取幣安 API 時發生錯誤：{e}")
        return None
    except KeyError:
        print("無法在幣安 API 回應中找到 'price'。請檢查 API 回應格式。")
        return None

def save_to_json(data, filename="static.json"):
    existing_data = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]  # 如果現有資料不是列表，則將其轉換為列表
        except json.JSONDecodeError:
            print(f"警告：無法解碼 {filename} 中的現有 JSON。將覆寫為新資料。")
            existing_data = []
        except FileNotFoundError:
            pass  # 如果檔案不存在，則保持 existing_data 為空列表

    existing_data.append(data)

    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=4)
    print(f"從幣安獲取的比特幣價格已附加至 {filename}")

def save_to_csv(data, filename="static.csv"):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "price"])
        writer.writerow([data["timestamp"], data["price"]])
    print(f"從幣安獲取的比特幣價格已附加至 {filename}")

if __name__ == "__main__":
    bitcoin_data = scrape_bitcoin_price()
    if bitcoin_data:
        save_to_json(bitcoin_data)
        save_to_csv(bitcoin_data)