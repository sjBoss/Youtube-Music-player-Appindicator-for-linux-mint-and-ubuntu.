import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject as gobject
from selenium import webdriver
from pyvirtualdisplay import Display
import webbrowser
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import signal
import time
import threading
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
import random
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

APPINDICATOR_ID = 'myappindicator'
global flag
flag = 0


def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/subhadip/python/spotify.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    k = gobject.timeout_add(100,pr)
    
    gtk.main()


def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    play = gtk.MenuItem('Start')
    play.connect('activate',play_def)
    stop = gtk.MenuItem('Stop')
    stop.connect('activate',stop_def)
    pause = gtk.MenuItem('Play/Pause')
    pause.connect('activate',pause_def)
    change = gtk.MenuItem('Change')
    change.connect('activate',next1)
    menu.append(play)
    menu.append(pause)
    menu.append(change)
    menu.append(stop)
    
    separator = gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)
    menu.append(item_quit)    
    menu.show_all()
    return menu


def stop_def(source):
  #try:
      flag=1
      
      site.implicitly_wait(5)
      site.back()
      site.quit()
  #except Exception:
      #print("")
 
 
def quit(source):
    try:
      
      site.quit()
    except Exception:
      print("") 
    notify.uninit()  
    gtk.main_quit()


def play_info():
    #global timer
    #timer = site.execute_script("return document.getElementById('movie_player').getDuration()")
    time.sleep(5)
    title = site.find_element_by_id('eow-title')
    title1 = title.text
    title2 = title1.replace("(Official Video)"," ")
    title2 = title2.replace("(Official Music Video)"," ")
    title2 = title2.replace("(OFFICIAL MUSIC VIDEO)"," ")
    title2 = title2.replace("[music video]"," ")
    title2 = title2.replace("(Official Lyrics Video)"," ")
    title2 = title2.replace("[Official Video]"," ")
    title2 = title2.replace("(Lyrics Video)"," ")
    title2 = title2.replace("(Lyric)"," ")
    
    return title2

def next1(source):
     
    site.back()
    site.back()
    song_execution()

def next():
     
    site.back()
    site.back()
    song_execution()     
    

def play_info_display():
    time.sleep(3)
    site.execute_script("document.getElementById('movie_player').setPlaybackQuality('small')")
    string = play_info()
    print(string)
    notify.init(APPINDICATOR_ID)
    n1 = notify.Notification.new('Playing', string)
    n1.set_timeout(3000)
    n1.show()
    #notify.Notification.timeout = 3000
    #notify.Notification.new("<b>Playing</b>", string, None).show()
    print("ggs")
    
    

def pause_def(source):
       
   
       staten = site.execute_script("return document.getElementById('movie_player').getPlayerState()")
       if staten == 1:
           site.execute_script('document.getElementsByTagName("video")[0].pause()')

       elif staten == 2:
           site.execute_script('document.getElementsByTagName("video")[0].play()')
 
       
def play_def(source):
    display = Display(visible=0, size=(800, 600))
    display.start()
    global site
    site = webdriver.Firefox()
    site.get("https://www.youtube.com/playlist?list=PL7-4xVu8FNDDuvU24R1t1PjVADO7DKk4u")
    song_execution()
   
def song_execution():    
    
       x = random.randint(0,50)
       site.implicitly_wait(5)
       song = site.find_elements_by_class_name('pl-video-title-link.yt-uix-tile-link.yt-uix-sessionlink.spf-link')
       
       if x>=4:
         site.execute_script("return arguments[0].scrollIntoView();", song[x-4])
       #time.sleep(1)
       site.implicitly_wait(3)
       song[x].click()
       site.implicitly_wait(4)
       player_status = 1;
       play_info_display()
         
         
def pr():
  global player_status
  player_status = 1;
  
  try:
   player_status = site.execute_script("return document.getElementById('movie_player').getPlayerState()")
   
  except Exception:
   j = 1
     
  
  if player_status == 0:
       next()
  return True     


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    main()

