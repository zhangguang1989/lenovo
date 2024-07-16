from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
driver = webdriver.Edge(options=options)
driver.implicitly_wait(5)
ready = False
phone = '13880944717'
password = 'ysqkdlxylcmqL2'

def checkAndOrder(url):
    try:
        driver.get(url)
        userNameElem = driver.find_element(By.CLASS_NAME,'userNameNav')
        if userNameElem.text == '':
            login()
            driver.get(url)
        buyBtn = driver.find_element(By.ID,'ljgm')
        if buyBtn.text == '立即购买':
            print(url + ' 发现库存')
            buyBtn.click()
            accountInput = driver.find_element(By.XPATH, '//input[@class="virtual-goods-account-form-input"]')
            accountInput.send_keys(phone)
            submitBtn = driver.find_element(By.XPATH, '//span[@class="fr submitBtn"]')
            submitBtn.click()
            payBtn = driver.find_element(By.XPATH, '//div[text()="立即支付"]')
            print(url + ' 已抢到')
            return True
        else:
            print(url + ' 没库存')
            return False
    except Exception as e:
        print('未知错误 %s' %(e))
        return False
    

def login():
    print('登录中')
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
    print('登录成功')

if __name__ == "__main__":
    while(True):
        if ready:
            t = time.localtime()
            if t.tm_hour >= 9 and t.tm_hour <= 12:
                #500
                rst1 = checkAndOrder("https://item.lenovo.com.cn/product/1037657.html")
                rst1 = rst1 and checkAndOrder("https://item.lenovo.com.cn/product/1037657.html")
                #100
                rst2 = checkAndOrder("https://item.lenovo.com.cn/product/1034686.html")
                rst2 = rst2 and checkAndOrder("https://item.lenovo.com.cn/product/1034686.html")
                if rst1 and rst2:
                    ready = False
                #504
                # checkAndOrder("https://item.lenovo.com.cn/product/1038258.html")
                # ready = False
            else:
                ready = False
        else:
           t = time.localtime()
           if t.tm_hour >= 9 and t.tm_hour <= 12:
               ready = True
               print('设为已准备')
           else:
            print('未准备')
        time.sleep(2)
