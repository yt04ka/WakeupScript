"""
    This python script is used to monitor what is happening on the screen, and if something changes is sets of an alarm
"""

import os
import time
import pyautogui
import cv2


def main():
    while True:
        pyautogui.screenshot("screenshot_old.jpg")
        time.sleep(60)
        pyautogui.screenshot("screenshot_new.jpg")

        old = cv2.imread("screenshot_old.jpg")
        new = cv2.imread("screenshot_new.jpg")

        difference = cv2.subtract(old, new)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            pass
        else:
            os.system("afplay " + "alarm.mp3")
            time.sleep(600)


if __name__ == '__main__':
    main()
