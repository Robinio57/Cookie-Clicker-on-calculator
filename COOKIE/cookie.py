from data import *
from setting import *
from achiev import *
from language import *

class Game:
  def __init__(self):
    self.all_achi=True
    self.achi_hungry=0
    self.achi_1=True
    self.achi_1000=True
    self.achi_50000=True
    self.achi=0
    self.achi_nb=13
    self.achi_add_10=True
    self.achi_auto_10=True
    self.achi_speed_5=True
    self.achi_speed_20=True
    self.achi_rebirth_1=True
    self.achi_rebirth_5=True
    self.achi_who_fuck_are_you=True
    self.achi_max_out_game=True
    self.cheat=False
    self.free_upgrades=False
    self.multiplicator=1
    self.cookie=0
    self.add=1
    self.price_add=15
    self.auto=0
    self.price_auto=30
    self.auto_speed=21
    self.price_auto_speed=50
    self.rebirth=0
    self.price_rebirth=100000
    self.used_key_dict = {"K_cookie":24,"K_add":81,"K_auto":82,"K_speed":83,"K_rebirth":94,"K_achi":35,"K_settings":21,"K_code":33,"K_end":22}
    self.lg_nb={"en":0,"fr":1,"es":2}
    self.index_lg=self.lg_nb["fr"]
    self.K_dict=K_dict
    self.lg_dict=lg(self)
    
  def run(self):
    start(self)
    running=True
    while running:
      key = getkey()
      if key!=None:
        running=False
        clear()
    running=True
    counter=0
    while running:
      self.lg_dict=lg(self)
      goto(-175,75)
      write(self.lg_dict["cookie"][self.index_lg])
      goto(-175,62)
      if int(self.add*self.multiplicator)==self.add*self.multiplicator:
        write(self.lg_dict["add1"][self.index_lg])
      else:
        write(self.lg_dict["add2"][self.index_lg])
      goto(-175,49)
      if int(self.auto*self.multiplicator)==self.auto*self.multiplicator:
        write(self.lg_dict["auto1"][self.index_lg])
      else:
        write(self.lg_dict["auto2"][self.index_lg])
      goto(-175,36)
      if self.auto_speed>1:
        write(self.lg_dict["speed1"][self.index_lg])
      else:
        write(self.lg_dict["speed2"][self.index_lg])
      goto(-175,23)
      write(self.lg_dict["rebirth"][self.index_lg])
      goto(-175,10)
      if not self.cheat:
        write(self.lg_dict["achi1"][self.index_lg])
      else:
        write(self.lg_dict["achi2"][self.index_lg])
      goto(-175,-3)
      write(self.lg_dict["setting"][self.index_lg])
      goto(-175,-16)
      write(self.lg_dict["quit"][self.index_lg])
      if not self.cheat:
        achievement_fonc(self)
      key=getkey()
      if key==self.used_key_dict["K_cookie"] :
        self.cookie+=self.add*self.multiplicator
        clear()
      elif key==self.used_key_dict["K_add"]:
        if self.cookie>=self.price_add:
          self.add+=1  
          self.cookie-=self.price_add
          self.price_add=int(self.price_add*1.7)
          clear()
        else:
          no_cookie(self)
      elif key==self.used_key_dict["K_auto"]:
        if self.cookie>=self.price_auto:
          self.auto+=1
          self.cookie-=self.price_auto
          self.price_auto=int(self.price_auto*1.7)
          clear()
        else:
          no_cookie(self)
      elif key==self.used_key_dict["K_speed"]:
        if self.cookie>=self.price_auto_speed and self.auto_speed>1:
          self.auto_speed-=1
          self.cookie-=self.price_auto_speed
          self.price_auto_speed=int(self.price_auto_speed*2)
          counter=0
          clear()
        else:
          if self.auto_speed==1:
            max_upgrades(self)
          else:  
            no_cookie(self)
      elif key==self.used_key_dict["K_rebirth"]:
        if self.cookie>=self.price_rebirth:
          rebirth_func(self)
          clear()
        else:
          no_cookie(self)
      elif key==self.used_key_dict["K_achi"]:
        achi_screen(self)
        wait(9990)
      elif key==self.used_key_dict["K_code"]:        
        self.code()
        wait(9990)
      elif key==self.used_key_dict["K_settings"]:
        settings(self)
        clear()
        wait(9990)
      elif key==self.used_key_dict["K_end"]:
        running=end(self)
      wait(9990)
      counter+=1
      if running:
        if counter==self.auto_speed:
          counter=0
          self.cookie+=self.auto*self.multiplicator
          if self.auto>=1:
            clear()
  
  def code(self):
    keylist=[]
    run_code=True
    goto(-50,0)
    while run_code:
      key=None
      key=getkey()
      wait(9990)
      if key!=33 and key!=None and len(keylist)<3:
        keylist.append(key)
        write(str(key))
        wait(50000)
      elif len(keylist)==3:
        if keylist[0]==81:
          if keylist[1]==82:
            if keylist[2]==83:
              clear()
              if not self.cheat:
                write(self.lg_dict["imp achi"][self.index_lg])
                cheat_run=True
                while cheat_run:
                  key=getkey()
                  if key==24 or key==95:
                    clear()
                    self.cheat=True
                    self.cookie+=10000
                    write(self.lg_dict["+cookie"][self.index_lg])
                    wait(50000)
                    cheat_run=False
                  elif key==None:
                    pass
                  else:
                    cheat_run=False
              else:
                self.cookie+=10000
                write(self.lg_dict["+cookie"][self.index_lg])
                wait(50000)
            else:
              error(self)
          else:
            error(self)
        elif keylist[0]==83:
          if keylist[1]==82:
            if keylist[2]==81:
              clear()
              if not self.cheat:
                write(self.lg_dict["imp achi"][self.index_lg])
                cheat_run=True
                while cheat_run:
                  key=getkey()
                  if key==24 or key==95:
                    clear()
                    write(self.lg_dict["no_cost"][self.index_lg])
                    wait(50000)
                    self.price_add=0
                    self.price_auto=0
                    self.price_auto_speed=0
                    self.price_rebirth=0
                    self.cheat=True
                    self.free_upgrades=True
                    cheat_run=False
                  elif key==None:
                    pass
                  else:
                    cheat_run=False
              else:
                clear()
                write(self.lg_dict["no cost"][self.index_lg])
                wait(50000)
                self.price_add=0
                self.price_auto=0
                self.price_auto_speed=0
                self.price_rebirth=0
            else:
              error(self)
          else:
            error(self)
        elif keylist[0]==91:
          if keylist[1]==73:
            if keylist[2]==63:
              clear()
              write(self.lg_dict["hungry"][self.index_lg])
              wait(50000)
              if self.achi_hungry==0:
                self.achi_hungry+=1
            else:
              error(self)
          else:
            error(self)
        else:
          error(self)
        run_code=False
      clear()

game = Game()
game.run()
