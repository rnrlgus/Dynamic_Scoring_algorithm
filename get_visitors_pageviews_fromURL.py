import requests
from bs4 import BeautifulSoup

url = 'https://website.informer.com/op.gg'

# 데일리 뷰, visitors 추출
def get_visitors_and_pageviews(url):
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        #문자열
        visitors = soup.select_one('#visitors > b').get_text()
        pageviews = soup.select_one('#pageviews > b').get_text()
        #정수
        visitors_int = int(visitors.replace(" ", ""))
        pageviews_int = int(pageviews.replace(" ", ""))
        
        print("url: ", url)
        print("visitors: ", visitors_int)
        print("pageviews: ", pageviews_int)
    else:
        print(response.status_code)
        
get_visitors_and_pageviews(url)