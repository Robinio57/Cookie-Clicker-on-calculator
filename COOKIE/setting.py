from data import *

def settings(self):
  clear()
  running=True
  page="home"
  leave=False
  while running:
    key=getkey()
    if page=="home":
      goto(-175,85)
      write(self.lg_dict["set_main1"][self.index_lg])
      goto(-175 ,70)
      write(self.lg_dict["set_main2"][self.index_lg])
      goto(-175,55)
      write(self.lg_dict["set_main3"][self.index_lg])
      goto(-175,40)
      write(self.lg_dict["set_main4"][self.index_lg])
      goto(-175,25)
      write(self.lg_dict["set_main5"][self.index_lg])
      if key==81:
        page="color"
        wait(9900)
        key=None
        clear()
        page,leave=color(self)
      if key==82:
        page="key"
        wait(9900)
        key=None
        clear()
        page,leave=define_key(self)
      if key==83:
        page="language"
        wait(9900)
        key=None
        clear()
        page,leave=language(self)
      if key==91:
        page="about"
        wait(9990)
        key=None
        clear()
        page,leave=about(self)
      if key==22 or key==12:
        return
      if leave:
        return

def about(self):
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write(self.lg_dict["set_about1"][self.index_lg])
    wait(9990)
    goto(-175,70)
    write(self.lg_dict["set_about2.1"][self.index_lg])
    goto(-175,55)
    write(self.lg_dict["set_about2.2"][self.index_lg])
    goto(-175,40)
    write(self.lg_dict["set_about3"][self.index_lg])
    goto(-175,25)
    write(self.lg_dict["set_about4"][self.index_lg])
    if key==12:
      clear()
      return "home",True 
    if key==22:
      clear()
      return "home",False 
    wait(9990)

def color(self):
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write(self.lg_dict["set_color1"][self.index_lg])
    wait(9990)
    goto(-175,70)
    write(self.lg_dict["set_color2"][self.index_lg])
    goto(-175,55)
    write(self.lg_dict["set_color3"][self.index_lg])
    goto(-175,40)
    write(self.lg_dict["set_color4"][self.index_lg])
    goto(-175,25)
    write(self.lg_dict["set_color5"][self.index_lg])
    goto(-175,10)
    write(self.lg_dict["set_color6"][self.index_lg])
    goto(-175,-5)
    write(self.lg_dict["set_color7"][self.index_lg])
    goto(-175,-20)
    write(self.lg_dict["set_color8"][self.index_lg])
    goto(-175,-35)
    write(self.lg_dict["set_color9"][self.index_lg])
    goto(-175,-50)
    write(self.lg_dict["set_color10"][self.index_lg])
    if key==81:
      pencolor("black")
    if key==82:
      pencolor("red")
    if key==83:
      pencolor("blue")
    if key==71:
      pencolor("green")
    if key==72:
      pencolor("purple")
    if key==73:
      pencolor("yellow")
    if key==61:
      pencolor("brown")
    if key==62:
      pencolor("pink")
    if key==63:
      pencolor("orange")
    if key==22:
      clear()
      return "home",False
    if key==12:
      clear()
      return "home",True
    wait(9990)

def define_key(self):
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write(self.lg_dict["set_key1"][self.index_lg])
    wait(9990)
    goto(-175,70)
    write(self.lg_dict["set_key2"][self.index_lg])
    goto(-175,55)
    write(self.lg_dict["set_key3"][self.index_lg])
    goto(-175,40)
    write(self.lg_dict["set_key4"][self.index_lg])
    goto(-175,25)
    write(self.lg_dict["set_key5"][self.index_lg])
    goto(-175,10)
    write(self.lg_dict["set_key6"][self.index_lg])
    goto(-175,-5)
    write(self.lg_dict["set_key7"][self.index_lg])
    goto(-175,-20)
    write(self.lg_dict["set_key8"][self.index_lg])
    goto(-175,-35)
    write(self.lg_dict["set_key9"][self.index_lg])
    goto(-175,-50)
    write(self.lg_dict["set_key10"][self.index_lg])
    goto(-175,-65)
    write(self.lg_dict["set_key11"][self.index_lg])
    if key==81:
      self.used_key_dict["K_cookie"] = new_key(self,("add cookies","cookie par click"),"K_cookie")
      wait(9990)
    if key==82:
      self.used_key_dict["K_add"] = new_key(self,("upgrade add","amelioration click"),"K_add")
      wait(9990)
    if key==83:
      self.used_key_dict["K_auto"] = new_key(self,("upgrade auto","amelioration auto"),"K_auto")
      wait(9990)
    if key==71:
      self.used_key_dict["K_speed"] = new_key(self,("upgrade speed","amel. vitesse"),"K_speed")
      wait(9990)
    if key==72:
      self.used_key_dict["K_rebirth"] = new_key(self,("rebirth","rennaissance"),"K_rebirth")
      wait(9990)
    if key==73:
      self.used_key_dict["K_achi"] = new_key(self,("achievements","succes"),"K_achi")
      wait(9990)
    if key==61:
      self.used_key_dict["K_code"] = new_key(self,("codes","codes"),"K_code")
      wait(9990)
    if key==62:
      self.used_key_dict["K_settings"] = new_key(self,("settings","parametres"),"K_settings")
      wait(9990)
    if key==63:
      self.used_key_dict["K_end"] = new_key(self,("quit game","quitter le jeu"),"K_end")
      wait(9990)
    if key==91:
      clear()
      goto(-175,85)
      write(self.lg_dict["set_key1"][self.index_lg])
      goto(-175,70)
      write(self.lg_dict["set_reset"][self.index_lg])
      reset=True
      while reset:
        key=getkey()
        if key==24:
          reset=False
          self.used_key_dict = {"K_cookie":24,"K_add":81,"K_auto":82,"K_speed":83,"K_rebirth":94,"K_achi":35,"K_settings":21,"K_code":33,"K_end":22}
        elif key==22:
          reset=False
        wait(9990)
      wait(9990)
      clear()
      key=None
    if key==22:
      clear()
      return "home",False
    if key==12:
      clear()
      return "home",True
    wait(9990)

def new_key(self,func,newkey):
  clear()
  key_run=True
  key=None
  wait(9990)
  while key_run:
    goto(-175,85)
    write(self.lg_dict["set_key1"][self.index_lg])
    goto(-175,70)
    set_new_key1 = ("With which keybinds do you want to change : "+func[self.index_lg],"Avec quelle touche tu veux changer : "+func[self.index_lg])
    write(set_new_key1[self.index_lg])
    goto(-175,55)
    set_new_key2 = ("Return without changing the keybinds : "+K_dict[self.used_key_dict[newkey]][self.index_lg],"Revenir sans changer la touche : "+K_dict[self.used_key_dict[newkey]][self.index_lg])
    write(set_new_key2[self.index_lg])
    already_used = True
    key=getkey()
    change_key = key
    if change_key==self.used_key_dict[newkey]:
      clear()
      return change_key
    if change_key != None:
      for elt in self.used_key_dict.values():
        if already_used:
          if change_key == elt:
            goto(-175,40)
            set_new_key3 = ("The keybind "+K_dict[change_key][self.index_lg]+" is already used in another function","La touche "+K_dict[change_key][self.index_lg]+" est deja utilise dans une autre fonction")
            write(set_new_key3[self.index_lg]) 
            already_used=False
            wait(200000)
            clear()
      if already_used:
        clear()
        return change_key
    wait(9990)

def language(self):
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write(self.lg_dict["set_lan"][self.index_lg])
    wait(9990)
    goto(-175,70)
    write("1- English")
    goto(-175,55)
    write("2- Francais")
    if key==81:
      self.index_lg=self.lg_nb["en"]
      clear()
      wait(9990)
    if key==82:
      self.index_lg=self.lg_nb["fr"]
      clear()
      wait(9990)
    if key==22:
      clear()
      return "home",False
    if key==12:
      clear()
      return "home",True
    wait(9990)