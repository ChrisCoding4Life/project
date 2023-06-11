import pyautogui
import time

mode = input("what mode AC(clicks at the center of screen) or AM(moves to different places on the screen)")
if mode == "AC":

    button_to_click = input("button to use?: ")
    speed_between_clicks = float(input("speed inbetween clicks?: "))
    num_of_clicks = int(input("number of clicks?:   "))
    mouse_pos = pyautogui.position()
    pyautogui.click(683, y=384, clicks=num_of_clicks, interval=speed_between_clicks, button=f'{button_to_click}')
