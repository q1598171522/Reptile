from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class taobao:
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9rn6jBi&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  #设置为开发者模式，防止被各大网站识别出来使用了Selenium


        self.browser = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.browser, 10)   # 超时时长为10s

    def loin_taobao(self):
        self.browser.get(self.url)
        # 进入登录页面
        login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        login.click()
        # 进入微博登录界面
        WBlogin = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        WBlogin.click()
        # 登录微博账号密码
        WBuser = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        WBpassowrd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        WBuser.send_keys(weibo_username)
        WBpassowrd.send_keys(weibo_password)
        WBlogins = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > .W_btn_g')))
        WBlogins.click()

        #选择购物车
        Shopp = self.wait.until(EC.presence_of_element_located((By.ID, 'mc-menu-hd')))
        Shopp.click()

        #结算
        Settlement = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_SelectAll2"]/div/label')))
        Settlement.click()
        time.sleep(0.5)
        Settlements = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_Go"]')))
        Settlements.click()
        Settlementes = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submitOrderPC_1"]/div[1]/a[2]')))
        Settlementes.click()

        #输入支付密码
        passwords = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="payPassword_container"]/div')))
        passwords.send_keys(ZF_password)
        confirm = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_authSubmit"]')))
        confirm.click()

if __name__ == '__main__':
    weibo_username = input("")
    weibo_password = input("")
    ZF_password = input("")
    run = taobao()
    run.loin_taobao()


