# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#guide-gl
# http://www.natan.termitnjak.net/tutorials/pyglet_basic.html
# https://www.packtpub.com/books/content/creating-amazing-3d-guis-pyglet
# https://github.com/fogleman/Minecraft/blob/master/main.py

import pdb
import pyglet

from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
from OpenGL.GLUT import *

from resources import vertices, surfaces, colors, floor_verts,\
        win_sz, cube_sz, floor_sz

INCREMENT = 15

class Window(pyglet.window.Window):

    xRotation = -75
    zRotation = 0 # initial cube rotations
    xTrans = yTrans = 0 # initial cube translations

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title,
                resizable=True)
        # TODO see about shaders

    def Floor(self, color=colors['white'], size=floor_sz):
        for vert in floor_verts:
            vert_coords = [a*floor_sz for a in vert]
            glColor3ub(*color)
            glVertex3f(*vert_coords)

    def Cube(self, colors, size=cube_sz, x=0, y=0, z=0):
        i = 0
        for surface in surfaces:
            for vert_ix in surface:
                vert_coords = [a*cube_sz for a in vertices[vert_ix]]
                vert_coords[0] += x
                vert_coords[1] += y
                vert_coords[2] += z
                color = colors[i]
                i = (i + 1) %len(colors)
                glColor3ub(*color)
                glVertex3f(*vert_coords)

    def on_draw(self):
        self.clear()
        glPushMatrix() # push mx onto stack

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.zRotation, 0, 0, 1)

        glTranslatef(self.xTrans, 0, 0)
        glTranslatef(0, self.yTrans, 0)

        glBegin(GL_QUADS)

        self.Floor()
        self.Cube(colors=[colors['red']], x=2.5*cube_sz, y=2.5*cube_sz)
        self.Cube(colors=[colors['red']], x=-2.5*cube_sz, y=2.5*cube_sz)
        self.Cube(colors=[colors['green']])

        glEnd() # GL_QUADS

        glPopMatrix()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -800)

    def on_text_motion(self, motion):

        if motion == key.UP:
            self.yTrans += INCREMENT
        elif motion == key.DOWN:
            self.yTrans -= INCREMENT

        elif motion == key.LEFT:
            self.xTrans -= INCREMENT
        elif motion == key.RIGHT:
            self.xTrans += INCREMENT

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save(
                    'screenshot.png')
        elif symbol == key.ESCAPE:
            exit(0)

        elif symbol == key.J:
            self.xRotation += INCREMENT
        elif symbol == key.K:
            self.xRotation -= INCREMENT
        elif symbol == key.H:
            self.zRotation += INCREMENT
        elif symbol == key.L:
            self.zRotation -= INCREMENT


class Model(object):
    def __init__(self):
        # A Batch is a collection of vertex lists for batched rendering.
        self.batch = pyglet.graphics.Batch()

        # # A TextureGroup manages an OpenGL texture.
        # self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())

        # A mapping from position to the texture of the block at that position.
        # This defines all the blocks that are currently in the world.
        self.world = {}

        # Same mapping as `world` but only contains blocks that are shown.
        self.shown = {}

        # Mapping from position to a pyglet `VertextList` for all shown blocks.
        self._shown = {}

        # Mapping from sector to a list of positions inside that sector.
        self.sectors = {}

        # Simple function queue implementation. The queue is populated with
        # _show_block() and _hide_block() calls
        self.queue = deque()

        self._initialize()


def setup():
    """ Basic OpenGL configuration.
    https://github.com/fogleman/Minecraft/blob/master/main.py
    with modifications
    """
    # Set the color of "clear", i.e. the sky, in rgba.
    glClearColor(0.5, 0.69, 1.0, 1)
    # Enable culling (not rendering) of back-facing facets -- facets that aren't
    # visible to you.
    glEnable(GL_CULL_FACE)
    # Set the texture minification/magnification function to GL_NEAREST (nearest
    # in Manhattan distance) to the specified texture coordinates. GL_NEAREST
    # "is generally faster than GL_LINEAR, but it can produce textured images
    # with sharper edges because the transition between texture elements is not
    # as smooth."
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # setup_fog()

def main():
    # pyglet.clock.schedule_interval(update, 0.5)
    window = Window(*win_sz, 'Drone AI Gym')
    window.push_handlers(pyglet.window.event.WindowEventLogger())
    setup()
    pyglet.app.run()

if __name__ == '__main__':
    main()
