import requests
from bs4 import BeautifulSoup

url = 'https://www.koreanft365days.com/mint'
tmp = 'https://plugin.eventscalendar.co/widget.html?pageId=lysrv&compId=comp-kxlyxx7i&viewerCompId=comp-kxlyxx7i&siteRevision=663&viewMode=site&deviceType=desktop&locale=ko&tz=Asia%2FSeoul&regionalLanguage=ko&width=940&height=1316&instance=OFmR3y9jDUY7bm1fmaq9Re_FGa1pNM5LZ2FBXMdyyvg.eyJpbnN0YW5jZUlkIjoiNTAxOWU3OTUtYTRhNS00OTdlLWJlOTUtZWZhNDk3NjIyYTMwIiwiYXBwRGVmSWQiOiIxMzNiYjExZS1iM2RiLTdlM2ItNDliYy04YWExNmFmNzJjYWMiLCJzaWduRGF0ZSI6IjIwMjItMDMtMjhUMDg6MDA6MjAuOTU4WiIsInZlbmRvclByb2R1Y3RJZCI6InByZW1pdW0iLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQ4ODNiODYxLTY5YWItNDVkNC1iOWYzLTQ5MjVhNDY5ZjA3OCIsInNpdGVPd25lcklkIjoiNzc1OTQyYTctMTZmYS00NjAxLWI1NDktNGYyMjFlZWI2YjdiIn0&currency=KRW&currentCurrency=KRW&commonConfig=%7B%22brand%22:%22wix%22,%22bsi%22:%22931b4d3a-cf8c-4270-b608-ca6e589a4d7b%7C1%22,%22BSI%22:%22931b4d3a-cf8c-4270-b608-ca6e589a4d7b%7C1%22%7D&vsi=6f6fda03-2e4a-483a-8a90-b2aec61ff6d3'

def get_minting_calender(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        
        #tmp = soup.select("#weeks-container")
        tmp = soup.select('#weeks-container > div:nth-child(1) > div.day.ng-scope.inactive > div.events > div:nth-child(1) > a > span')
        
        print(tmp)
        
    else:
        print(response.status_code)
        
get_minting_calender(tmp)
