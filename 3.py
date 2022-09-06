# from lib2to3.pgen2 import driver
# from typing_extensions import Self
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
# Using a Pen or Mouse actions
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.action_builder import KeyInput
from selenium.webdriver.common.actions.action_builder import PointerActions
from selenium.webdriver.common.actions.action_builder import PointerInput
# Screenshot
# from Screenshot import Screenshot_Clipping
from selenium.webdriver.common.actions.mouse_button import MouseButton

import uiautomation as auto
import time
import os
import pywinauto

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행

CHROME_DRIVER_PATH = (
    "C:\python_selenium_auto_vir\chromedriver.exe")  # 크롬 드라이버 경로
driver = webdriver.Chrome(
    executable_path=CHROME_DRIVER_PATH, chrome_options=options)

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(options=options)

# windows을 최대 사이즈로 조절
# driver.maximize_window()

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
print("Legacy Non-Standard (callback-based) getStats()로 선택했습니다.")

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
    By.XPATH, "//div[@class ='email-input el-input el-input--suffix']/input[1]")
userid.send_keys('maxgim875@gmail.com')
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
    By.XPATH, "//div[@class = 'password-input el-input el-input--suffix']/input[1]")
userpw.send_keys('@rokmc875th')
print("패스워드가 입력되었습니다")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 로그인 클릭
loginbtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@class = 'el-button next-btn block-btn el-button--info']")))
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

# 현재 활성화 된 탭
print(driver.window_handles)

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

########## WebRTC 띄우기 > STG 홈 화면 > 로그인센터 로그인 > 원격협업 생성까지 대략 15초 소요됨 ##########

# 웹에서 원격 협업 요청 후, 수동으로 직접 Remote Mobile에서 로그인하고 원격 협업을 선택 할 수 있는 물리적인 시간이 필요함
print("Mobile Remote Application을 실행해 주세요.")
print("모바일 앱에서 알림을 확인해주세요.")

# 60초 타임슬립 : 모바일이 로그인되고 인수 테스트 원격협업방에 진입되기까지 대기 상태
time.sleep(60)

# 모바일 협업 인원 더블 클릭하여 선택하기
participantvideo = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class = 'participant-video']/div[@class = 'participant-video__stream']")))
actions = ActionChains(driver)\
    .move_to_element(participantvideo)\
    .double_click(participantvideo)\
    .perform()
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

# 실시간 공유 탭 선택
# liveshare = driver.find_element(
#     "//nav[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][1]/button[@class = 'header-lnb__button active']")
# actions = ActionChains(driver)\
#     .click(liveshare)\
#     .perform()

# 실시간 공유 탭 화면 상태 체크 코드
if driver.find_element(
        By.XPATH, "//nav[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][1]/button[@class = 'header-lnb__button active']").is_displayed():
    print("실시간 공유 화면으로 선택되어 있습니다.")
else:
    liveshare = driver.find_element(
        By.XPATH, "//nav[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][1]/button[@class = 'header-lnb__button active']")
    actions = ActionChains(driver)\
        .move_to_element(liveshare)\
        .click(liveshare)\
        .perform()

# 실시간 화면 상태에서 포인팅 버튼 선택
pointingbtn = driver.find_element(
    By.XPATH, "//div[@class = 'stream-tools tools']/div[@class = 'tooltip']/button[@class = 'tool'][1]")
actions = ActionChains(driver)\
    .move_to_element(pointingbtn)\
    .click(pointingbtn)\
    .perform()

# 3초 동안 타임 슬립
time.sleep(3)

# 실시간 화면에서 정해 놓은 위치를 더블 클릭하여 번 반복 동작하기
# 포인팅은 현재 1번만 반복되어 있음

i = 0
while i < 1:
    
    # //div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item on'][1]
    # Default(RED) 컬러 > 1번 포인팅
    pointing_1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_1)\
        .click_and_hold(pointing_1)\
        .drag_and_drop_by_offset(pointing_1, 0, -200)\
        .click(pointing_1)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    ###############  2번째 컬러 선택 및 2번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 2번째 컬러 선택
    color_2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][1]")))
    actions = ActionChains(driver)\
        .move_to_element(color_2)\
        .click(color_2)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 클릭 2번째 포인팅
    pointing_2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_2)\
        .click_and_hold(pointing_2)\
        .drag_and_drop_by_offset(pointing_2, -50, 200)\
        .click(pointing_2)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    ###############  3번째 컬러 선택 및 3번째 포인팅
    # 색상 선택 메뉴 선택
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
        
    # 3번째 컬러 선택
    color_3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][2]")))
    actions = ActionChains(driver)\
        .move_to_element(color_3)\
        .click(color_3)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 클릭 3번째 포인팅
    pointing_3 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_3)\
        .click_and_hold(pointing_3)\
        .drag_and_drop_by_offset(pointing_3, -0, -120)\
        .click(pointing_3)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    ###############  4번째 컬러 선택 및 4번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 4번째 컬러 선택
    color_4 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][3]")))
    actions = ActionChains(driver)\
        .move_to_element(color_4)\
        .click(color_4)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 클릭 4번째 포인팅
    pointing_4 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_4)\
        .click_and_hold(pointing_4)\
        .drag_and_drop_by_offset(pointing_4, -5, -150)\
        .click(pointing_4)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    ###############  5번째 컬러 선택 및 5번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 5번째 컬러 선택
    color_5 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][4]")))
    actions = ActionChains(driver)\
        .move_to_element(color_5)\
        .click(color_5)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")))
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 암묵적 대기
    driver.implicitly_wait(time_to_wait=3)
    
    # 포인팅 클릭 5번째 포인팅
    pointing_5 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")))
    actions = ActionChains(driver)\
        .move_to_element(pointing_5)\
        .click_and_hold(pointing_5)\
        .drag_and_drop_by_offset(pointing_5, -70, -200)\
        .click(pointing_5)\
        .perform()
        
    i = i + 1

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

###### 이미지 파일 업로드 #####
# 협업 보드 탭 클릭
headerlnbbtn2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//nav[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][2]/button[@class = 'header-lnb__button']")))
headerlnbbtn2.click()
print("협업 보드 탭을 선택하였습니다.")

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)
######=============================================================================================================================

# # 협업 보드에서 파일 추가 메뉴 클릭
uploadbtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//*[@class = 'upload-list__button']")))
uploadbtn.click()

# 3초 타임 슬립
time.sleep(3)

# Windows 열기창에서 PNG 이미지 파일 추가하기
uploader = auto.WindowControl(searchDepth=2, Name='열기')
time.sleep(2)
uploader.EditControl(Name="파일 이름(N):").SendKeys('qa1.png')
uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
# uploader.ButtonControl(Name="열기(O)").Click()

# 3초 타임 슬립
time.sleep(3)
######=============================================================================================================================

# # 협업 보드에서 파일 추가 메뉴 클릭
uploadbtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//*[@class = 'upload-list__button']")))
uploadbtn.click()

# 3초 타임 슬립
time.sleep(3)

# Windows 열기창에서 BMP 이미지 파일 추가하기
uploader = auto.WindowControl(searchDepth=2, Name='열기')
time.sleep(2)
uploader.EditControl(Name="파일 이름(N):").SendKeys('qa2.bmp')
uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
# uploader.ButtonControl(Name="열기(O)").Click()

# 3초 타임 슬립
time.sleep(3)

######=============================================================================================================================

# 불러오기 버튼 선택
loading = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-box__empty']/div[@class = 'drawing-box__empty-inner']/button[@class = 'btn' and contains(text(), '불러오기')]")))
loading.click()

# 3초 타임 슬립
time.sleep(3)

# Windows 열기창에서 JPG 이미지 파일 추가하기
uploader = auto.WindowControl(searchDepth=2, Name='열기')
time.sleep(2)
uploader.EditControl(Name="파일 이름(N):").SendKeys('qa3.jpg')
uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
# uploader.ButtonControl(Name="열기(O)").Click()

# 3초 타임 슬립
time.sleep(3)

######=============================================================================================================================

# 불러오기 버튼 선택 > GIF 파일 추가
loading = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-box__empty']/div[@class = 'drawing-box__empty-inner']/button[@class = 'btn' and contains(text(), '불러오기')]")))
loading.click()

# 3초 타임 슬립
time.sleep(3)

# Windows 열기창에서 GIF 이미지 파일 추가하기
uploader = auto.WindowControl(searchDepth=2, Name='열기')
time.sleep(2)
uploader.EditControl(Name="파일 이름(N):").SendKeys('qa4.gif')
uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
# uploader.ButtonControl(Name="열기(O)").Click()

# 3초 타임 슬립
time.sleep(3)

######=============================================================================================================================

##### 이미지 파일 선택하여 화면에 공유하기 #####
# => 화면에 이미지를 공유하면서 이미지 위에 그리기 동작은 미구현 되어 있음

# 협업 보드 > qa1.png 더블 클릭 > 화면 불러오기
sharingimage1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share-body__file']/div[@class = 'vue-scrollbar__wrapper']/div[@class = 'vue-scrollbar__area vue-scrollbar-transition']/ol[@class = 'upload-list']/li[2]/button[@class = 'sharing-image__item']")))
actions = ActionChains(driver)\
    .move_to_element(sharingimage1)\
    .double_click(sharingimage1)\
    .perform()
print("qa1.png 이미지를 화면에 불러왔습니다.")

# 3초 타임 슬립
time.sleep(3)

# 파일 목록 선택
share = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share']/ul[@class = 'share-title']/li[1]/button[@class = 'share-title__button' and contains (text(), '파일목록')]")))
share.click()

# 3초 타임 슬립
time.sleep(3)

# 협업 보드 > qa2.bmp 더블 클릭 > 화면 불러오기
sharingimage2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share-body__file']/div[@class = 'vue-scrollbar__wrapper']/div[@class = 'vue-scrollbar__area vue-scrollbar-transition']/ol[@class = 'upload-list']/li[3]/button[@class = 'sharing-image__item']")))
actions = ActionChains(driver)\
    .move_to_element(sharingimage2)\
    .double_click(sharingimage2)\
    .perform()
print("qa2.bmp 이미지를 화면에 불러왔습니다.")

# 3초 타임 슬립
time.sleep(3)

# 파일 목록 선택
share = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share']/ul[@class = 'share-title']/li[1]/button[@class = 'share-title__button' and contains (text(), '파일목록')]")))
share.click()

# 3초 타임 슬립
time.sleep(3)

# 협업 보드 > qa3.jpg 더블 클릭 > 화면 불러오기
sharingimage3 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share-body__file']/div[@class = 'vue-scrollbar__wrapper']/div[@class = 'vue-scrollbar__area vue-scrollbar-transition']/ol[@class = 'upload-list']/li[4]/button[@class = 'sharing-image__item']")))
actions = ActionChains(driver)\
    .move_to_element(sharingimage3)\
    .double_click(sharingimage3)\
    .perform()
print("qa3.jpg 이미지를 화면에 불러왔습니다.")

# 3초 타임 슬립
time.sleep(3)

# 파일 목록 선택
share = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share']/ul[@class = 'share-title']/li[1]/button[@class = 'share-title__button' and contains (text(), '파일목록')]")))
share.click()

# 3초 타임 슬립
time.sleep(3)

# 협업 보드 > qa4.gif 더블 클릭 > 화면 불러오기
sharingimage4 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share-body__file']/div[@class = 'vue-scrollbar__wrapper']/div[@class = 'vue-scrollbar__area vue-scrollbar-transition']/ol[@class = 'upload-list']/li[5]/button[@class = 'sharing-image__item']")))
actions = ActionChains(driver)\
    .move_to_element(sharingimage4)\
    .double_click(sharingimage4)\
    .perform()
print("qa4.gif 이미지를 화면에 불러왔습니다.")

# 3초 타임 슬립
time.sleep(3)

# 파일 목록 선택
share = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'share']/ul[@class = 'share-title']/li[1]/button[@class = 'share-title__button' and contains (text(), '파일목록')]")))
share.click()

# 3초 타임 슬립
time.sleep(3)

### 협업보드 > 캔버스에 선 긋기 동작
# 선 두께 메뉴 선택 
linethickness1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")))
linethickness1.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 선 두께 선택 > 10px로 변경
linethickness2 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'picker--container']/div[@class = 'picker line_width']/ul[@class = 'picker--list']/li[@class = 'picker--item'][4]")))
linethickness2.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 선 두께 선택하여 메뉴 닫기
linethickness3 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")))
linethickness3.click()

######***************************************************************************************************

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 협업 보드 화면에서 선 긋기 동작 : 마우스 클릭하여 홀드 상태 > 원하는 위치로 마우스 이동
# 캔버스에 선 긋기 동작 확인 : 현재 web에서는 점으로만 보임
pointer_area = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")))
actions = ActionChains(driver)\
    .click_and_hold(pointer_area)\
    .drag_and_drop_by_offset(pointer_area, 0, 50)\
    .drag_and_drop_by_offset(pointer_area, -100, 100).double_click()\
    .perform()
    
# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)