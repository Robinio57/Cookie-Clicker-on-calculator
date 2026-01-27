from donnees import *

forward(0)
hideturtle()
penup()
pencolor("black")

class Game:
  def __init__(self):
    self.all_achi=True
    self.achi_hungry=0
    self.achi_1=True
    self.achi_1000=True
    self.achi_50000=True
    self.achi=0
    self.achi_nb=9
    self.achi_add_10=True
    self.achi_auto_10=True
    self.achi_speed_5=True
    self.achi_speed_20=True
    self.cheat=False
    self.cookie=0
    self.add=1
    self.price_add=15
    self.auto=0
    self.price_auto=30
    self.auto_speed=21
    self.price_auto_speed=50
  
  def run(self):
    start()
    running=True
    while running:
      key = getkey()
      if key!=None:
        running=False
        clear()
    running=True
    counter=0
    while running:
      goto(-175,75)
      write("cookie : "+str(self.cookie)+" | key : OK")
      goto(-175,62)
      write("add : "+str(self.add)+" | cost : "+str(self.price_add)+" | key : 1")
      goto(-175,49)
      write("auto : "+str(self.auto)+" | cost : "+str(self.price_auto)+" | key : 2")
      goto(-175,36)
      if self.auto_speed>1:
        write("auto speed : "+str(21-self.auto_speed)+"/20 | cost : "+str(self.price_auto_speed)+" | key : 3")
      else:
        write("auto speed : "+str(21-self.auto_speed)+"/20")
      goto(-175,23)
      if not self.cheat:
        write("achievement : "+str(self.achi)+" / "+str(self.achi_nb))
      else:
        write("achievement enabled")
      if not self.cheat:
        self.all_achi,self.achi,self.achi_nb,self.achi_1,self.achi_1000,self.achi_50000,self.achi_add_10,self.achi_auto_10,self.achi_speed_5,self.achi_speed_20,self.achi_hungry=achievement_fonc(
          self.cheat,self.cookie,self.add,self.auto,self.auto_speed,self.all_achi,self.achi,self.achi_nb,self.achi_1,self.achi_1000,self.achi_50000,self.achi_add_10,self.achi_auto_10,self.achi_speed_5,self.achi_speed_20,self.achi_hungry)
      key=getkey()
      if key==K_OK :
        self.cookie+=self.add
        clear()
      elif key==K_1:
        if self.cookie>=self.price_add:
          self.add+=1  
          self.cookie-=self.price_add
          self.price_add=int(self.price_add*1.7)
          clear()
      elif key==K_2:
        if self.cookie>=self.price_auto:
          self.auto+=1
          self.cookie-=self.price_auto
          self.price_auto=int(self.price_auto*1.7)
          clear()
      elif key==K_3:
        if self.cookie>=self.price_auto_speed and self.auto_speed>1:
          self.auto_speed-=1
          self.cookie-=self.price_auto_speed
          self.price_auto_speed=int(self.price_auto_speed*2)
          counter=0
          clear()
      elif key==K_BOOK:
        self.achi_screen()
        wait(9990)
      elif key==K_VAR:        
        self.code()
        wait(9990)
      elif key==K_TOOL:
        settings()
        clear()
        wait(9990)
      elif key==K_BACK:
        running=end(self.cookie,self.add,self.auto,self.auto_speed,self.achi,self.achi_nb,self.cheat)
      wait(9990)
      counter+=1
      if running:
        if counter==self.auto_speed:
          counter=0
          self.cookie+=self.auto
          clear()
  
  def code(self):
    keylist=[]
    run_code=True
    goto(-50,0)
    while run_code:
      key=None
      key=getkey()
      wait(9990)
      if key!=K_VAR and key!=None and len(keylist)<3:
        keylist.append(key)
        write(str(key))
        wait(50000)
      elif len(keylist)==3:
        if keylist[0]==K_1:
          if keylist[1]==K_2:
            if keylist[2]==K_3:
              clear()
              if not self.cheat:
                write("Achievements will be impossible")
                cheat_run=True
                while cheat_run:
                  key=getkey()
                  if key==K_OK or key==K_EXE:
                    clear()
                    self.cheat=True
                    self.cookie+=10000
                    write("+10000 cookie")
                    self.cheat=True
                    wait(50000)
                    cheat_run=False
                  elif key==None:
                    pass
                  else:
                    cheat_run=False
              else:
                self.cookie+=10000
                write("+10000 cookie")
                self.cheat=True
                wait(50000)
            else:
              error()
        elif keylist[0]==K_3:
          if keylist[1]==K_2:
            if keylist[2]==K_1:
              clear()
              if not self.cheat:
                write("Achievements will be impossible")
                cheat_run=True
                while cheat_run:
                  key=getkey()
                  if key==K_OK or key==K_EXE:
                    clear()
                    write("Everything is free now !")
                    wait(50000)
                    self.price_add=0
                    self.price_auto=0
                    self.price_auto_speed=0
                    self.cheat=True
                    cheat_run=False
                  elif key==None:
                    pass
                  else:
                    cheat_run=False
              else:
                clear()
                write("Everything is free now !")
                wait(50000)
                self.price_add=0
                self.price_auto=0
                self.price_auto_speed=0
            else:
              error()
          else:
            error()
        elif keylist[0]==K_0:
          if keylist[1]==K_6:
            if keylist[2]==K_9:
              clear()
              write("You, hungry??")
              wait(50000)
              if self.achi_hungry==0:
                self.achi_hungry+=1
            else:
              error()
          else:
            error()
        else:
          error()
        run_code=False
      clear()
    
  def achi_screen(self):
    run_achi=True
    clear()
    screen=0
    while run_achi:
      key=getkey()
      if not self.cheat:
        if screen==0:
          goto(-175,95)
          if not self.achi_1:
            write("There is a begining to everything : collect your 1st cookie")
          else:
            write("???")
          goto(-185,85)
          write("-"*200)
          goto(-175,75)
          if not self.achi_1000:
            write("Like a grandma : reach 1000 cookies")
          else:
            write("???")
          goto(-185,65)
          write("-"*200)
          goto(-175,55)
          if not self.achi_50000:
            write("Do you have any life ? : reach 50000 cookies")
          else:
            write("???")
          goto(-185,45)
          write("-"*200)
          goto(-175,35)
          if not self.achi_add_10:
            write("It's adding up... : reach 10 add upgrades")
          else:
            write("???")
          goto(-185,25)
          write("-"*200)
          goto(-175,15)
          if not self.achi_auto_10:
            write("A little factory : reach 10 auto upgrades")
          else:
            write("???")
          goto(-185,5)
          write("-"*200)
          goto(-175,-5)
          if not self.achi_speed_5:
            write("The FLASH : reach 5 auto speed upgrades")
          else:
            write("???")
          goto(-185,-15)
          write("-"*200)
          if not self.achi_speed_20:
            goto(-175,-25)
            write("Have you kidnapped chinese kids ? : reach all auto speed")
            goto(-175,-35)
            write("upgrades")
          else:
            goto(-175,-30)
            write("???")
          goto(-185,-45)
          write("-"*200)
          goto(-175,-55)
          if self.achi_hungry==2:
            write("8=====- : found a secret code")
          else:
            write("???")
          goto(-185,-65)
          write("-"*200)
          goto(-175,-75)
          if not self.all_achi:
            write("Finisher : you finish the game")
          else:
            write("???")
          goto(-185,-85)
          write("-"*200)
      else:
        goto(-175,95)
        write("You used cheats, achievements are enabled")
        wait(9900)
      if key==K_BACK:
        clear()
        run_achi=False
      wait(9900)

game = Game()
game.run()