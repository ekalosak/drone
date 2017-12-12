# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#guide-gl
# http://www.natan.termitnjak.net/tutorials/pyglet_basic.html

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *

from resources import vertices, colors, surfaces, edges, win_sz

window = pyglet.window.Window(*win_sz)
box_x, box_y, box_z = 0, 0, 0

@window.event
def on_show():
    print("setting up window...")
    pyglet.gl.glClear(
            pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT
            )
    # Set up projection matrix.
    pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
    pyglet.gl.glLoadIdentity()
    pyglet.gl.gluPerspective(
            46.0,
            float(window.width)/window.height,
            0.1,
            360)

@window.event
def on_draw():
    window.clear()

def update(dt):
    print("update loop")
    #TODO move box here

@window.event
def on_key_press(symbol, modifiers):

    global box_x, box_y, box_z
    if symbol == key.LEFT:
        pass
    elif symbol == key.RIGHT:
        pass
    elif symbol == key.UP:
        pass
    elif symbol == key.DOWN:
        pass
    elif symbol == key.SPACE:
        print("space, screenshotting")
        pyglet.image.get_buffer_manager().get_color_buffer().save(
                'screenshot.png')

# window.push_handlers(pyglet.window.event.WindowEventLogger())

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 0.5)
    pyglet.app.run()
