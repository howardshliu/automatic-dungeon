
# coding: utf-8
from pyautogui import click, locateCenterOnScreen, moveRel, mouseDown, mouseUp, doubleClick
import os
from time import sleep, time
from logging import basicConfig, info, INFO


basicConfig(level=INFO, filename='paradise.txt', format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def initial_test():
    XX = locateCenterOnScreen('icon\\XX.png',grayscale=True, confidence=.85)
    while XX is not None:
        click(XX)
        sleep(1)
        XX = locateCenterOnScreen('icon\\XX.png',grayscale=True, confidence=.85)
        moveRel(0,50)
    cancel = locateCenterOnScreen('icon\\cancel.png',grayscale=True, confidence=.85)
    while cancel is not None:
        click(cancel)
        sleep(1)
        cancel = locateCenterOnScreen('icon\\cancel.png',grayscale=True, confidence=.85)
    menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
    safetyzone = locateCenterOnScreen('icon\\safetyzone.png',grayscale=True, confidence=.5)
    transportscroll = locateCenterOnScreen('icon\\transportscroll.png',grayscale=True, confidence=.9)
    if menu and safetyzone and transportscroll is not None:
        return 1
    else:
        return 0

def standby():
    XX = locateCenterOnScreen('icon\\XX.png',grayscale=True, confidence=.85)
    while XX is not None:
        click(XX)
        sleep(1)
        XX = locateCenterOnScreen('icon\\XX.png',grayscale=True, confidence=.85)
        moveRel(0,50)
    cancel = locateCenterOnScreen('icon\\cancel.png',grayscale=True, confidence=.85)
    while cancel is not None:
        click(cancel)
        sleep(1)
        cancel = locateCenterOnScreen('icon\\cancel.png',grayscale=True, confidence=.85)
    sleep(1)
    click(locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8))
    sleep(1.5)
    click(locateCenterOnScreen('icon\\dugeon.png',grayscale=True, confidence=.8))
    sleep(2)
    Dugeontest = locateCenterOnScreen('icon\\dugeontest.png',grayscale=True, confidence=.88)
    click(Dugeontest)
    sleep(1.5)
    li = []
    for i in range(1,7):
        pic = locateCenterOnScreen('icon\\dugeon'+ str(i) +'.png',grayscale=True, confidence=.8)
        if i == 1:
            pass
        elif i == 3:
            pass
        elif pic is not None:
            li.append(pic)
    if len(li) == 0:
        question = locateCenterOnScreen('icon\\question.png',grayscale=True, confidence=.88)
        mouseDown(question[0],question[1]+100) 
        sleep(1)
        moveRel(-775,0 ,duration=0.5)
        mouseUp()
        moveRel(0,-100)
        for i in range (7,10):
            pic = locateCenterOnScreen('icon\\dugeon'+ str(i) +'.png',grayscale=True, confidence=.8)
            if pic is not None:
                li.append(pic)
        click(li[0])
        sleep(1)
        click(locateCenterOnScreen('icon\\confirm1.png',grayscale=True, confidence=.8))  
        return 1
    else:
        click(li[0])
        sleep(1)
        click(locateCenterOnScreen('icon\\confirm1.png',grayscale=True, confidence=.8))
        return 1
    
def judge():
    sleep(3)
    for i in range(1,10):
        image = i, locateCenterOnScreen('icon\\dugeon'+ str(i) +'judge.png',grayscale=True, confidence=.8)
        if image[1] is not None:
            click(image[1])
            return image[0]


def second_test():
    sleep(0.5)
    autofight = locateCenterOnScreen('icon\\autofight.png',grayscale=True, confidence=.7)
    click(autofight)
    missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
    secondproof = locateCenterOnScreen('icon\\secondproof.png',grayscale=True, confidence=.8)
    ill = locateCenterOnScreen('icon\\ill.png',grayscale=True, confidence=.8)
    while 1:
        if missioncomplete is not None and ill is None:
            sleep(3)
            click(missioncomplete)
            info('任務完成')
            sleep(2)
            break
        elif missioncomplete is None and ill is None:
            sleep(3)
            info('任務完成囉')
            break
        else:
            click(ill)
            info('繼續打')
            moveRel(0,50)
            sleep(2.2)
            secondproof = locateCenterOnScreen('icon\\secondproof.png',grayscale=True, confidence=.8)
            missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
            ill = locateCenterOnScreen('icon\\ill.png',grayscale=True, confidence=.8)
            


def forth_test():
    sleep(0.5)
    transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
    same = 0
    missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
    while 1:
        goal2 = locateCenterOnScreen('icon\\goal2.png',grayscale=True, confidence=.75)
        if goal2 is None and missioncomplete is not None:
            click(missioncomplete)
            info('任務完成(點圈圈或直接飛到)')
            sleep(2)
            break
        elif goal2 is not None:
            click(goal2)
            info('找到圈圈 點圈圈')
            sleep(8)
            same = goal2
            missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.9)
            goal2 = locateCenterOnScreen('icon\\goal2.png',grayscale=True, confidence=.75)
            if same == goal2:
                info('卡點或點不到goal，再飛一次')
                click(transport)
                sleep(2)
        elif transport is None:
            menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
            test1proof = locateCenterOnScreen('icon\\test1proof.png',grayscale=True, confidence=.7)
            if menu and test1proof is None:
                info('任務結束!')
                sleep(2)
                break
            else:
                movebutton = locateCenterOnScreen('icon\\movebutton.png',grayscale=True, confidence=.8)
                click(movebutton[0],movebutton[0]-200)
                sleep(2)
                menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
                test1proof = locateCenterOnScreen('icon\\test1proof.png',grayscale=True, confidence=.7)

        else:
            click(transport)
            info('未找到終點 繼續飛')
            sleep(1.5)
            moveRel(0,50)
            sleep(1)
            transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
            missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
            
def fifth_test():
    sleep(0.5)
    transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
    same = 0
    missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.7)
    while 1:
        treasure1 = locateCenterOnScreen('icon\\treasure1.png',grayscale=True, confidence=.85)
        if treasure1 is None and missioncomplete is not None:
            click(missioncomplete)
            info('任務完成')
            sleep(2)
            break
        elif treasure1 is not None:
            doubleClick(treasure1, duration=0.5)
            info('點寶箱')
            sleep(5)
            same = treasure1
            treasure1 = locateCenterOnScreen('icon\\treasure1.png',grayscale=True, confidence=.85)
            if same == treasure1:
                info('卡點或點不到寶箱，再飛一次')
                click(transport)
                moveRel(0,50)
                sleep(2)
                transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
        elif transport is None:
            menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
            test2proof = locateCenterOnScreen('icon\\test2proof.png',grayscale=True, confidence=.8)
            if menu is not None and test2proof is None:
                info('任務結束!')
                sleep(2)
                break
            else:
                transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
                pass
        else:
            click(transport)
            info('未找到寶箱 繼續飛')
            sleep(1.5)
            moveRel(0,50)
            sleep(1)
            transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
            missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.7)
def sixth_test():
    sleep(0.5)
    transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
    autofight = locateCenterOnScreen('icon\\autofight.png',grayscale=True, confidence=.7)
    click(autofight)
    missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
    while 1:
        if missioncomplete is not None:
            sleep(3)
            click(missioncomplete)
            info('任務完成')
            sleep(2)
            break
        elif transport is None:
            sleep(3)
            menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
            thirdproof = locateCenterOnScreen('icon\\thirdproof.png',grayscale=True, confidence=.8)
            if menu is not None and thirdproof is None:
                info('任務結束!')
                sleep(2)
                break
            else:
                info('找不到按鈕，等兩秒繼續')
                sleep(2)
                missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
                transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
        else:
            click(transport)
            info('未打完，繼續飛')
            sleep(6)
            moveRel(0,50)
            sleep(1)
            transport = locateCenterOnScreen('icon\\transport.png',grayscale=True, confidence=.9)
            missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)


def seventh_test():
    sleep(0.5)
    autofight = locateCenterOnScreen('icon\\autofight.png',grayscale=True, confidence=.68)
    click(autofight)
    sleep(9)
    alive = locateCenterOnScreen('icon\\alive.png',grayscale=True, confidence=.75)
    kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.7)
    transportscroll = locateCenterOnScreen('icon\\transportscroll.png',grayscale=True, confidence=.9)
    while 1:
        if kill is None and alive is not None:
            click(transportscroll)
            info('順移打怪')
            sleep(8)
            kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.7)
            alive = locateCenterOnScreen('icon\\alive.png',grayscale=True, confidence=.75)
        elif kill is None and alive is None:
            sleep(2)
            alive = locateCenterOnScreen('icon\\alive.png',grayscale=True, confidence=.75)
            if alive is None:
                sleep(5)
                missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
                click(missioncomplete)
                info('任務結束!')
                sleep(2)
                break
        else:
            click(alive)
            sleep(0.5)
            moveRel(0,50)
            sleep(2)
            kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.8)
            alive = locateCenterOnScreen('icon\\alive.png',grayscale=True, confidence=.75)

def eigth_test():
    sleep(0.5)
    autofightice = locateCenterOnScreen('icon\\autofightice.png',grayscale=True, confidence=.7)
    click(autofightice)
    sleep(10)
    storm = locateCenterOnScreen('icon\\storm.png',grayscale=True, confidence=.75)
    transportscroll = locateCenterOnScreen('icon\\transportscroll.png',grayscale=True, confidence=.9)
    kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.6)
    while 1:
        if kill is None and storm is not None:
            click(transportscroll)
            info('順移打怪')
            sleep(10)
            kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.7)
            storm = locateCenterOnScreen('icon\\storm.png',grayscale=True, confidence=.75)
        elif kill is None and storm is None:
            sleep(2)
            storm = locateCenterOnScreen('icon\\storm.png',grayscale=True, confidence=.75)
            if storm is None:
                sleep(5)
                missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
                click(missioncomplete)
                info('任務結束!')
                sleep(2)
                break
        else:
            click(storm)
            sleep(0.5)
            moveRel(0,50)
            sleep(1)
            kill = locateCenterOnScreen('icon\\kill.png',grayscale=True, confidence=.7)
            storm = locateCenterOnScreen('icon\\storm.png',grayscale=True, confidence=.75)

def ninth_test():
    sleep(0.5)
    menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
    mouseDown(menu[0]-1045,menu[1]+530) 
    sleep(1)
    moveRel(50,50)
    sleep(11)
    mouseUp()
    autofight = locateCenterOnScreen('icon\\autofight.png',grayscale=True, confidence=.7)
    click(autofight)
    while 1:
        missioncomplete = locateCenterOnScreen('icon\\missioncomplete.png',grayscale=True, confidence=.8)
        test6proof = locateCenterOnScreen('icon\\test6proof.png',grayscale=True, confidence=.8)
        if missioncomplete is not None and test6proof is None:
            sleep(2)
            click(missioncomplete)
            info('任務完成')
            break
        elif missioncomplete and test6proof is None:
            sleep(3)
            menu = locateCenterOnScreen('icon\\menu.png',grayscale=True, confidence=.8)
            if menu is not None:
                info('任務結束')
                break 
        else:
            ass = locateCenterOnScreen('icon\\ass.png',grayscale=True, confidence=.7)
            if ass is not None:
                click(ass)
            sleep(2)