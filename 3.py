# from lib2to3.pgen2 import driver
# from typing_extensions import Self
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from pywinauto.application import Application
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import pywinauto

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")

CHROME_DRIVER_PATH = (
    "C:\python_selenium_auto_vir\chromedriver.exe")  # 크롬 드라이버 경로
driver = webdriver.Chrome(
    executable_path=CHROME_DRIVER_PATH, chrome_options=options)

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(options=options)

# windows을 최대 사이즈로 조절
driver.maximize_window()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 함수 종료 방지
# while(True):
#     pass

# WebRTC_Internal 페이지로 이동
driver.get('chrome://webrtc-internals/')
print("WebRTC_Internal 페이지로 이동합니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# WebRTC_Internal 페이지에서 Read stats From 선택
formselect = driver.find_element(
    By.XPATH, "//*[@id = 'statsSelectElement']")
formselect.click()
print("Read stats From을 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# WebRTC_Internal 페이지에서 Read stats From을 Legacy Non-Standard (callback-based) getStats() API로 선택
api_2 = driver.find_element(
    By.XPATH, "//*[@id = 'statsSelectElement']/option[2]")
api_2.click()
print("Legacy Non-Standard (callback-based) getStats() 선택했습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 새창 열기
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

# 현재 활성화 된 탭
print(driver.window_handles)

# STG VIRNECT로 이동
driver.get('https://stgwww.virnect.com')
print("STG VIRNECT로 이동합니다.")

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Log in 버튼을 클릭하여 로그인센터로 이동한다.
logincenter = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class = 'login-wrap']/li[@class = 'login-btn']")))
logincenter.click()
print("로그인센터로 이동합니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 아이디 입력창 위치 찾기 및 아이디 입력
userid = driver.find_element(
    By.XPATH, "//div[@class ='email-input el-input el-input--suffix']/input[1]").send_keys('maxgim875@gmail.com')
print("이메일 계정이 입력되었습니다.")
# 이메일 계정 정보
# stgim875@gmail.com
# stgim1516@gmail.com
# stgim1314@gmail.com
# stgim1112@gmail.com
# stgim789@gmail.com
# stgim456@gmail.com
# stgim123@gmail.com

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 패스워드 입력창 위치 찾기 및 패스워드 입력
userpw = driver.find_element(
    By.XPATH, "//div[@class = 'password-input el-input el-input--suffix']/input[1]").send_keys('@rokmc875th')
print("패스워드가 입력되었습니다")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 로그인 클릭
loginbtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@class = 'el-button next-btn block-btn el-button--info']"))
)
loginbtn.click()
print("정상적으로 로그인되었습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 썸네일 버튼을 클릭
thumbnailbtn = driver.find_element(
    By.XPATH, "//*[@class = 'link-btn status-btn']")
thumbnailbtn.click()
print("썸네일 버튼을 클릭하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Remote 메뉴 클릭
Remotemenu = driver.find_element(
    By.XPATH, "//a[@href ='https://stgremote.virnect.com']")
Remotemenu.click()
print("Remote 메뉴를 클릭하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 쿠키 및 이용통계 수집 동의 모달
cookiebtn = driver.find_element(
    By.XPATH, "//*[@class = 'cookie-policy-wrapper__submit-button']")
cookiebtn.click()
print("쿠키 및 이용통계 수집 동의하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 생성 버튼 클릭
remotecreatebtn = driver.find_element(
    By.XPATH, "//*[contains(text(), '원격 협업 생성')]")
remotecreatebtn.click()
print("원격 협업 생성 버튼을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 생성하기 모달창 정상 출력 확인
if driver.find_element(By.XPATH, "//*[@class = 'modal--body']").is_displayed():
    print("원격 협업 생성하기 모달창이 정상적으로 출력되었습니다.")
else:
    print("원격 협업 생성하기 모달창이 출력되지 않았습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# [예외 처리 코드: 멤버 리스트가 닫혀 있을 경우 select 버튼 클릭]
if driver.find_element(By.XPATH, "//*[@class = 'collapsible member-collapsible opend decorated']").is_displayed():
    print("원격 협업 멤버 리스트가 정상적으로 출력됩니다.")
else:
    selectbtn = driver.find_element(
        By.XPATH, "//*[@class = 'collapsible__button decorated']")
    selectbtn.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# Default 원격 협업 이름 지우기
placeholder = driver.find_element(
    By.XPATH, "//*[@class = 'modal--body']/div[@class ='createroom']/section[@class ='createroom-info']/figure[@class ='inputrow'][1]/input[@class = 'inputrow-input input']")
placeholder.clear()
print("Default 원격 협업 이름을 지웠습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 협업 그룹 이름 입력하기
# 협업 이름은 _인수테스트
Cooperationname = driver.find_element(
    By.XPATH, "//*[@class = 'modal--body']/div[@class ='createroom']/section[@class ='createroom-info']/figure[@class ='inputrow'][1]/input[@class = 'inputrow-input input']")
Cooperationname.send_keys('인수 테스트')
print("원격 협업 이름은 인수 테스트로 입력하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# # 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기
# # stgim875@gmail.com[1]
# # stgim1516@gmail.com[1]
# # stgim1314@gmail.com[2]
# # stgim1112@gmail.com[3]
# # stgim789@gmail.com[4]
# # stgim456@gmail.com[5]
# # stgim123@gmail.com[6]
manageradd = driver.find_element(
    By.XPATH, "//*[@class = 'collapsible__content opend']/div[@class = 'widecard choice'][1]")
manageradd.click()
print("stgim875@gmail.com 멤버를 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 원격 협업 생성하기 시작하기 버튼 클릭
createroombtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class = 'btn large createroom-info__button']")))
createroombtn .click()
print("원격 협업 생성하기 시작 버튼을 선택하였습니다.")

# permission 동의 팝업창 확인 선택하기
# 카메라 및 마이크 => options.add_argument("--use-fake-ui-for-media-stream")으로 fake 처리함

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 웹에서 원격 협업 요청 후, 수동으로 직접 Remote Mobile에서 로그인하고 원격 협업을 선택 할 수 있는 물리적인 시간이 필요함
# 50초 암묵적 대기
time.sleep(50)
print("Mobile Remote Application을 실행해 주세요.")
print("모바일 앱에서 알림을 확인해주세요.")

# 모바일 협업 인원 더블 클릭하여 선택하기
participantvideo = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class = 'participant-video']/div[@class = 'participant-video__stream']")))
action = ActionChains(driver)
action.double_click(participantvideo).perform()
print("모바일 협업 인원을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 전체 공유 버튼 클릭
selectviewbutton = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '전체 공유')]")))
selectviewbutton.click()
print("모바일 협업 인원을 전체 공유하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 협업 보드 탭 클릭
headerlnbbtn2 = driver.find_element(
    By.XPATH, "//*[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][2]/button[@class = 'header-lnb__button']")
headerlnbbtn2.click()
print("협업 보드 탭을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 협업 보드에서 파일 추가 메뉴 클릭
uploadbtn = driver.find_element(
    By.XPATH, "//*[@class = 'upload-list__button']")
uploadbtn.click()
print("협업 보드에서 파일 추가 메뉴를 선택하였습니다.")

# 3초 암묵적 대기
time.sleep(5)

# 열기창은 Default가 User 폴더임
#-*-coding:utf-8-*-
# 애플리케이션 모듈 선언
app = pywinauto.application.Application()
app.connect(title_re='열기', class_name='#32770')
window = app['열기']
window.set_focus()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# PNG 파일 추가하기
# # 파일 이름(N)에 검색할 이미지 이름 입력
window['파일 이름(&N):Edit'].type_keys('qa1.png')

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 이미지 이름 입력 후, 열기 버튼 클릭
window['열기(&O)Button'].click()

# png 파일 추가하기
print("qa1.png 파일을 추가 하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 협업 보드 탭 클릭
if driver.find_element(
    By.XPATH, "//*[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][2]/button[@class = 'header-lnb__button']").click():
    print("협업 보드 탭을 선택하였습니다.")
elif 






# 협업 보드 > qa1.png 더블 클릭하여 화면 불러오기
sharingimage1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class = 'sharing-image']/button[@class = 'sharing-image__item'][1]")))
action = ActionChains(driver)
action.double_click(sharingimage1).perform()
print("qa1.png 이미지를 화면에 불러왔습니다.")


