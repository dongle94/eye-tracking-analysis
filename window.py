import pyautogui
import cv2
import win32gui
import time

def test():
    cur_win = pyautogui.getActiveWindow()
    print(cur_win.title)

    w = win32gui.GetActiveWindow()
    print(w, type(w), dir(w))
    w = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print(w)

    hwnd = win32gui.FindWindow(None, cur_win.title)
    print(hwnd)

    l, t, w, h = win32gui.GetClientRect(hwnd)
    x1, y1 = win32gui.ClientToScreen(hwnd, (l, t))
    x2, y2 = win32gui.ClientToScreen(hwnd, (w, h))
    print(l, t, w, h)
    print(x1, y1, x2, y2)

    im = pyautogui.screenshot(region=(x1, y1, w, h))    # ltwh
    print(type(im), dir(im))
    im.save('./sample.jpg')


if __name__ == "__main__":
    test()