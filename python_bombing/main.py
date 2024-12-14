import os
import time
from selenium import webdriver, common
from selenium.webdriver.common.by import By

os.system('cls && title [TikTok Automated Viewbot]')
VIDEO_URL = input('[>] TikTok Video URL: ')

views_sent = 0
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging


def beautify(arg):
    # Adds a "thousands separator" — for readability purposes.
    return format(arg, ',d').replace(',', '.')


driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 660)
driver.get('https://vipto.de/')
print('[!] Solve the captcha...')
captcha = True

while captcha:
    # Attempts to select the "Views" option.
    try:
        driver.find_element(
            By.XPATH,
            '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button'
        ).click()
    except (
        common.exceptions.NoSuchElementException,
        common.exceptions.ElementClickInterceptedException
    ):
        continue
    #driver.set_window_position(-10000, 0)
    print('[!] Running...')
    captcha = False

# Pastes the URL into the "Enter video URL" textbox.
driver.find_element(
    By.XPATH,
    '/html/body/div[10]/div/form/div/input'
).send_keys(VIDEO_URL)

while True:
    # Clicks the "Search" button.
    driver.find_element(
        By.XPATH,
        '/html/body/div[10]/div/form/div/div/button').click()
    time.sleep(160)
    needtobeclose = driver.find_elements(By.CSS_SELECTOR, "[id~='dismiss-button']")
    if(needtobeclose):
        needtobeclose[0].click()
    print(needtobeclose)
    time.sleep(2)
    driver.find_element(
        By.XPATH,
        '/html/body/div[10]/div/form/div/div/button').click()
    time.sleep(5)

    try:
        # Clicks the "Send Views" button.
        driver.find_element(
            By.XPATH,
            '/html/body/div[10]/div/div/div[1]/div/form/button'
        ).click()
    except common.exceptions.NoSuchElementException:
        driver.quit()
        os.system('cls')
        print(
            f'[>] TikTok Video URL: {VIDEO_URL}\n'
            '[!] Solve the captcha...\n'
            '[!] Invalid URL.'
        )
        break
    else:
        views_sent += 1000
        print("+1000 sent total : " + str(views_sent))
        os.system(f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)}')

        seconds = 62
        while seconds > 0:
            seconds -= 1
            os.system(
                f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending '
                f'in: {seconds} seconds'
            )
            time.sleep(1)
        os.system(
            f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending...'
        )

os.system(
    'title [TikTok Automated Viewbot] - Restart required && '
    'pause >NUL && '
    'title [TikTok Automated Viewbot] - Exiting...'
)
time.sleep(3)
print('finished')