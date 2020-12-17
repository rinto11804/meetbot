from pyautogui import hotkey ,typewrite ,click,prompt
from time import sleep
code=prompt(text="enter the meeting code",title="meetbot")#ask for meeting code
hotkey("winleft")#cick on windows logo
sleep(3)
typewrite("chrome\n",0.2)#type chrome in input fleid 
sleep(1)
typewrite("https://meet.google.com\n",0.1)#type meet link in address bar
sleep(7)
click(601,732)#click on input fleid to enter meeting code
typewrite(code)#enters the meeting code
sleep(5)
click(678,732)#cick on join button
sleep(20)
click(x=703, y=818)#off vedio
sleep(1)
click(x=633, y=817)#off audio
sleep(1)
click(x=1351, y=609)#ask to join
sleep(10)
click(x=1663, y=170)#click on chat box icon
sleep(2)
typewrite("your name\n")#enter your name in chat box
