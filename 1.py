import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# USB: usb_device_handle_win.cc:1048 Failed to read descriptor
# from node connection:시스템에 부착된 장치가 작동하지 않습니다.(0x1F)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")

CHROME_DRIVER_PATH = (
    "C:\python_selenium_auto_vir\chromedriver.exe")  # 크롬드라이버 경로경로
driver = webdriver.Chrome(
    executable_path=CHROME_DRIVER_PATH, chrome_options=options)

# 사용할 webdriver 지정: Chrome 사용
# driver = webdriver.Chrome(options=options)

# 진입할 경로 지정
virnectproductpage = "https://stgwww.virnect.com/"
driver.get(virnectproductpage)

# 웹페이지에서 특정 요소가 준비될 때까지 암묵적으로 대기한다.
# 3초 대기
time.sleep(3)

# 웹페이지 해상도 조절
# driver.set_window_size(1690, 1060)
# windows을 최대 사이즈로 조절
driver.maximize_window()

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

# 3초 대기
time.sleep(3)

# 패스워드 입력창 위치 찾기 및 패스워드 입력
userpw = driver.find_element(
    By.XPATH, "//div[@class = 'password-input el-input el-input--suffix']/input[1]").send_keys('@rokmc875th')

# 3초 대기
time.sleep(3)

# 로그인 클릭
loginbtnclick = driver.find_element(
    By.XPATH, "//*[@class = 'el-button next-btn block-btn el-button--info']")
loginbtnclick.click()

# 3초 대기
time.sleep(3)

# 썸네일 버튼을 클릭
thumbnailbutn = driver.find_element(
    By.XPATH, "//*[@class = 'link-btn status-btn']")
thumbnailbutn.click()

# 3초 대기
time.sleep(3)

# # Remote 메뉴 클릭
Remotemenu = driver.find_element(
    By.XPATH, "//a[@href ='https://stgremote.virnect.com']")
Remotemenu.click()

# 5초 대기
time.sleep(5)

# 현재 활성화 된 탭
print(driver.window_handles)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
time.sleep(5)

# 쿠키 및 이용통계 수집 동의 모달
cookiebtn = driver.find_element(
    By.XPATH, "//*[@class = 'cookie-policy-wrapper__submit-button']")
cookiebtn.click()

# 5초 대기
time.sleep(5)

# 원격 협업 생성 버튼 클릭
remotecreatebtn = driver.find_element(
    By.XPATH, "//*[contains(text(), '원격 협업 생성')]")
remotecreatebtn.click()

# 5초 대기
time.sleep(5)

# 협업 그룹 이름 입력하기
# 협업 이름은 _인수테스트
Cooperationname = driver.find_element(
    By.XPATH, "//*[@class = 'modal--body']/div[@class ='createroom']/section[@class ='createroom-info']/figure[@class ='inputrow'][1]/input[@class = 'inputrow-input input']")
Cooperationname.send_keys('_인수테스트')

# 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기
# stgim875@gmail.com [1]
# stgim1516@gmail.com[1]
# stgim1314@gmail.com[2]
# stgim1112@gmail.com[3]
# stgim789@gmail.com[4]
# stgim456@gmail.com[5]
# stgim123@gmail.com[6]
createroommanageradd = driver.find_element(
    By.XPATH, "//*[@class = 'collapsible__content opend']/div[@class = 'widecard choice'][1]")
createroommanageradd.click()

# 5초 대기
time.sleep(5)

# 원격 협업 생성하기 시작하기 버튼 클릭
createroomstrbtn = driver.find_element(
    By.XPATH, "//*[@class = 'btn large createroom-info__button']")
createroomstrbtn.click()

# 10초 대기
time.sleep(10)

# permission 동의 팝업창 확인 선택하기
# 카메라 및 마이크 => options.add_argument("--use-fake-ui-for-media-stream")으로 fake 처리함

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 웹에서 원격 협업 요청 후, 수동으로 직접 Remote Mobile에서 로그인하고 원격 협업을 선택 할 수 있는 물리적인 시간이 필요함
# 30초 대기
time.sleep(30)

# 협업 인원 더블 클릭하여 선택하기
participantvideo = driver.find_element(
    By.XPATH, "//*[@class = 'participant-video']/div[@class = 'participant-video__stream']")
action = ActionChains(driver)
action.double_click(participantvideo).perform()

# 5초 대기
time.sleep(5)

# 전체 공유 버튼 클릭
selectviewbutton = driver.find_element(
    By.XPATH, "//*[contains(text(), '전체 공유')]")
selectviewbutton.click()

# 5초 대기
time.sleep(5)

# 협업 보드 탭 클릭
headerlnbbtn2 = driver.find_element(
    By.XPATH, "//*[@class = 'header-lnbs service']/ul[@class = 'flex']/li[@class = 'header-lnb'][2]/button[@class = 'header-lnb__button']")
headerlnbbtn2.click()

# 5초 대기
time.sleep(5)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
time.sleep(5)

# 협업 보드에서 파일 업로드 메뉴 클릭 
uploadbtn = driver.find_element(
    By.XPATH, "//*[@class = 'upload-list__button']")
uploadbtn.click()

# 5초 대기
time.sleep(3)

# 현재 사용하는 모니터의 해상도 출력
print(pyautogui.size())

# 협업보드 > windows file open 다이얼로그에서 파일 열기
# abc.png 이미지 선택 및 클릭
# abc.png 클릭하기
pyautogui.click(x=1135, y=577,clicks=1, interval=0.1)
# 5초 대기
time.sleep(3)
# 윈도우 탐색기 열기 버튼 선택 및 클릭
pyautogui.click(x=1180, y=760, clicks=1, interval=0.1)
# 5초 대기
time.sleep(3)

# 협업 보드 > abc.png 더블 클릭하여 화면 불러오기
sharingimage1 = driver.find_element(
    By.XPATH, "//*[@class = 'sharing-image']/button[@class = 'sharing-image__item'][1]")
action = ActionChains(driver)
action.double_click(sharingimage1).perform()

# 5초 대기
time.sleep(5)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
time.sleep(5)

# 협업보드 > 공유 화면에서 그리기 모드(점찍기)
# 첫번째 점찍기
pyautogui.click(x=1036, y=783, clicks=1, interval=0.1)
# 3초 대기
time.sleep(3)
# 두번째 점찍기
pyautogui.click(x=1182, y=765, clicks=1, interval=0.1)
# 3초 대기
time.sleep(3)
# 세번째 점찍기
pyautogui.click(x=1311, y=762, clicks=1, interval=0.1)
# 3초 대기
time.sleep(3)

# 점찍기 되돌기 버튼 3번 클릭하기
# 첫번째 클릭
sharingimage1 = driver.find_element(
    By.XPATH, "//*[@class = 'main-body drawing']/div[@class = 'drawing-tools tools']/div[@class = 'tooltip'][3]/button[@class = 'tool']")
sharingimage1.click()
# 3초 대기
time.sleep(3)
# 두번째 클릭
sharingimage2 = driver.find_element(
    By.XPATH, "//*[@class = 'main-body drawing']/div[@class = 'drawing-tools tools']/div[@class = 'tooltip'][3]/button[@class = 'tool']")
sharingimage2.click()
# 3초 대기
time.sleep(3)
sharingimage3 = driver.find_element(
    By.XPATH, "//*[@class = 'main-body drawing']/div[@class = 'drawing-tools tools']/div[@class = 'tooltip'][3]/button[@class = 'tool']")
sharingimage3.click()
# 3초 대기
time.sleep(5)

# PNG 파일 추가하기
# uploadfileadd = driver.find_element(
#     By.XPATH, "//input[@type='file' and @accept='image/gif,image/bmp,image/jpeg,image/png,application/pdf']").send_keys("C:/Users/VIRNECT/abc.png")
# uploadfileadd = driver.find_element(
#     By.ID, "//input[@type='file' and @accept='image/gif,image/bmp,image/jpeg,image/png,application/pdf']").send_keys("C:/Users/VIRNECT/abc.png")

# 추가 초대하기 버튼 클릭
# addbutton = driver.find_element(
#     By.XPATH, "//*[@class = 'participant-video append more']").click()

# 5초 대기
# time.sleep(5)

# 녹화 버튼 클릭하기
# buttonmenu_1 = driver.find_element(
#     By.XPATH, "//*[@class='menus-box']/div[@class='tooltip tooltip-menu'][2]/button[@class='menu']").click()

# 3초 대기
# time.sleep(3)

# 녹화 버튼 다시 클릭하기
# buttonmenu_2 = driver.find_element(
#     By.XPATH, "//*[@class='menus-box']/div[@class='tooltip tooltip-menu'][2]/button[@class='menu active']").click()

# 5초 대기
# time.sleep(5)

# 나가기 버튼 클릭
# exit_ = driver.find_element(
#     By.XPATH, "//*[@class = 'header-tools__leave']").click()

# 5초 대기
# time.sleep(5)

# 최근 열린 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
# time.sleep(5)

# 오픈 룸 생성 버튼 클릭
# openroomcreatebtn = driver.find_element(
#     By.XPATH, "//*[@class = 'btn workspace-welcome__open']").click()

# 로그아웃 시 매우 중요함
# status 메뉴 선택
# informatiobtn = driver.find_element(
#     By.XPATH, "//*[@class ='status-btn thumbnail-btn']").click()
