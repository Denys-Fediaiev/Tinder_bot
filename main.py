import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = "/Users/raydavis/Desktop/Python Development/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
time.sleep(1)
login_with = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_with.click()
time.sleep(3)
# windows = driver.window_handles
base_window = driver.window_handles[0]
fb = driver.window_handles[1]
driver.switch_to.window(fb)
cookies = driver.find_element(By.CSS_SELECTOR, "div div div div div div._9xo5 button")
cookies.click()

# TODO insert your facebook data
email = driver.find_element(By.NAME, "email")
email.send_keys("Your Email")
password = driver.find_element(By.NAME, "pass")
password.send_keys("Your Password")
fb_login = driver.find_element(By.NAME, "login")
fb_login.click()
driver.switch_to.window(base_window)
time.sleep(7)
allow_location = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div/div[3]/button[1]')
allow_location.click()
ni = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div/div[3]/button[2]')
ni.click()
time.sleep(10)
try:
    like = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
    like.click()
except:
    later = driver.find_element(By.XPATH, '//*[@id="q2069402257"]/main/div/div/div[3]/button[2]')
    later.click()
time.sleep(2)

accept_terms = driver.find_element(By.XPATH, '//*[@id="q-497183963"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_terms.click()

time.sleep(1)
go = True
while go:
    try:
        like_loop = driver.find_element(By.CSS_SELECTOR, "#q-497183963 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button")
        like_loop.click()
    except:
        not_interest = driver.find_element(By.CSS_SELECTOR, '#q2069402257 > main > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\)--ml.Px\(24px\) > button.c1p6lbu0.D\(b\).Mx\(a\)')
        not_interest.click()
        time.sleep(1)
    else:

        time.sleep(1)
#time.sleep(1)
