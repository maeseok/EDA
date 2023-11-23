from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

#Chrome driver
print('Loading...')
options = ChromeOptions()
options.add_argument("headless") #백그라운드 실행
#options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(30)

#폴더 생성 함수
def createFolder (name) :
    if os.path.isdir("./{}".format(name)) == False :
        os.mkdir("./{}".format(name))
        print('{} 폴더 생성 완료'.format(name))
    else :
        print('이미 존재하는 폴더입니다.')

def scroll_down(cnt):
    for i in range(cnt):
        driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
        time.sleep(2)
        
''' 대용량 ver
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click() #스크롤을 내리다 보면 "결과 더보기"가 뜨는 경우 이를 클릭해준다
            except:
                break
        last_height = new_height'''

#배우 이미지 다운로드 함수
def DownloadImage(keyword,size):
    for i in range(len(keyword)):
        url = 'https://www.google.com/search?tbm=isch&q={}'.format(keyword[i])
        driver.get(url)
        scroll_down(size//30)
        createFolder(keyword[i])
        #이미지 src 추출
        img = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
        src = [i.get_attribute('src') for i in img]
        for j in range(size):
            #이미지 URL 다운로드
            try:
                print("[%] Download : Success  ({}{})".format(keyword[i],j+1))
                print()
                urllib.request.urlretrieve(src[j], "./{}\\Image_{}.jpg".format(keyword[i],j+1))
            except:
                print("[%] Download : Fail")

#폴더 생성
createFolder("배우사진")
os.chdir('./배우사진')

#배우 리스트
#https://namu.wiki/w/%EB%B0%B0%EC%9A%B0/%ED%95%9C%EA%B5%AD

# 사이트 접속하기
keyword=["황정민"] #인물 리스트만 설정하면 될 듯
DownloadImage(keyword,60)