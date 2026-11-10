from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from bird import Bird

boy = None
birds = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, birds

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    birds = [Bird(80 + i * 160, 180 + i * 40, 1 if i % 2 == 0 else -1)
             for i in range(10)]
    for bird in birds:
        game_world.add_oject(bird)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, birds
    game_world.clear()
    boy = None
    birds = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









