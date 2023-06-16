import pyautogui
import cv2
import win32gui
import time
from threading import Thread

class WindowControl(object):
    def __init__(self, window_name=""):
        self.window_name = window_name
        self.window_hwnd = win32gui.FindWindow(None, self.window_name)

    def get_hwnd(self):
        return self.window_hwnd

    def get_winname(self):
        return self.window_name

    def get_coord(self):
        l, t, w, h = win32gui.GetClientRect(self.window_hwnd)
        return l, t, w, h
    def get_abscoord(self):
        l, t, w, h = self.get_coord()
        x1, y1 = win32gui.ClientToScreen(self.window_hwnd, (l, t))
        x2, y2 = win32gui.ClientToScreen(self.window_hwnd, (w, h))
        return x1, y1, x2 ,y2

    def screenshot(self, fname='./frame.jpg'):
        x1, y1, x2, y2 = self.get_abscoord()
        w, h = x2 - x1, y2 - y1
        im = pyautogui.screenshot(region=(x1, y1, w, h))  # ltwh
        im.save(fname)


class CurrentWindowControl(WindowControl):
    def __init__(self):
        super().__init__()
        self.window_hwnd = win32gui.GetForegroundWindow()
        self.window_name = win32gui.GetWindowText(self.window_hwnd)

        print(self.window_hwnd, self.window_name)

        self.alive = True
        self.thread = Thread(target=self.update, args=(), daemon=True)
        self.thread.start()

    def update(self):
        # TODO replace Thread to APScheduler
        while self.alive:
            self.window_hwnd = win32gui.GetForegroundWindow()
            self.window_name = win32gui.GetWindowText(self.window_hwnd)
            time.sleep(1)


def test():
    winctrl = CurrentWindowControl()
    print(winctrl.get_winname(), winctrl.get_hwnd())
    winctrl.screenshot('./sample1.jpg')
    time.sleep(5)
    print(winctrl.get_winname(), winctrl.get_hwnd())
    winctrl.screenshot('./sample2.jpg')

    # l, t, w, h = win32gui.GetClientRect(hwnd)
    # x1, y1 = win32gui.ClientToScreen(hwnd, (l, t))
    # x2, y2 = win32gui.ClientToScreen(hwnd, (w, h))
    # print(l, t, w, h)
    # print(x1, y1, x2, y2)
    #
    # im = pyautogui.screenshot(region=(x1, y1, w, h))    # ltwh
    # print(type(im), dir(im))
    # im.save('./sample.jpg')


if __name__ == "__main__":
    test()