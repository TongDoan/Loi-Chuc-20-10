import pyautogui, pyperclip, time
import time
import cv2
from time import sleep
import sys
import tkinter
line_1 = "  Nếu giọt nước là những nụ hôn, anh sẽ trao em biển cả\n"
line_2 = "  Nếu lá là những ôm ấp vuốt ve, anh sẽ tặng em cả rừng cây\n"
line_3 = "  Nếu đêm dài là tình yêu, anh muốn gửi em cả trời sao lấp lánh\n"
line_4 = "  Nhưng trái tim anh không thể dành tặng em được\n"
line_5 = "  Vì nơi đó đã thuộc về em rồi\n"
line_6 = "  Chúc em một ngày 20/10 hạnh phúc.\n"
for l1 in line_1:
    print(l1, end='')
    sys.stdout.flush()
    sleep(0.06)
for l2 in line_2:
    print(l2, end='')
    sys.stdout.flush()
    sleep(0.06)
sleep(0.4)
for l3 in line_3:
    print(l3, end='')
    sys.stdout.flush()
    sleep(0.06)
sleep(0.8)
for l4 in line_4:
    print(l4, end='')
    sys.stdout.flush()
    sleep(0.06)
for l5 in line_5:
    print(l5, end='')
    sys.stdout.flush()
    sleep(0.05)
for l6 in line_6:
    print(l6, end='')
    sys.stdout.flush()
    sleep(0.05)
sleep(1)
msg = "Bé iu A❤!"
print("\nQuay trờ lại đoạn chat với mình và đợi 5s bất ngờ sẽ đến với e!")
sleep(2)
for i in range(5,0,-1):
    print(i ,"...",end=" ",flush=True)
    time.sleep(1)
pyperclip.copy(msg)
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

