# 鼠标自动模拟人点击，适合重复性工作

import pyautogui
import time

pyautogui.FAILSAFE = True # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常


def get_mouse_positon():
    # 首次需人工移动，以获取鼠标位置
    time.sleep(3)  # 此间将鼠标移动到初始位置
    x1, y1 = pyautogui.position()
    print(x1, y1)
    pyautogui.click(x=x1, y=y1, button='right')  # 模拟鼠标右键点击，呼出菜单
    time.sleep(5)  # 此间将鼠标移动到“save image as...”选项中央
    x2, y2 = pyautogui.position()
    print(x2, y2)
    pyautogui.click(x=x2, y=y2)  # 模拟鼠标左键点击，点中“save image as...”
    time.sleep(10)  # 此间弹出保存文件弹窗，自行选择保存位置，并将鼠标移至“保存(S)”按钮中央
    x3, y3 = pyautogui.position()
    pyautogui.click(x=x3, y=y3)
    print(x3, y3)


def click_download(N):
    # 控制鼠标移动,duration为持续时间
    for i in range(N):  # 拟下载图片数量
        pyautogui.click(x=517, y=557, duration=0.25, button='right')  # 呼出菜单，自行将x/y设置为x1/y1
        time.sleep(1)
        pyautogui.click(x=664, y=773, duration=0.25)  # 下载，x/y为x2/y2
        time.sleep(1)
        pyautogui.click(x=745, y=559, duration=0.25)  # 保存，x/y为x3/y3
        time.sleep(1)
        pyautogui.click(x=517, y=557, duration=0.25)  # 进入下一张图片
        time.sleep(2) # 取决于网络加载速度，自行设置
    
 
 
if __name__ == "__main__":
    # get_mouse_positon()  # 一开始只运行此命令，获取屏幕坐标，后续注释掉该句
    click_download(10)