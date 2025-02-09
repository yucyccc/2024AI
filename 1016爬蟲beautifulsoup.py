

import requests
from bs4 import BeautifulSoup

url = "https://2023ntcu.ntcu.edu.tw/"
html = requests.get(url)
html.encoding="utf-8"
#print(html.text)列印網頁內容
soup = BeautifulSoup(html.text,"html.parser")
#print(soup.prettify())

#htmllist = html.text.splitlines()  把html原始碼以每一列分割成字串，並去除跳列字元
#print(htmllist) 

#統計關鍵字出現次數
keyword ="臺中"
# 使用 BeautifulSoup 的 find_all 方法找出所有包含關鍵字的元素   
elements_with_keyword = soup.find_all(string=lambda text: keyword in text)

# 計算關鍵字出現的次數
keyword_count = len(elements_with_keyword)

print(f"關鍵字「{keyword}」在網頁中出現了 {keyword_count} 次。")