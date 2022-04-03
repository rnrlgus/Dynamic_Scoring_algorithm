from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = 'https://www.koreanft365days.com/mint'
tmp = 'https://plugin.eventscalendar.co/widget.html?pageId=lysrv&compId=comp-kxlyxx7i&viewerCompId=comp-kxlyxx7i&siteRevision=663&viewMode=site&deviceType=desktop&locale=ko&tz=Asia%2FSeoul&regionalLanguage=ko&width=940&height=1316&instance=OFmR3y9jDUY7bm1fmaq9Re_FGa1pNM5LZ2FBXMdyyvg.eyJpbnN0YW5jZUlkIjoiNTAxOWU3OTUtYTRhNS00OTdlLWJlOTUtZWZhNDk3NjIyYTMwIiwiYXBwRGVmSWQiOiIxMzNiYjExZS1iM2RiLTdlM2ItNDliYy04YWExNmFmNzJjYWMiLCJzaWduRGF0ZSI6IjIwMjItMDMtMjhUMDg6MDA6MjAuOTU4WiIsInZlbmRvclByb2R1Y3RJZCI6InByZW1pdW0iLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQ4ODNiODYxLTY5YWItNDVkNC1iOWYzLTQ5MjVhNDY5ZjA3OCIsInNpdGVPd25lcklkIjoiNzc1OTQyYTctMTZmYS00NjAxLWI1NDktNGYyMjFlZWI2YjdiIn0&currency=KRW&currentCurrency=KRW&commonConfig=%7B%22brand%22:%22wix%22,%22bsi%22:%22931b4d3a-cf8c-4270-b608-ca6e589a4d7b%7C1%22,%22BSI%22:%22931b4d3a-cf8c-4270-b608-ca6e589a4d7b%7C1%22%7D&vsi=6f6fda03-2e4a-483a-8a90-b2aec61ff6d3'

# using selenium     
def get_minting_calender(url):
    driver = webdriver.Chrome('C:/Users/Koo/dynamic_scoring_algorithm/chromedriver.exe')
    driver.implicitly_wait(3)   
    driver.get(url)
    
    items = driver.find_elements(By.TAG_NAME, 'span')
    
    for i in items:
        print(i.get_attribute('outerHTML'))
        
    items[10].click() # 팝업창 띄우기 하나 완성하고 나중에 반복문으로 다 돌아야함
    
    item = driver.find_element(By.CSS_SELECTOR, '#weeks-container > div:nth-child(1) > div:nth-child(4) > div.events > div:nth-child(3) > div > div.full-height > div > div > div.popup-main.atc-parent > div')
    #weeks-container > div:nth-child(2) > div:nth-child(2) > div.events > div:nth-child(3) > div > div.full-height > div > div > div.popup-main.atc-parent
    #weeks-container > div:nth-child(2) > div:nth-child(1) > div.events > div > div > div.full-height > div > div > div.popup-main.atc-parent > div
    # item마다 다 달라........ ㅠㅠ 클릭했을때 popup 부분을 find_element 활용해서 해봐야겠음
    tmp = item.get_attribute('outerHTML') # 팝업창 html 소스 (문자열 형태)
    print(tmp)
    print("------------------------------------------------------------------------------------------------")
    
    # 얻은 html 코드를 bs를 사용해서 원하는 정보들 추출해볼까 싶다
    html = BeautifulSoup(tmp, 'html.parser') # 팝업창 html 소스 (html 형태)
    
    texts = html.get_text() # 텍스트 추출
    hrefs_tmp = html.select('a') # 링크 추출
    hrefs = [] # 링크 리스트
    
    
    print(texts)
    print("-----------------------------------------------------------------------------------------------")
    for h in hrefs_tmp:
        href_tmp = h.attrs['href']
        
        if href_tmp in hrefs:
            continue
        else:
            hrefs.append(href_tmp)
    print(hrefs)
    print("-----------------------------------------------------------------------------------------------")
    
    while(True): pass # 셀레니움 창 유지시키기 위해 (함수 중료될 때 셀레니움도 같이 종료돼서 꺼지는거임)

    
get_minting_calender(tmp)
