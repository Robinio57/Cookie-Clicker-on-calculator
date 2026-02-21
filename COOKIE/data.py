from turtle import *
from casioplot import *

def rebirth_func(self):
  if not self.free_upgrades:
    self.price_rebirth*=5   
    self.price_add=15
    self.price_auto=30
    self.price_auto_speed=50
  else:
    self.price_rebirth*=5  
    self.price_add=0
    self.price_auto=0
    self.price_auto_speed=0
  self.multiplicator+=1
  self.rebirth+=1
  self.cookie=0
  self.add=1
  self.auto=0
  self.auto_speed=21

def no_cookie():
  goto(-100,-80)
  write("You can't buy that, you don't have enough cookies!")
  wait(150000)
  clear()

def error():
  write("Error")
  wait(50000)

def wait(step):
  for i in range(step):
    pass

def end(self):
  clear()
  run_end=True
  wait(9900)
  while run_end:
    key=getkey()
    goto(-50,0)
    write("Do you want to quit the game?")
    wait(10000)
    if key==None:
      pass
    elif key==95 or key==24:
      run_end=False
    else:
      clear()
      return True
    wait(9900)
  clear()
  goto(-175,75)
  write("Cookie : "+str(self.cookie))
  goto(-175,62)
  write("Add bought : "+str(self.add-1))
  goto(-175,49)
  write("Auto bought : "+str(self.auto))
  goto(-175,36)
  write("Auto speed bought : "+str(21-self.auto_speed))
  goto(-175,23)
  write("Rebirth bought : "+str(self.rebirth))
  goto(-175,10)
  if not self.cheat:
    write("Achievement : "+str(self.achi)+" / "+str(self.achi_nb))
  else:
    write("Achievement disabled")
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
  write("To buy rebirths : press FORMAT")
  goto(-100,-10)
  write("To see your achievements : press CATALOG")
  goto(-100,-20)
  write("To change the settings : press TOOLS")
  goto(-100,-30)
  write("To use cheat codes : press VARIABLE")
  goto(-100,-40)
  write("To start the game : press any key")
  goto(-190,-80)
  write("v2.0")
  goto(80,-80)
  write("Author : Robinio57")

K_dict = {12:"Home",13:"Left weird arrow",14:"Up arrow",15:"Right weird arrow",16:"Up weird arrow",21:"Settings",22:"Back",23:"Left arrow",24:"Ok",25:"Right arrow",26:"Down weird arrow",31:"Shift",32:"Alpha",33:"Variable",34:"Down arrow",35:"Catalog",
          36:"Tools",41:"x",42:"Fraction",43:"Squareroot",44:"Power",45:"Squared",46:"Exponential",51:"Virgula",52:"Sin",53:"Cos",54:"Tan",55:"Left round bracket",56:"Right round bracket", 61:"7",62:"8",63:"9",64:"Back space",71:"4",72:"5",73:"6",

          74:"*",75:"/",81:"1",82:"2",83:"3",84:"+",85:"-",91:"0",92:".",93:"Power of 10", 94:"Format", 95:"Exe"}
