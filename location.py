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
options.add_argument("--use-fake-ui-for-media-stream") # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized') # 브라우저가 최대화된 상태로 실행

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
    print("실시간 공유 탭을 선택하였습니다.")

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

# 3초 타임 슬립
time.sleep(3)

# 선 긋기 지우기
pointdele = driver.find_element(
    By.XPATH, "//*[@class = 'main-body drawing']/div[@class = 'drawing-tools tools']/div[@class = 'tooltip'][3]/button[@class = 'tool']")
for i in range(4):
    pointdele.click()
    time.sleep(3)

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 텍스트 크기 선택
textsizebtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-tools tools']/div[4]/div[@class = 'tooltip']/button[@class = 'tool']")))
textsizebtn.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 텍스트 크기를 최대 사이즈인 18로 선택
textwritemode = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'picker--container']/div[@class = 'picker text_size']/ul[@class ='picker--list']/li[@class = 'picker--item'][4]")))
textwritemode.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 텍스트 크기 선택하여 텍스트 크기 메뉴 닫기
textsizebtn = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-tools tools']/div[4]/div[@class = 'tooltip']/button[@class = 'tool active']")))
textsizebtn.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 텍스트 모드 메뉴 선택
textmode = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-tools tools']/div[3]")))
textmode.click()

# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)

# 협업보드 > 캔버스 > 캔버스 중앙에 텍스트 입력하기
pointer_area = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")))
actions = ActionChains(driver)\
    .move_to_element(pointer_area)\
    .double_click(pointer_area)\
    .send_keys_to_element(pointer_area, '인수 테스트 중입니다.')\
    .perform()
    
# 3초 암묵적 대기
driver.implicitly_wait(time_to_wait=3)


# Using a Pen 동작 : 캔버스에 선 긋기 동작 확인
# pointer_area = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# actions = ActionChains(driver)
# actions = ActionBuilder(
#     driver, mouse=PointerInput(interaction.POINTER_PEN, "default pen"))
# # actions.pointer_action
# actions.pointer_action.click_and_hold(pointer_area)
# actions.pointer_action.move_to(pointer_area)
# actions.pointer_action.pointer_down()
# actions.pointer_action.move_by(0, 50)
# actions.pointer_action.pointer_up()
# actions.perform()

# 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

##### ============================================================================================================#####
# 드래그 앤 드롭 동작
# drawingCanvas = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# action = ActionChains(driver)
# action.click_and_hold(drawingCanvas)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 0, 50)
# action.perform()

# drawingCanvas = driver.find_element(
#     By.XPATH, "//div[@class = 'canvas-container']/canvas[@id = 'drawingCanvas' and @class = 'lower-canvas']")
# action = ActionChains(driver)\
#     .click_and_hold(drawingCanvas)\
#     .drag_and_drop_by_offset(drawingCanvas, 0, 300)\
#     .context_click(drawingCanvas)\
#     .perform()
#     .send_keys(Keys.ESCAPE)

# 마우스 포인트 고정
# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)\
#     .click_and_hold(uppercanvas)\
#     .move_to_element_with_offset(uppercanvas, 0, 50).double_click()\
#     .perform()

# 드래그 앤 드롭 동작 및 더블 클릭 동작
# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)\
#     .click_and_hold(uppercanvas)\
#     .drag_and_drop_by_offset(uppercanvas, -100, -50).double_click()\
#     .drag_and_drop_by_offset(uppercanvas, -50, 0).double_click()\
#     .drag_and_drop_by_offset(uppercanvas, 0, 50).double_click()\
#     .drag_and_drop_by_offset(uppercanvas, 50, 100).double_click()\
#     .perform()

# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)\
#     .click_and_hold(uppercanvas)\
#     .drag_and_drop_by_offset(uppercanvas, -100, -50).double_click()\

# drawingCanvas = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# action = ActionChains(driver)
# action.click_and_hold(drawingCanvas)
# action.move_to_element_with_offset(drawingCanvas, 0, 50)
# action.click(drawingCanvas)

# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 50, -50)
# action.perform()

# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, -50, -10)
# action.perform()

# time.sleep(3)

# action.drag_and_drop_by_offset(drawingCanvas, -10, 0)
# action.perform()

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 현재 페이지 스크린샷
# screenshot_name = "my_screenshot_name.png"
# driver.save_screenshot(screenshot_name)

# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)
# action.click_and_hold(uppercanvas)
# time.sleep(3)
# action.drag_and_drop_by_offset(uppercanvas, 0, 50)
# time.sleep(3)
# action.drag_and_drop_by_offset(uppercanvas, 50, 90)
# time.sleep(3)
# action.drag_and_drop_by_offset(uppercanvas, 90, 0)
# time.sleep(3)
# action.perform()

# drawingCanvas = driver.find_element(
#     By.XPATH, "//div[@class = 'canvas-container']/canvas[@id = 'drawingCanvas' and @class = 'lower-canvas']")
# action = ActionChains(driver)
# action.click_and_hold(drawingCanvas)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 0, 50)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 50, 90)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 90, 0)
# time.sleep(3)
# action.perform()

# drawingCanvas = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# action = ActionChains(driver)
# action.click_and_hold(drawingCanvas)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 0, 50)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 50, 90)
# time.sleep(3)
# action.drag_and_drop_by_offset(drawingCanvas, 90, 0)
# time.sleep(3)
# action.perform()

# Using a Pen 동작
# pointer_area = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# actions = ActionChains(driver)
# actions = ActionBuilder(
#     driver, mouse=PointerInput(interaction.POINTER_PEN, "default pen"))
# # actions.pointer_action
# actions.pointer_action.click_and_hold(pointer_area)
# actions.pointer_action.move_to(pointer_area)
# actions.pointer_action.pointer_down()
# actions.pointer_action.move_by(0, 50)
# actions.pointer_action.pointer_up()
# actions.perform()

# Using a Pen 동작
# pointer_area = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# actions = ActionBuilder(
#     driver, mouse=PointerInput(interaction.POINTER_PEN, "default pen"))
# actions.pointer_actions\
#     .pointer_action.click_and_hold(pointer_area)\
#     .pointer_action.move_to(pointer_area)\
#     .pointer_action.pointer_down()\
#     .pointer_action.move_by(0, 50)\
#     .pointer_action.pointer_up()\
#     .perform()

# pointer_area = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# actions = ActionBuilder(driver)
# actions.pointer_action.click_and_hold(pointer_area)
# actions.pointer_action.move_to(pointer_area)
# actions.pointer_action.pointer_down(MouseButton.LEFT)
# actions.pointer_action.move_by(0, 100)

# actions.pointer_action.click_and_hold(pointer_area)
# actions.pointer_action.move_to(pointer_area)
# actions.pointer_action.pointer_down(MouseButton.LEFT)
# actions.pointer_action.move_by(100, -80)
# actions.perform()

# pointer_area = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-box']/div[@class = 'drawing-canvas']/div[@class = 'pinch-zoom-container']/div[@class = 'pinchzoom-layer']")
# actions = ActionChains(driver)
# actions.click_and_hold(pointer_area)
# actions.drag_and_drop_by_offset(pointer_area, -100, 100).double_click()
# actions.perform()


#-------------------------------------
# 위와 중복되는 코드

# 협업 보드 화면에서 선 긋기 동작 : 마우스 클릭하여 홀드 상태 > 원하는 위치로 마우스 이동
# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)\
#     .click_and_hold(uppercanvas)\
#     .move_to_element_with_offset(uppercanvas, 0, 50)
# action.click_and_hold(uppercanvas)

# uppercanvas = driver.find_element(
#     By.XPATH, "//div[@class= 'drawing-box']/div[1]/div[1]/div[1]/div[2]/canvas[@class = 'upper-canvas ']")
# action = ActionChains(driver)\
#     .drag_and_drop_by_offset(uppercanvas, 0, 50)\
#     .perform()

# 5초 타임 슬립
time.sleep(5)

# 색상 선택 메뉴 클릭
# colormenu = driver.find_element(
#     By.XPATH, "//div[@class = 'drawing-tools tools']/div[5]/div[@class = 'tooltip']/button[@class = 'tool']")
# colormenu.click()

# 3초 타임 슬립
# time.sleep(3)

# 색상 선택 메뉴 클릭 > 투명도 조절 100 % > 80% > 60%
# 투명도 조절을 ActionChanins로는 컨트롤 하기 어려워서 클릭 액션으로 처리하는게 현재로써는 제일 좋음
# colorrange = driver.find_element(
#     By.XPATH, "//div[@class = 'picker--container']/div[@class = 'picker']/div[@class = 'picker--range']/div[@class = 'picker--range__box']/input[@type = 'range']")
# colorrange.click()
# colorrange.click()

# AR 기능 탭 클릭
# headerlnbbtn2 = driver.find_element(
#     By.XPATH, "//nav[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][3]/button[@class = 'header-lnb__button']")
# headerlnbbtn2.click()
# print("AR 기능 탭을 선택하였습니다.")

########### 여기까지 구현 ##########################

# # 원격 협업 화면에서 설정 메뉴 선택
# tooltipmenu = driver.find_element(
#     By.XPATH, "//*[@class = 'menus-box']/div[@class = 'tooltip tooltip-menu'][4]/button[@class = 'menu']")
# tooltipmenu.click()

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 환경 설정 모달창 출력 여부 확인
# if driver.find_element(
#         By.XPATH, "//*[@class = 'modal service-setting-modal']").is_displayed():
#     print("환경 설정 모달창이 출력되었습니다.")
# else:
#     print("환경 설정 모달창이 출력되지 않았습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 환경 설정 메뉴에서 번역 설정 탭 선택
# Translationset = driver.find_element(
#     By.XPATH, "//*[@class = 'service-setting']/section[@class = 'service-setting-nav']/button[@data-text = '번역 설정' and @class = 'service-setting-nav__menu']")
# Translationset.click()

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 설정 > 번역 사용 허용 체크 상태 확인
# Translationuse = driver.find_element(
#     By.XPATH, "//section[@class = 'service-setting__view']/div[@class = 'service-setting__row'][1]/div[@class = 'check']/span[@class = 'check-toggle' and contains (text(), 'OFF')]").is_selected()
# print("번역 사용 허용이 체크 되어 있지 않습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 현재 번역 언어 설정 상태(Default는 한국어)
# languagestate = driver.find_element(
#     By.XPATH, "//*[@class = 'select-label disabled']").text
# print(languagestate)
# print("번역 언어 설정은 현재 한국어로 설정되어 있습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 설정 > 번역 사용 허용 체크
# Translationcheck = driver.find_element(
#     By.XPATH, "//section[@class = 'service-setting__view']/div[@class = 'service-setting__row'][1]/div[@class = 'check']/span[@class = 'check-toggle' and contains (text(), 'OFF')]").click()
# print("번역 사용 허용이 체크 되었습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 설정 > 음성 변환 사용 허용 체크 상태 확인
# voiceconversionuse = driver.find_element(
#     By.XPATH, "//section[@class = 'service-setting__view']/div[@class = 'service-setting__row'][5]/div[@class = 'check']/span[@class = 'check-toggle' and contains (text(), 'OFF')]").is_selected()
# print("음성 변환 사용 허용이 체크 되어 있지 않습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 설정 > 번역 사용 허용 체크
# Translationcheck = driver.find_element(
#     By.XPATH, "//section[@class = 'service-setting__view']/div[@class = 'service-setting__row'][5]/div[@class = 'check']/span[@class = 'check-toggle' and contains (text(), 'OFF')]").click()
# print("음성 변환 사용 허용이 체크 되었습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 언어 설정 Selectbox 선택
# languagesetbox = driver.find_element(
#     By.XPATH, "//div[@class = 'service-setting__row'][2]/span[@class = 'popover--wrapper service-setting__selector']/button[@class = 'select-label']")
# languagesetbox.click()
# print("번역 언어 설정 SELECTBOX를 클릭하였습니다.")

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 번역 언어 설정 선택 > 한국어
# languageselect = driver.find_element(
#     By.XPATH, "//div[@class = 'modal service-setting-modal']/div[@class = 'popover select-options']/div[@class = 'popover--body']/div[@class = 'select-optionbox']/button[1]")
# languageselect.click()
# print("번역 언어를 한국어로 선택했습니다.")

# # # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# 번역/원본 출력방식 : 동식 출력

# 음성 인식 방식(STT) : 음성 녹음


# 환경 설정 모달창 닫기
# modalclose = driver.find_element(
#     By.XPATH, "//*[@class = 'modal--header']/button[@class = 'modal--close']")
# modalclose.click()

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# ########### 채팅창에서 채팅하기 ###########
# # 채팅 입력 필드에 채팅 내용 입력하기
# chattextareainput = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/textarea[@class = 'chat-input__form-write']")
# chattextareainput.send_keys('지금부터 인수 테스트 원격협업을 진행 하겠습니다.')

# # 3초 타임 슬립
# time.sleep(3)

# # 보내기 버튼 선택
# textareainputbtn = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/button[@class = 'chat-input__form-button']")
# textareainputbtn.click()

# # 3초 타임 슬립
# time.sleep(3)

# # 채팅 입력 필드에 채팅 내용 입력하기
# chattextareainput = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/textarea[@class = 'chat-input__form-write']")
# chattextareainput.send_keys('리모트 테스트')

# # 3초 타임 슬립
# time.sleep(3)

# # 보내기 버튼 선택
# textareainputbtn = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/button[@class = 'chat-input__form-button']")
# textareainputbtn.click()

# # 3초 타임 슬립
# time.sleep(3)

# # 채팅 입력 필드에 채팅 내용 입력하기
# chattextareainput = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/textarea[@class = 'chat-input__form-write']")
# chattextareainput.send_keys('리모트 테스트입니다.')

# # 3초 타임 슬립
# time.sleep(3)

# # 보내기 버튼 선택
# textareainputbtn = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/button[@class = 'chat-input__form-button']")
# textareainputbtn.click()

# # 3초 타임 슬립
# time.sleep(3)

# # 채팅 입력 필드에 채팅 내용 입력하기
# chattextareainput = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/textarea[@class = 'chat-input__form-write']")
# chattextareainput.send_keys('리모트 테스트가 잘되는 것 같습니다.')

# # 3초 타임 슬립
# time.sleep(3)
#
# 보내기 버튼 선택
# textareainputbtn = driver.find_element(
#     By.XPATH, "//div[@class = 'chat-body']/div[@class = 'chat-list']/div[2]/div[@class = 'chat-input']/div[@class ='chat-input__form']/button[@class = 'chat-input__form-button']")
# textareainputbtn.click()

# 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# # 음성 변환 설정(TTS) 체크

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

#

# # 3초 암묵적 대기
# driver.implicitly_wait(time_to_wait=3)

# 채팅창 TTS(Text to speech) 번역 언어 설정

# 협업 보드 탭 클릭
# headerlnbbtn2 = driver.find_element(
#     By.XPATH, "//*[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][2]/button[@class = 'header-lnb__button']")
# headerlnbbtn2.click()
# print("협업 보드 탭을 선택하였습니다.")

# # 협업 보드에서 파일 추가 메뉴 클릭
# uploadbtn = driver.find_element(
#     By.XPATH, "//*[@class = 'upload-list__button']")
# uploadbtn.click()

# # 5초 대기
# # time.sleep(5)

# # # #-*-coding:utf-8-*-
# # # 애플리케이션 모듈 선언
# app = pywinauto.application.Application()
# app.connect(title_re='열기', class_name='#32770')
# window = app['열기']
# window.set_focus()

# # # 아래 코드는 윈도우 애플리케이션의 상위/하위 정보를 모두 볼 수 있는 코드
# app.YourDialog.print_control_identifiers()

# # 3초 대기
# time.sleep(3)

# # # PNG 파일 추가하기
# # # 파일 이름(N)에 검색할 이미지 이름 입력
# window['파일 이름(&N):Edit'].type_keys('qa1.png')

# # 3초 대기
# time.sleep(3)

# # 이미지 이름 입력 후, 열기 버튼 클릭
# window['열기(&O)Button'].click()

#취소 버튼 클릭
# window.Button2.click()  # 버튼 클릭 이벤트 보내기

# # 협업 보드 > qa1.png 더블 클릭하여 화면 불러오기
# sharingimage1 = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@class = 'sharing-image']/button[@class = 'sharing-image__item'][1]")))
# action = ActionChains(driver)
# action.double_click(sharingimage1).perform()
# print("qa1.png 이미지를 화면에 불러왔습니다.")

# 위와 중복되는 코드
#-------------------------------------

