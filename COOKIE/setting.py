from data import *

def settings(self):
  clear()
  running=True
  page="home"
  while running:
    key=getkey()
    if page=="home":
      goto(-175,85)
      write("SETTINGS")
      goto(-175 ,70)
      write("1- Color")
      goto(-175,55)
      write("2- Custom Keybinds")
      goto(-175,40)
      write("3- Language (not 100% comming)")
      if key==81:
        page="color"
        wait(9900)
        key=None
        clear()
        page=color(self)
      if key==82:
        page="key"
        wait(9900)
        key=None
        clear()
        page=define_key(self)
      if key==83:
        page="language"
        wait(9900)
        key=None
        clear()
        page=language(self)
      if key==22:
        return

def color(self):
  clear()
  running=True
  while running:
    key=getkey()
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
      return "home"
    wait(9990)
  
def define_key(self):
  
  def new_key(self,func,newkey):
    clear()
    key_run=True
    key=None
    wait(9990)
    while key_run:
      goto(-175,85)
      write("SETTINGS : CUSTOM KEYBINDS")
      goto(-175,70)
      write("With which keybinds do you want to change this : "+func)
      goto(-175,60)
      write("To quit without changing the keybinds, press : "+K_dict[self.used_key_dict[newkey]])
      already_used = True
      key=getkey()
      if key==self.used_key_dict[newkey]:
        clear()
        return key
      if key != None:
        for elt in self.used_key_dict.values():
          if already_used:
            if key == elt:
              goto(-175,50)
              write("The keybind "+K_dict[key]+" is already used in another function") 
              goto(-175,40)
              write("choose another key")
              already_used=False
              wait(200000)
              clear()
        if already_used:
          clear()
          return key
      wait(9990)
  
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write("SETTINGS : CUSTOM KEYBINDS")
    wait(9990)
    goto(-175,70)
    write("1- Cookie")
    goto(-175,60)
    write("2- Add")
    goto(-175,50)
    write("3- Auto")
    goto(-175,40)
    write("4- Speed")
    goto(-175,30)
    write("5- Rebirth")
    goto(-175,20)
    write("6- Achievements")
    goto(-175,10)
    write("7- Codes")
    goto(-175,0)
    write("8- Settings")
    goto(-175,-10)
    write("9- Quit Game")
    if key==81:
      self.used_key_dict["K_cookie"] = new_key(self,"add cookies","K_cookie")
      wait(9990)
    if key==82:
      self.used_key_dict["K_add"] = new_key(self,"upgrade add","K_add")
      wait(9990)
    if key==83:
      self.used_key_dict["K_auto"] = new_key(self,"upgrade auto","K_auto")
      wait(9990)
    if key==71:
      self.used_key_dict["K_speed"] = new_key(self,"upgrade speed","K_speed")
      wait(9990)
    if key==72:
      self.used_key_dict["K_rebirth"] = new_key(self,"buy rebirth","K_rebirth")
      wait(9990)
    if key==73:
      self.used_key_dict["K_achi"] = new_key(self,"see achievement","K_achi")
      wait(9990)
    if key==61:
      self.used_key_dict["K_code"] = new_key(self,"use code","K_code")
      wait(9990)
    if key==62:
      self.used_key_dict["K_settings"] = new_key(self,"open settings","K_settings")
      wait(9990)
    if key==63:
      self.used_key_dict["K_end"] = new_key(self,"quit game","K_end")
      wait(9990)
    if key==22:
      clear()
      return "home"
    wait(9990)

def language(self):
  clear()
  running=True
  while running:
    key=getkey()
    goto(-175,85)
    write("SETTINGS : Change Language")
    wait(9990)
    goto(-175,70)
    write("Not Implemented Yet")
    if key==22:
      clear()
      return "home"
    wait(9990)