import webbrowser
import pyautogui

url = "https://www.hindustantimes.com/ht-img/img/2024/01/05/550x309/ramaswamy_1704445011135_1704445017422.jpeg"
webbrowser.open(url)
pyautogui.sleep(1)
pyautogui.hotkey('ctrl','s')
pyautogui.sleep(1)
pyautogui.press('backspace')
pyautogui.sleep(0.5)
pyautogui.write(r'Y:\image\1234niefhauihfwu iuufaih fuquiwfh uwhfuiwh fuiiufhwui fuiq huiwfh iufhwuihfiuwfiuq uqbfuiqufh iqfh iubfiuweh ufe ')
pyautogui.sleep(1)
pyautogui.press('enter')
print("SAVED")

