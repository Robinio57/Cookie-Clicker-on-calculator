from turtle import *
from casioplot import *

K_dict = {12:("Home","Home"),13:("Left weird arrow","Fleche gauche bizarre"),14:("Up arrow","Fleche haut"),15:("Right weird arrow","Fleche droite bizarre"),16:("Up weird arrow","Fleche haut bizarre"),21:("Settings","Settings"),
          22:("Back","retour"),23:("Left arrow","Fleche gauche"),24:("OK","OK"),25:("Right arrow","Fleche droite"),26:("Down weird arrow","Fleche bas bizarre"),31:("Shift","Shift"),32:("Alpha","Alpha"),33:("Variable","Variable"),
          34:("Down arrow","Fleche bas"),35:("Catalog","Catalog"),36:("Tools","Tools"),41:("x","x"),42:("Fraction","Fraction"),43:("Squareroot","Racine carre"),44:("Exponent","Exposant"),45:("Squared","Carre"),46:("Exponential","exponentielle"),
          51:("Comma","Virgule"),52:("Sin","Sin"),53:("Cos","Cos"),54:("Tan","Tan"),55:("Left round bracket","Parenthese gauche"),56:("Right round bracket","Parenthese droite"),61:("7","7"),62:("8","8"),63:("9","9"),64:("Back space","Effacer"),
          71:("4","4"),72:("5","5"),73:("6","6"),74:("*","*"),75:("/","/"),81:("1","1"),82:("2","2"),83:("3","3"),84:("+","+"),85:("-","-"),91:("0","0"),92:(".","."),93:("Power of 10","Puissance de 10"), 94:("Format","Format"), 95:("Exe","Exe")}

def rebirth_func(self):
  if not self.free_upgrades:
    self.price_rebirth*=5   
    self.price_add=15
    self.price_auto=30
    self.price_auto_speed=50
  else:
    self.price_rebirth=0  
    self.price_add=0
    self.price_auto=0
    self.price_auto_speed=0
  self.multiplicator+=1
  self.rebirth+=1
  self.cookie=0
  self.add=1
  self.auto=0
  self.auto_speed=21

def no_cookie(self):
  goto(-180,-80)
  write(self.lg_dict["no_cookie"][self.index_lg])
  wait(150000)
  clear()

def error(self):
  write(self.lg_dict["error"][self.index_lg])
  wait(50000)

def max_upgrades(self):
  goto(-180,-80)
  write(self.lg_dict["max"][self.index_lg])
  wait(150000)
  clear()

def wait(step):
  for i in range(step):
    pass

def end(self):
  clear()
  run_end=True
  wait(9900)
  while run_end:
    key=getkey()
    goto(-160,0)
    write(self.lg_dict["end1"][self.index_lg])
    goto(-160,-15)
    write(self.lg_dict["end2"][self.index_lg])
    goto(-160,-70)
    write(self.lg_dict["end3"][self.index_lg])
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
  write(self.lg_dict["end4"][self.index_lg])
  goto(-175,62)
  write(self.lg_dict["end5"][self.index_lg])
  goto(-175,49)
  write(self.lg_dict["end6"][self.index_lg])
  goto(-175,36)
  write(self.lg_dict["end7"][self.index_lg])
  goto(-175,23)
  write(self.lg_dict["end8"][self.index_lg])
  goto(-175,10)
  if not self.cheat:
    write(self.lg_dict["end9"][self.index_lg])
  else:
    write(self.lg_dict["achi2"][self.index_lg])
  return False

def start1(self):
  forward(0)
  hideturtle()
  penup()
  pencolor("black")
  goto(-160,30)
  write("1- Play in English")
  goto(-160,20)
  write("2- Jouer en Francais")

def start2(self):
  goto(-160,30)
  write(self.lg_dict["start1"][self.index_lg])
  goto(-160,20)
  write(self.lg_dict["start2"][self.index_lg])
  goto(-160,10)
  write(self.lg_dict["start3"][self.index_lg])
  goto(-160,0)
  write(self.lg_dict["start4"][self.index_lg])
  goto(-160,-10)
  write(self.lg_dict["start5"][self.index_lg])
  goto(-160,-20)
  write(self.lg_dict["start6"][self.index_lg])
  goto(-160,-30)
  write(self.lg_dict["start7"][self.index_lg])
  goto(-160,-40)
  write(self.lg_dict["start8"][self.index_lg])



