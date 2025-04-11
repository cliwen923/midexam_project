import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime

def scrape_bitcoin_price():
    url = httpswww.tradingview.comsymbolsBTCUSDT  # 請替換成您選擇的頁面 URL
    headers = {'User-Agent' 'Mozilla5.0 (Windows NT 10.0; Win64; x64) AppleWebKit537.36 (KHTML, like Gecko) Chrome58.0.3029.110 Safari537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 如果發生錯誤，例如 404 或 500，會拋出異常
        soup = BeautifulSoup(response.content, 'html.parser')

        # 您需要檢查 TradingView 頁面的 HTML 結構，找到包含比特幣價格的元素
        # 這是一個範例選擇器，您可能需要根據實際情況調整
        price_element = soup.find('span', {'class' 'tv-symbol-price-quote__value'})

        if price_element:
            price = price_element.text.strip()
            timestamp = datetime.now().isoformat()
            return {timestamp timestamp, price price}
        else:
            print(找不到比特幣價格元素。請檢查網頁結構。)
            return None

    except requests.exceptions.RequestException as e
        print(f抓取網頁時發生錯誤：{e})
        return None

def save_to_json(data, filename=static.json)
    if data
        with open(filename, 'w') as f
            json.dump(data, f)
        print(f資料已儲存至 {filename})

def save_to_csv(data, filename=static.csv)
    if data
        with open(filename, 'a', newline='') as f
            writer = csv.writer(f)
            if f.tell() == 0  # 如果檔案是空的，寫入標題
                writer.writerow([timestamp, price])
            writer.writerow([data[timestamp], data[price]])
        print(f資料已附加至 {filename})

if __name__ == __main__
    bitcoin_data = scrape_bitcoin_price()
    if bitcoin_data
        save_to_json(bitcoin_data)
        save_to_csv(bitcoin_data)