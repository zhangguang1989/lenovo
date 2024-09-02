from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import threading

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

phone = '13880944717'
password = 'ysqkdlxylcmqL2'
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/126.0.0.0'


def checkAndOrder(driver, url):
    try:
        driver.get(url)
        buyBtn = driver.find_element(By.ID, 'detail-product-buyGroup-ljgm')
        if buyBtn.text == '立即购买':
            log(url + ' 发现库存')
            buyBtn.click()
            time.sleep(0.1)
            confirmBuyBtn = driver.find_element(By.ID, 'detail-product-goodsContent-buyBtn')
            confirmBuyBtn.click()
            # accountInput = driver.find_element(By.XPATH, '//input[@class="virtual-goods-account-form-input"]')
            # accountInput.send_keys(phone)
            submitBtn = driver.find_element(By.XPATH, '//div[@class="submit_order"]')
            submitBtn.click()
            driver.find_element(By.XPATH, '//div[text()="收银台"]')
            log(url + ' 已抢到')
            return True
        else:
            log(url + ' 没库存')
            return False
    except Exception as e:
        log('未知错误 %s' % e)
        return False


def login(driver):
    log('登录中')
    driver.get("https://reg.lenovo.com.cn/user_auth/toc/#/login")
    tab = driver.find_element(By.XPATH, '//div[@class="tab-pane-item "]/div[1]')
    tab.click()
    uInput = driver.find_element(By.XPATH, '//div[@class="le-input"][1]/input')
    pInput = driver.find_element(By.XPATH, '(//div[@class="le-input"])[2]/input')
    checkBox = driver.find_element(By.XPATH, '//img[@class="le-radio-icon"]')
    uInput.send_keys(phone)
    pInput.send_keys(password)
    checkBox.click()
    loginBtn = driver.find_element(By.XPATH, '//div[text()="登录"]')
    loginBtn.click()
    WebDriverWait(driver, 30).until_not(
        presence_of_element_located((By.XPATH, '//div[@class="shumei_captcha shumei_captcha_popup_wrapper shumei_show"]'))
    )
    log('登录成功')


def log(msg):
    print(datetime.datetime.now(), threading.current_thread().name, msg)


def newDriver():
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-agent=%s' % ua)
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(6)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    return driver


def runTask(url: str):
    driver = newDriver()
    login(driver)
    while True:
        t = time.localtime()
        if 9 <= t.tm_hour <= 12:
            checkAndOrder(driver, url)
        else:
            log('不在开抢时间')
        time.sleep(1)


def main():
    urlList = ['https://mitem.lenovo.com.cn/product/1039473.html', 'https://mitem.lenovo.com.cn/product/1039472.html']
    for url in urlList:
        threading.Thread(target=runTask, args=(url,)).start()
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()


if __name__ == "__main__":
    main()
