i = 0
while i < 3:
    
    # //div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item on'][1]
    # Default(RED) 컬러 > 1번 포인팅
    pointing_1 = driver.find_element(
        By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")
    actions = ActionChains(driver)\
        .move_to_element(pointing_1)\
        .click_and_hold(pointing_1)\
        .drag_and_drop_by_offset(pointing_1, 0, -200)\
        .click(pointing_1)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    ###############  2번째 컬러 선택 및 2번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
    
    # 3초 타임 슬립
    time.sleep(3)
    
    # 2번째 컬러 선택
    color_2 = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][1]")
    actions = ActionChains(driver)\
        .move_to_element(color_2)\
        .click(color_2)\
        .perform()

    # 3초 타임 슬립
    time.sleep(3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 포인팅 클릭 2번째 포인팅
    pointing_2 = driver.find_element(
        By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")
    actions = ActionChains(driver)\
        .move_to_element(pointing_2)\
        .click_and_hold(pointing_2)\
        .drag_and_drop_by_offset(pointing_2, -50, 200)\
        .click(pointing_2)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)


###############  3번째 컬러 선택 및 3번째 포인팅

    # 색상 선택 메뉴 선택
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 3번째 컬러 선택
    color_3 = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][2]")
    actions = ActionChains(driver)\
        .move_to_element(color_3)\
        .click(color_3)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 포인팅 클릭 3번째 포인팅
    pointing_3 = driver.find_element(
        By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")
    actions = ActionChains(driver)\
        .move_to_element(pointing_3)\
        .click_and_hold(pointing_3)\
        .drag_and_drop_by_offset(pointing_3, -0, -120)\
        .click(pointing_3)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    
    ###############  4번째 컬러 선택 및 4번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 4번째 컬러 선택
    color_4 = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][3]")
    actions = ActionChains(driver)\
        .move_to_element(color_4)\
        .click(color_4)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)

    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 포인팅 클릭 4번째 포인팅
    pointing_4 = driver.find_element(
        By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")
    actions = ActionChains(driver)\
        .move_to_element(pointing_4)\
        .click_and_hold(pointing_4)\
        .drag_and_drop_by_offset(pointing_4, -5, -150)\
        .click(pointing_4)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    
    ###############  5번째 컬러 선택 및 5번째 포인팅
    
    # 색상 선택 메뉴 선택
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 5번째 컬러 선택
    color_5 = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'picker--container']/div[@class = 'picker line_color']/ul[@class = 'picker--list']/li[@class = 'picker--item'][4]")
    actions = ActionChains(driver)\
        .move_to_element(color_5)\
        .click(color_5)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 색상 선택 메뉴 선택 > 색상 컨테이너 닫기
    colorbtn = driver.find_element(
        By.XPATH, "//div[@class = 'stream-tools tools']/div[2]/div[@class = 'tooltip']/button[@class = 'tool active']")
    actions = ActionChains(driver)\
        .move_to_element(colorbtn)\
        .click(colorbtn)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
    
    # 포인팅 클릭 5번째 포인팅
    pointing_5 = driver.find_element(
        By.XPATH, "//div[@class= 'main-video']/div[@class = 'main-video__box']/div[@class = 'main-video__pointing']")
    actions = ActionChains(driver)\
        .move_to_element(pointing_5)\
        .click_and_hold(pointing_5)\
        .drag_and_drop_by_offset(pointing_5, -70, -200)\
        .click(pointing_5)\
        .perform()
        
    # 3초 타임 슬립
    time.sleep(3)
