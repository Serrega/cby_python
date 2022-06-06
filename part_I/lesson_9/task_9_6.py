import pyglet
from random import randint


def video_play():
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


def paint_pictures(win=True):
    print(win)
    try:
        with open('result.txt', 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
    except BaseException as be:
        print('file error - ', be.args)
    if win:
        print('\n', *content[20:])
    else:
        print(*content[:20])


if __name__ == '__main__':
    road = (150, 100)
    user_speed = randint(150, 250)
    user_time = (road[0] / user_speed, road[1] / user_speed)
    win_number = user_time.index(min(user_time))
    video_play()
    user_input = int(
        input('Enter number of road, 0 - track, 1 - dirt road: '))
    print(win_number, user_input)
    if user_input == win_number:
        paint_pictures()
    else:
        paint_pictures(False)






