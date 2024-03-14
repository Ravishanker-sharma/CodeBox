from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import pyautogui
def uploadvideo(tittle,pathofvideo , nameofuser , passwordofuser):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.41")

    driver = webdriver.Edge(options=options)

    driver.get("https://www.youtube.com/") 
    time.sleep(2)
    cookies = driver.get_cookies()
    driver.find_element(By.XPATH,
                        '''//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]''').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '''//*[@id="identifierId"]''').send_keys(nameofuser)
    driver.find_element(By.XPATH, '''//*[@id="identifierNext"]/div/button''').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '''//*[@id="password"]/div[1]/div/div[1]/input''').send_keys(passwordofuser)
    driver.find_element(By.XPATH, '''//*[@id="passwordNext"]/div/button''').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '''//*[@id="buttons"]/ytd-topbar-menu-button-renderer[2]''').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '''/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[2]/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item''').click()
    time.sleep(2)
    driver.find_element(By.ID, '''create-icon''').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/div/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[1]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string''').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/ytcp-button/div''').click()
    time.sleep(0.5)
    pyautogui.write(pathofvideo)
    pyautogui.press('enter')
    time.sleep(10)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-video-title/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div''').send_keys(
        tittle)
    time.sleep(0.5)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]''').click()
    time.sleep(1)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div''').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]''').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div''').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '''/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div''').click()

    print("VIDEO UPLOADED")
