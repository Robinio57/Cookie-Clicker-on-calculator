from data import *

def achi_screen(self):
    screen_max=2
    run_achi=True
    clear()
    screen=1
    while run_achi:
      key=getkey()
      if not self.cheat:
        if screen==1:
          goto(-175,95)
          if not self.achi_1:
            write(self.lg_dict["achi_1"][self.index_lg])
          else:
            write("???")
          goto(-185,85)
          write("-"*200)
          goto(-175,75)
          if not self.achi_1000:
            write(self.lg_dict["achi_1000"][self.index_lg])
          else:
            write("???")
          goto(-185,65)
          write("-"*200)
          goto(-175,55)
          if not self.achi_50000:
            write(self.lg_dict["achi_50000"][self.index_lg])
          else:
            write("???")
          goto(-185,45)
          write("-"*200)
          goto(-175,35)
          if not self.achi_add_10:
            write(self.lg_dict["achi_add_10"][self.index_lg])
          else:
            write("???")
          goto(-185,25)
          write("-"*200)
          goto(-175,15)
          if not self.achi_auto_10:
            write(self.lg_dict["achi_auto_10"][self.index_lg])
          else:
            write("???")
          goto(-185,5)
          write("-"*200)
          goto(-175,-5)
          if not self.achi_speed_5:
            write(self.lg_dict["achi_speed_5"][self.index_lg])
          else:
            write("???")
          goto(-185,-15)
          write("-"*200)
          if not self.achi_speed_20:
            goto(-175,-25)
            write(self.lg_dict["achi_speed_20_1"][self.index_lg])
            goto(-175,-35)
            write(self.lg_dict["achi_speed_20_2"][self.index_lg])
          else:
            goto(-175,-30)
            write("???")
          goto(-185,-45)
          write("-"*200)
          goto(-175,-55)
          if not self.achi_rebirth_1:
            write(self.lg_dict["achi_rebirth_1"][self.index_lg])
          else:
            write("???")
          goto(-185,-65)
          write("-"*200)
          goto(-185,-75)
          write(str(screen)+"/"+str(screen_max))
        elif screen==2:
          goto(-175,95)
          if not self.achi_rebirth_5:
            write(self.lg_dict["achi_rebirth_5"][self.index_lg])
          else:
            write("???")
          goto(-185,85)
          write("-"*200)
          goto(-175,75)
          if not self.achi_who_fuck_are_you:
            write(self.lg_dict["achi_who_fuck_are_you"][self.index_lg])
          else:
            write("???")
          goto(-185,65)
          write("-"*200)
          if not self.achi_speed_20:
            goto(-175,55)
            write(self.lg_dict["achi_max_out_game_1"][self.index_lg])
            goto(-175,45)
            write(self.lg_dict["achi_max_out_game_2"][self.index_lg])
            goto(-175,35)
            write(self.lg_dict["achi_max_out_game_3"][self.index_lg])
          else:
            goto(-175,45)
            write("???")
          goto(-185,25)
          write("-"*200)
          goto(-175,15)
          if not self.achi_hungry:
            write(self.lg_dict["achi_hungry"][self.index_lg])
          else:
            write("???")
          goto(-185,5)
          write("-"*200)
          goto(-175,-5)
          if not self.all_achi:
            write(self.lg_dict["achi_finisher"][self.index_lg])
          else:
            write("???")
          goto(-185,-15)
          write("-"*200)
          goto(-185,-75)
          write(str(screen)+"/"+str(screen_max))
        if key==25 and screen<screen_max:
          screen+=1
          clear()
        if key==23 and screen>1:
          screen-=1
          clear()
      else:
        goto(-175,95)
        write(self.lg_dict["achi3"][self.index_lg])
        wait(9900)
      if key==22:
        clear()
        run_achi=False
      wait(9900)

def achievement_fonc(self):
  if self.achi_1:
    if self.cookie>=1:
      goto(-175,-65)
      write(self.lg_dict["achi_1"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_1=False
      clear()
  if self.achi_1000:
    if self.cookie>=1000:
      goto(-175,-65)
      write(self.lg_dict["achi_1000"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_1000=False
      clear()
  if self.achi_50000:
    if self.cookie>=50000:
      goto(-175,-65)
      write(self.lg_dict["achi_50000"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_50000=False
      clear()
  if self.achi_add_10:
    if self.add>=10:
      goto(-175,-65)
      write(self.lg_dict["achi_add_10"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_add_10=False
      clear()
  if self.achi_auto_10:
    if self.auto>=10:
      goto(-175,-65)
      write(self.lg_dict["achi_auto_10"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_auto_10=False
      clear()
  if self.achi_speed_5:
    if self.auto_speed<=16:
      goto(-175,-65)
      write(self.lg_dict["achi_speed_5"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_speed_5=False
      clear()
  if self.achi_speed_20:
    if self.auto_speed==1:
      goto(-175,-65)
      write(self.lg_dict["achi_speed_20"][self.index_lg])
      goto(-175,-75)
      write("upgrades")
      wait(200000)
      self.achi+=1
      self.achi_speed_20=False
      clear()
  if self.achi_rebirth_1:
    if self.rebirth==1:
      goto(-175,-65)
      write(self.lg_dict["achi_rebirth_1"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_rebirth_1=False
      clear()
  if self.achi_rebirth_5:
    if self.rebirth==5:
      goto(-175,-65)
      write(self.lg_dict["achi_rebirth_5"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_rebirth_5=False
      clear()
  if self.achi_who_fuck_are_you:
    if self.rebirth==20 and self.cookie==10**6:
      goto(-175,-65)
      write(self.lg_dict["achi_who_fuck_are_you"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.who_fuck_are_you=False
      clear()
  if self.achi_max_out_game:
    if self.rebirth==50 and self.add==10000 and self.auto==10000 and self.cookie==10*8 and self.auto_speed==1:
      goto(-175,-55)
      write(self.lg_dict["achi_max_out_game_1"][self.index_lg])
      goto(-175,-65)
      write(self.lg_dict["achi_max_out_game_2"][self.index_lg])
      goto(-175,-75)
      write(self.lg_dict["achi_max_out_game_3"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.achi_max_out_game=False
      clear()
  if self.achi_hungry:
    if self.hungry==1:
      goto(-175,-65)
      write(self.lg_dict["achi_hungry"][self.index_lg])
      wait(200000)
      self.achi_hungry=False
      self.achi+=1
      clear()
  if self.all_achi:
    if self.achi==self.achi_nb-1:
      goto(-175,-65)
      write(self.lg_dict["achi_finisher"][self.index_lg])
      wait(200000)
      self.achi+=1
      self.all_achi=False
      clear()