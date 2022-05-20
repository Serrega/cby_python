import vlc
from time import sleep

p = vlc.MediaPlayer("alarm.mp3")
p.play()
sleep(5)