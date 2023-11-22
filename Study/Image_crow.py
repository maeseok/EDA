from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import os

#Chrome driver
print('Loading...')
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(30)

#폴더 생성 함수
def createFolder () :
    if os.path.isdir("C:\\Users\\Public\\{}".format("인물사진")) == False :
        os.mkdir("C:\\Users\\Public\\{}".format("인물사진"))
        print('폴더 생성 완료')
    else :
        print('이미 존재하는 폴더입니다.')


#폴더 생성
createFolder()

#배우 리스트
#https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD
#https://justweon-dev.tistory.com/m/41

# 사이트 접속하기 -> 이걸로도 가능하게 코드 수정해놓을 것 (인물 당 20장 정도 사진 저장 ) -> 발표할 때 코드 더 성의있게 한 부분?
keyword=["수지","이선균","황정민"] #인물 리스트만 설정하면 될 듯
for i in keyword:
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query={}'.format(i)
    driver.get(url)
    
    #이미지 src 추출
    img = driver.find_elements(By.CSS_SELECTOR, '._img')
    src = [i.get_attribute('src') for i in img]
    print(src)
    #이미지 URL 다운로드
    urllib.request.urlretrieve(src[0], "C:\\Users\\Public\\인물사진\\{}.jpg".format(i))