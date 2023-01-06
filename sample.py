import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# options = webdriver.ChromeOptions()
# # options.binary_location = '/usr/bin/google-chrome'
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--lang=ja-JP')
# options.add_argument(f'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36') #追加
# options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://accounts.nike.com/lookup?client_id=4fd2d5e7db76e0f85a6bb56721bd51df&redirect_uri=https://www.nike.com/auth/login&response_type=code&scope=openid%20nike.digital%20profile%20email%20phone%20flow%20country&state=9bf76ef1c86e447ca6eca4834f00c1cd&code_challenge=Hn_FU_hXhaMywuvXVDEeVJ2xB0rH3cqDa4aBakCWSV8&code_challenge_method=S256')
# time.sleep(1)
# login = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div/div/div[4]/div/button'))
# login.click()

my_email = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.NAME, "credential"))

#入力欄を空にする
my_email.clear()

#自動入力したメールアドレスを入力
my_email.send_keys("mai.sato@devenues.com")

submit = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div/div[4]/button'))
submit.click()
time.sleep(1)


# パスワードを入力
password = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.NAME, "password"))
password.send_keys('S9!hTtvS86rgHZF')

# # 「ログイン」をクリック
# nextb = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div/div[2]/button')
# nextb.click()
# time.sleep(1)

submit = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/form/div/div[2]/button'))
submit.click()

time.sleep(5)



#ブラウザを閉じる
# driver.close()