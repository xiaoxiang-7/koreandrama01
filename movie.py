# 導入 firebase_admin 模組
import firebase_admin

# 從 firebase_admin 模組中導入 credentials 和 firestore
from firebase_admin import credentials, firestore

# 載入服務帳戶金鑰
cred = credentials.Certificate("serviceAccountKey.json")

# 將服務帳戶金鑰設定到 Firebase 應用程式中
firebase_admin.initialize_app(cred)

# 建立一個 Firestore 資料庫的客戶端
db = firestore.client()

# 導入 requests 和 BeautifulSoup 模組
import requests
from bs4 import BeautifulSoup

# 定義要爬取的網頁網址
url = "https://jumi.tv/show/23.html"

# 使用 requests.get() 方法，取得網頁資料
data = requests.get(url)

# 設定網頁資料的編碼方式
data.encoding = "utf-8"

# 使用 BeautifulSoup 將網頁資料轉換成結構化的資料
sp = BeautifulSoup(data.text, "html.parser")

# 使用 find_all() 方法，找出所有 class 為 "title" 的 h4 標題
h4_titles = sp.find_all("h4", class_="title")
for h4_title in h4_titles[:10]:
  text = h4_title.text # 取出 h4 標題的文字內容
  link = h4_title.find("a").get("href") # 取出 h4 標題的文字超連結

  # 使用 db.collection("最新韓劇").document() 方法，建立一個文件
  doc_ref = db.collection("最新韓劇").document()
  
  # 建立一個文件資料結構，其中包含 h4 標題的文字內容和超連結
  doc = {
      "text": text,
      "link": link
  }

  # 將文件資料結構儲存到文件中
  doc_ref.set(doc)