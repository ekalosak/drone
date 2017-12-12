# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#guide-gl
# http://www.natan.termitnjak.net/tutorials/pyglet_basic.html

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *

from resources import vertices, colors, surfaces, edges

window = pyglet.window.Window(800, 600)

# @window.event
# def on_show():
#     pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT)
#     # Set up projection matrix.
#     pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
#     pyglet.gl.glLoadIdentity()
#     pyglet.gl.gluPerspective(
#             46.0,
#             float(cubeWindow.width)/cubeWindow.height,
#             0.1,
#             360)


@window.event
def on_draw():
    window.clear()

def update(dt):
    pass

# window.push_handlers(pyglet.window.event.WindowEventLogger())

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 0.5)
    pyglet.app.run()
