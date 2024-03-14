import webbrowser
import pyautogui
import os
def save_image(image_saving_path, link):
    if os.path.exists(f'{image_saving_path}.avif'):
        pass
    else:
        url = link
        webbrowser.open(url)
        pyautogui.sleep(3)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.sleep(1)
        pyautogui.press('backspace')
        pyautogui.sleep(1)
        pyautogui.write(image_saving_path)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        pyautogui.hotkey('alt', 'f4')


link = '''https://www.hindustantimes.com/ht-img/img/2024/01/12/550x309/Ayodhya--Ram-Mandir-construction-site-in-Ayodhya--_1705088618598_1705088827335.jpg'''
save_image('hell.jpg', link)