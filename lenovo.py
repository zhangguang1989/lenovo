from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
driver = webdriver.Edge(options=options)
driver.implicitly_wait(5)
phone = '13880944717'
password = 'ysqkdlxylcmqL2'


def checkAndOrder(url):
    try:
        driver.get(url)
        userNameElem = driver.find_element(By.CLASS_NAME, 'userNameNav')
        if userNameElem.text == '':
            login()
            driver.get(url)
        buyBtn = driver.find_element(By.ID, 'ljgm')
        if buyBtn.text == '立即购买':
            log(url + ' 发现库存')
            buyBtn.click()
            accountInput = driver.find_element(By.XPATH, '//input[@class="virtual-goods-account-form-input"]')
            accountInput.send_keys(phone)
            submitBtn = driver.find_element(By.XPATH, '//span[@class="fr submitBtn"]')
            submitBtn.click()
            payBtn = driver.find_element(By.XPATH, '//div[text()="立即支付"]')
            log(url + ' 已抢到')
            return True
        else:
            log(url + ' 没库存')
            return False
    except Exception as e:
        log('未知错误 %s' % e)
        return False


def login():
    log('登录中')
    driver.get("https://reg.lenovo.com.cn/user_auth/toc/#/login")
    tab = driver.find_element(By.XPATH, '//div[@class="tab-pane-item "]/div[1]')
    tab.click()
    uInput = driver.find_element(By.XPATH, '//div[@class="le-input"][1]/input')
    pInput = driver.find_element(By.XPATH, '(//div[@class="le-input"])[2]/input')
    checkBox = driver.find_element(By.XPATH, '//img[@class="le-checkbox-icon"]')
    uInput.send_keys(phone)
    pInput.send_keys(password)
    checkBox.click()
    btn = driver.find_element(By.XPATH, '//button[text()="登录"]')
    btn.click()
    time.sleep(1)
    log('登录成功')


def log(msg):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), msg)


if __name__ == "__main__":
    while True:
        t = time.localtime()
        if 9 <= t.tm_hour <= 12:
            # 500
            checkAndOrder("https://item.lenovo.com.cn/product/1037657.html")
            checkAndOrder("https://item.lenovo.com.cn/product/1037657.html")
            # 100
            checkAndOrder("https://item.lenovo.com.cn/product/1034686.html")
            checkAndOrder("https://item.lenovo.com.cn/product/1034686.html")
            # 1008
            # checkAndOrder("https://item.lenovo.com.cn/product/1037866.html")
        else:
            log('不在开抢时间')
        time.sleep(2)
