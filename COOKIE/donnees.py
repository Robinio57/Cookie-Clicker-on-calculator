from turtle import *
from casioplot import *

def no_cookie():
  goto(-100,-80)
  write("You can't buy that, you don't have enough cookies!")
  wait(150000)
  clear()

def settings():
  clear()
  running=True
  page="home"
  while running:
    key=getkey()
    if page=="home":
      goto(-175,85)
      write("SETTINGS")
      goto(-175 ,70)
      write("1- color")
      if key==K_1:
        page="color"
        wait(9900)
        key=None
        clear()
    elif page=="color":
      goto(-175,85)
      write("SETTINGS : COLOR")
      wait(9990)
      goto(-175,70)
      write("1- Black")
      goto(-175,60)
      write("2- Red")
      goto(-175,50)
      write("3- Blue")
      goto(-175,40)
      write("4- Green")
      goto(-175,30)
      write("5- Purple")
      goto(-175,20)
      write("6- Yellow")
      goto(-175,10)
      write("7- Brown")
      goto(-175,0)
      write("8- Pink")
      goto(-175,-10)
      write("9- Orange")
      if key==K_1:
        pencolor("black")
      if key==K_2:
        pencolor("red")
      if key==K_3:
        pencolor("blue")
      if key==K_4:
        pencolor("green")
      if key==K_5:
        pencolor("purple")
      if key==K_6:
        pencolor("yellow")
      if key==K_7:
        pencolor("brown")
      if key==K_8:
        pencolor("pink")
      if key==K_9:
        pencolor("orange")
    if key==K_BACK:
      if page=="home":
        running=False
        key=None
      else:
        page="home"
        key=None
        clear()
    wait(9990)
    
def achievement_fonc(cheat,cookie,add,auto,auto_speed,all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry):
  if achi_1:
    if cookie>=1:
      goto(-175,-65)
      write("There is a begining to everything : collect your 1st cookie")
      wait(200000)
      achievement+=1
      achi_1=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_1000:
    if cookie>=1000:
      goto(-175,-65)
      write("Like a grandma : reach 1000 cookies")
      wait(200000)
      achievement+=1
      achi_1000=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_50000:
    if cookie>=50000:
      goto(-175,-65)
      write("Do you have any life ? : reach 50000 cookies")
      wait(200000)
      achievement+=1
      achi_50000=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_add_10:
    if add>=10:
      goto(-175,-65)
      write("It's adding up... : reach 10 add upgrades")
      wait(200000)
      achievement+=1
      achi_add_10=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_auto_10:
    if auto>=10:
      goto(-175,-65)
      write("A little factory : reach 10 auto upgrades")
      wait(200000)
      achievement+=1
      achi_auto_10=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_speed_5:
    if auto_speed<=16:
      goto(-175,-65)
      write("The FLASH : reach 5 auto speed upgrades")
      wait(200000)
      achievement+=1
      achi_speed_5=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_speed_20:
    if auto_speed==1:
      goto(-175,-65)
      write("Have you kidnapped chinese kids ? : reach all auto speed")
      goto(-175,-75)
      write("upgrades")
      wait(200000)
      achievement+=1
      achi_speed_20=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if achi_hungry==1:
    goto(-175,-65)
    write("8=====- : found a secret code")
    wait(200000)
    achi_hungry+=1
    achievement+=1
    clear()
    return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  if all_achi:
    if achievement==achi_nb-1:
      goto(-175,-65)
      write("Finisher : you finish the game")
      wait(200000)
      achievement+=1
      all_achi=False
      clear()
      return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
  return all_achi,achievement,achi_nb,achi_1,achi_1000,achi_50000,achi_add_10,achi_auto_10,achi_speed_5,achi_speed_20,achi_hungry
      
def error():
  write("Error")
  wait(50000)

def wait(step):
  for i in range(step):
    pass

def end(cookie,add,auto,auto_speed,achi,achi_nb,cheat):
  clear()
  run_end=True
  wait(9900)
  while run_end:
    key=getkey()
    goto(-50,0)
    write("Do you want to quit the game?")
    if key==None:
      pass
    elif key==K_EXE or key==K_OK:
      run_end=False
    else:
      clear()
      return True
    wait(9900)
  clear()
  goto(-175,75)
  write("cookie : "+str(cookie))
  goto(-175,62)
  write("add bought : "+str(add))
  goto(-175,49)
  write("auto bought : "+str(auto))
  goto(-175,36)
  write("auto speed bought : "+str(21-auto_speed))
  goto(-175,23)
  if not cheat:
    write("achievement : "+str(achi)+" / "+str(achi_nb))
  else:
    write("achievement disabled")
  return False

def start():
  forward(0)
  hideturtle()
  penup()
  pencolor("black")
  goto(-100,30)
  write("Welcome in Cookie Clicker !!")
  goto(-100,20)
  write("To obtain cookies : press OK")
  goto(-100,10)
  write("To buy upgrades : press 1, 2 or 3")
  goto(-100,0)
  write("To see your achievements : press CATALOG")
  goto(-100,-10)
  write("To change the settings : press TOOLS")
  goto(-100,-20)
  write("To use cheat codes : press VARIABLE")
  goto(-100,-30)
  write("To start the game : press any key")
  goto(-190,-80)
  write("v1.1")
  goto(80,-80)
  write("Author : Robinio57")

K_TOOL=36
K_BOOK=35
K_BACK=22
K_OK=24
K_VAR=33
K_EXE=95
K_1=81
K_2=82
K_3=83
K_4=71
K_5=72
K_6=73
K_7=61
K_8=62
K_9=63
K_0=91