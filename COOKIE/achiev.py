from data import *

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
          if not self.achi_rebirth_1:
            write("Here we go again ! : reach 1 rebirth")
          else:
            write("???")
          goto(-185,-65)
          write("-"*200)
          goto(-175,-75)
          if not self.achi_rebirth_5:
            write("I've lost everything.. Except my obsession. : reach 5 rebirths")
          else:
            write("???")
          goto(-185,-85)
          write("-"*200)
        elif screen==1:
          goto(-175,95)
          if not self.achi_who_fuck_are_you:
            write("Who The Fuck are you ? : reach 20 rebirths and 1M cookies")
          else:
            write("???")
          goto(-185,85)
          write("-"*200)
          goto(-175,75)
          if not self.achi_speed_20:
            goto(-175,65)
            write("Max Out The Game : reach 50 rebirths, 10k add upgrades,")
            goto(-175,55)
            write("10k auto upgrades, 1M cookies and all auto speed upgrades")
          else:
            goto(-175,60)
            write("???")
          goto(-185,45)
          write("-"*200)
          goto(-175,35)
          if self.achi_hungry==2:
            write("You hungry?? : found a secret code")
          else:
            write("???")
          goto(-185,25)
          write("-"*200)
          goto(-175,15)
          if not self.all_achi:
            write("Finisher : you've finished the game")
          else:
            write("???")
          goto(-185,5)
          write("-"*200)
        if key==25 and screen<1:
          screen+=1
          clear()
        if key==23 and screen>0:
          screen-=1
          clear()
      else:
        goto(-175,95)
        write("You used cheat codes, achievements are disabled")
        wait(9900)
      if key==22:
        clear()
        run_achi=False
      wait(9900)

def achievement_fonc(self):
  if self.achi_1:
    if self.cookie>=1:
      goto(-175,-65)
      write("There is a begining to everything : collect your 1st cookie")
      wait(200000)
      self.achi+=1
      self.achi_1=False
      clear()
  if self.achi_1000:
    if self.cookie>=1000:
      goto(-175,-65)
      write("Like a grandma : reach 1000 cookies")
      wait(200000)
      self.achi+=1
      self.achi_1000=False
      clear()
  if self.achi_50000:
    if self.cookie>=50000:
      goto(-175,-65)
      write("Do you have any life ? : reach 50000 cookies")
      wait(200000)
      self.achi+=1
      self.achi_50000=False
      clear()
  if self.achi_add_10:
    if self.add>=10:
      goto(-175,-65)
      write("It's adding up... : reach 10 add upgrades")
      wait(200000)
      self.achi+=1
      self.achi_add_10=False
      clear()
  if self.achi_auto_10:
    if self.auto>=10:
      goto(-175,-65)
      write("A little factory : reach 10 auto upgrades")
      wait(200000)
      self.achi+=1
      self.achi_auto_10=False
      clear()
  if self.achi_speed_5:
    if self.auto_speed<=16:
      goto(-175,-65)
      write("The FLASH : reach 5 auto speed upgrades")
      wait(200000)
      self.achi+=1
      self.achi_speed_5=False
      clear()
  if self.achi_speed_20:
    if self.auto_speed==1:
      goto(-175,-65)
      write("Have you kidnapped chinese kids ? : reach all auto speed")
      goto(-175,-75)
      write("upgrades")
      wait(200000)
      self.achi+=1
      self.achi_speed_20=False
      clear()
  if self.achi_rebirth_1:
    if self.rebirth==1:
      goto(-175,-65)
      write("Here we go again : reach 1 rebirth")
      wait(200000)
      self.achi+=1
      self.achi_rebirth_1=False
      clear()
  if self.achi_rebirth_5:
    if self.rebirth==5:
      goto(-175,-65)
      write("I've lost everything.. Except my obsession. : reach 5 rebirths")
      wait(200000)
      self.achi+=1
      self.achi_rebirth_5=False
      clear()
  if self.achi_who_fuck_are_you:
    if self.rebirth==20 and self.cookie==10**6:
      goto(-175,-65)
      write("Who The Fuck are you ? : reach 20 rebirths and 1M cookies")
      wait(200000)
      self.achi+=1
      self.who_fuck_are_you=False
      clear()
  if self.achi_max_out_game:
    if self.rebirth==50 and self.add==10000 and self.auto==10000 and self.cookie==10*8 and self.auto_speed==1:
      goto(-175,-65)
      write("Max Out The Game : reach 50 rebirths, 10k add upgrades,")
      goto(-175,-75)
      write("10k auto upgrades, 1M cookies and all auto speed upgrades")
      wait(200000)
      self.achi+=1
      self.achi_max_out_game=False
      clear()
  if self.achi_hungry==1:
    goto(-175,-65)
    write("You hungry?? : found a secret code")
    wait(200000)
    self.achi_hungry+=1
    self.achi+=1
    clear()
  if self.all_achi:
    if self.achi==self.achi_nb-1:
      goto(-175,-65)
      write("Finisher : you finish the game")
      wait(200000)
      self.achi+=1
      self.all_achi=False
      clear()