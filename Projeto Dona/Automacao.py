import pyautogui as ptg
from time import sleep

def posicao():
    sleep(3)
    lugar = ptg.position()
    print(lugar)


ptg.PAUSE = 2
posicao()
ptg.press("win")
ptg.write("Spotfy")
ptg.press("enter")
sleep(3)
ptg.click(x=97, y=134)