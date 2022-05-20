import pyglet
from random import randint


vidPath = 'Need_for_Speed.mp4'
window = pyglet.window.Window(1280, 720)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)


pyglet.app.run()

try:
    with open('result.txt', 'r') as file_r:
        content = file_r.readlines()
except BaseException as be:
    print('file error - ', be.args)


if __name__ == '__main__':
    road = (150, 100)
    user_speed = randint(150, 250)
    user_time = (road[0]/user_speed, road[1]/user_speed)
    win_number = user_time.index(max(user_time))
    print(win_number)
    user_input = int(input('Enter number of road, 1 - track, 2 - dirt road: '))









