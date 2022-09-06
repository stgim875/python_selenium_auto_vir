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
import HTMLTestRunner
import unittest

# USB: usb_device_handle_win.cc:1048 Failed to read descriptor
# from node connection:시스템에 부착된 장치가 작동하지 않습니다.(0x1F)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

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

# 3초 대기
time.sleep(3)

# WebRTC_Internal 페이지로 이동
driver.get('chrome://webrtc-internals/')

# 3초 대기
time.sleep(3)

# WebRTC_Internal 페이지에서 Read stats From 선택
formselect = driver.find_element(
    By.XPATH, "//*[@id = 'statsSelectElement']")
formselect.click()

# 3초 대기
time.sleep(3)

# WebRTC_Internal 페이지에서 Read stats From을 Legacy Non-Standard (callback-based) getStats() API로 선택
api_2 = driver.find_element(
    By.XPATH, "//*[@id = 'statsSelectElement']/option[2]")
api_2.click()

# 3초 대기
time.sleep(3)

# 새창 열기 > 새창에 주소를 입력하여 이동하는 코드
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://stgwww.virnect.com')

# 웹페이지에서 특정 요소가 준비될 때까지 암묵적으로 대기한다.
# 3초 대기
time.sleep(3)

# Log in 버튼을 클릭하여 로그인센터로 이동한다.
logincenter = driver.find_element(By.XPATH, "//*[@class ='login-btn']")
logincenter.click()

# 3초 대기
time.sleep(3)

# 아이디 입력창 위치 찾기 및 아이디 입력
userid = driver.find_element(
    By.XPATH, "//div[@class ='email-input el-input el-input--suffix']/input[1]").send_keys('maxgim875@gmail.com')
# # 이메일 계정 정보
# # stgim875@gmail.com
# # stgim1516@gmail.com
# # stgim1314@gmail.com
# # stgim1112@gmail.com
# # stgim789@gmail.com
# # stgim456@gmail.com
# # stgim123@gmail.com

# # 3초 대기
time.sleep(3)

# 패스워드 입력창 위치 찾기 및 패스워드 입력
userpw = driver.find_element(
    By.XPATH, "//div[@class = 'password-input el-input el-input--suffix']/input[1]").send_keys('@rokmc875th')

# 3초 대기
time.sleep(3)

# 로그인 클릭
loginbtn = driver.find_element(
    By.XPATH, "//*[@class = 'el-button next-btn block-btn el-button--info']")
loginbtn.click()

# 3초 대기
time.sleep(3)

# 썸네일 버튼을 클릭
thumbnailbtn = driver.find_element(
    By.XPATH, "//*[@class = 'link-btn status-btn']")
thumbnailbtn.click()

# 3초 대기
time.sleep(3)

# Remote 메뉴 클릭
Remotemenu = driver.find_element(
    By.XPATH, "//a[@href ='https://stgremote.virnect.com']")
Remotemenu.click()

# 3초 대기
time.sleep(3)

# 현재 활성화 된 탭
print(driver.window_handles)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 3초 대기
time.sleep(3)

# 쿠키 및 이용통계 수집 동의 모달
cookiebtn = driver.find_element(
    By.XPATH, "//*[@class = 'cookie-policy-wrapper__submit-button']")
cookiebtn.click()

# 3초 대기
time.sleep(3)

# 원격 협업 생성 버튼 클릭
remotecreatebtn = driver.find_element(
    By.XPATH, "//*[contains(text(), '원격 협업 생성')]")
remotecreatebtn.click()

# 3초 대기
time.sleep(3)

# 원격 협업 생성하기 모달창 정상 출력 확인
if driver.find_element(By.XPATH, "//*[@class = 'modal--body']").is_displayed():
    print("원격 협업 생성하기 모달창이 정상적으로 출력되었습니다.")
else:
    print("원격 협업 생성하기 모달창이 출력되지 않았습니다.")

# 3초 대기
time.sleep(3)

# [예외 처리 코드: 멤버 리스트가 닫혀 있을 경우 select 버튼 클릭] 
if driver.find_element(By.XPATH, "//*[@class = 'collapsible member-collapsible opend decorated']").is_displayed():
    print("원격 협업 멤버 리스트가 정상적으로 출력됩니다.")
else:
    selectbtn = driver.find_element(
        By.XPATH, "//*[@class = 'collapsible__button decorated']")
    selectbtn.click()

# 3초 대기
time.sleep(3)

# Default 원격 협업 이름 지우기
placeholder = driver.find_element(
    By.XPATH, "//*[@class = 'modal--body']/div[@class ='createroom']/section[@class ='createroom-info']/figure[@class ='inputrow'][1]/input[@class = 'inputrow-input input']")
placeholder.clear()

# 3초 대기
time.sleep(3)

# 협업 그룹 이름 입력하기
# 협업 이름은 _인수테스트
Cooperationname = driver.find_element(
    By.XPATH, "//*[@class = 'modal--body']/div[@class ='createroom']/section[@class ='createroom-info']/figure[@class ='inputrow'][1]/input[@class = 'inputrow-input input']")
Cooperationname.send_keys('인수 테스트')

# 3초 대기
time.sleep(3)

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

# 3초 대기
time.sleep(3)

# 원격 협업 생성하기 시작하기 버튼 클릭
createroombtn = driver.find_element(
    By.XPATH, "//*[@class = 'btn large createroom-info__button']")
createroombtn.click()

# 5초 대기
time.sleep(5)

# permission 동의 팝업창 확인 선택하기
# 카메라 및 마이크 => options.add_argument("--use-fake-ui-for-media-stream")으로 fake 처리함

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 웹에서 원격 협업 요청 후, 수동으로 직접 Remote Mobile에서 로그인하고 원격 협업을 선택 할 수 있는 물리적인 시간이 필요함
# 70초 대기
time.sleep(70)
print("Mobile Remote Application을 실행해 주세요.")
