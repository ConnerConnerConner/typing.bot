from pynput.keyboard import Controller
from pyautogui import screenshot, size
from os import system
from pytesseract import image_to_string
from time import sleep

keyboard = Controller()

def intput(prompt):
    while True:
        try:
            output = str(input(prompt))
            if output == 'nd':
                return output
            else:
                output = int(output)
        except:
            prompt = 'Please Enter a Valid Number:'
        else:
            break
    return output

#Function to get the line to type
def get_line():
    screensize = size()
    width = (screensize[0]/2) - 485
    text_area = screenshot(region=(width, 166, 970, 605))
    return image_to_string(text_area).replace('\n', ' ').replace('  ', ' ') + ' '
           
#Function to type the words
def type(input, wpm):
    if wpm == 'nd':
        sleep_time = 0
    else:
        sleep_time = ((wpm*5)/60)/(((wpm*5)/60)**2)
    for char in input:
        keyboard.press(char)
        keyboard.release(char)
        sleep(sleep_time)

while True:
    stop = 0
    wpm = intput('what is the WPM you\'d like to use?: ')
    print('Focus on Typing.com within the next 3 seconds.')
    sleep(3)
    system('cls')
    print('Typing has started!')
    while True:
        line = get_line()
        if not 'Typing Test Complete!' in line:
            print(line)
            type(line, wpm)
            sleep(0.15)
            stop = 0
        else:
            stop += 1
            if stop == 2:
                break
    input('The Typing Test has concluded!\nPress \"Enter\" to start a new Typing Test!')
    