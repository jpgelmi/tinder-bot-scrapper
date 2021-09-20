from selenium import webdriver
import time
import json
from random import randint

PATH = "/Users/juanpablogelmi/chromedriver"
SECRETS = json.load(open("secrets.json"))

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)

    def login(self):
        self.driver.get("https://tinder.com")

        time.sleep(4)

        login = self.driver.find_element_by_xpath('//*[@class="H(40px) Px(28px)"]')
        login.click()

        time.sleep(3)

        fb_btn = self.driver.find_element_by_xpath('//*[@aria-label="Iniciar sesión con Facebook"]')
        fb_btn.click()

        time.sleep(2)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(SECRETS["EMAIL"])

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(SECRETS["PSW"])

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        time.sleep(5)
        self.driver.switch_to_window(self.driver.window_handles[0])

        print(self.driver.title)
        time.sleep(2)
        geo = self.driver.find_element_by_xpath('//*[@aria-label="Permitir"]')
        geo.click()
        time.sleep(1)
        act = self.driver.find_element_by_xpath('//*[@aria-label="No me interesa"]')
        act.click()

        self.auto_swipe()



    def like(self):
        like_p = self.driver.find_element_by_xpath('//*[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a" ]')
        name = self.driver.find_element_by_xpath('//*[@itemprop="name" ]')
        print(name.text)
        like_p.click()

    def dislike(self):
        dislike_p = self.driver.find_element_by_xpath('//*[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-pink):a"]')
        dislike_p.click()

    def auto_swipe(self):
        time.sleep(6)
        while True:
            time.sleep(randint(2,4))
            try:
                time.sleep(0.3)
                age = self.driver.find_element_by_xpath('//*[@itemprop="age" ]')
                i = int(age.text)
                print(i)
                print(type(i))
                time.sleep(0.3)
                if i <= 20:
                    self.like()
                    pass
                else:
                    self.dislike()
                    pass
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        close = self.driver.find_element_by_xpath('//*[@class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml C($c-secondary) C($c-base):h Fw($semibold) focus-button-style D(b) Mx(a)" ]')
        close.click()

    def close_match(self):
        pass


bot = Bot()
bot.login()
