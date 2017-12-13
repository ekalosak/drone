# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#guide-gl
# http://www.natan.termitnjak.net/tutorials/pyglet_basic.html
# https://www.packtpub.com/books/content/creating-amazing-3d-guis-pyglet

import pdb
import pyglet

from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *
from OpenGL.GLUT import *

from resources import vertices, surfaces, win_sz, colors, cube_sz

INCREMENT = 5

class Window(pyglet.window.Window):
    # Cube 3D start rotation
    xRotation = yRotation = 30

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

    def on_draw(self):
        self.clear()
        glPushMatrix() # push mx onto stack

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # BEGIN: Draw the cube
        glBegin(GL_QUADS)

        color = colors['green']
        surface = surfaces[0]
        # for surface in surfaces:
        for vert_ix in surface:
            vert_coords = [a*cube_sz for a in vertices[vert_ix]]
            glColor3ub(*color)
            glVertex3f(*vert_coords)

        glEnd()
        # END: Draw cube

        glPopMatrix()

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.xRotation -= INCREMENT
        elif symbol == key.DOWN:
            self.xRotation += INCREMENT
        elif symbol == key.LEFT:
            self.yRotation -= INCREMENT
        elif symbol == key.RIGHT:
            self.yRotation += INCREMENT

        elif symbol == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save(
                    'screenshot.png')

# window.push_handlers(pyglet.window.event.WindowEventLogger())

if __name__ == '__main__':
    # pyglet.clock.schedule_interval(update, 0.5)
    Window(*win_sz, 'Pyglet Colored Cube')
    pyglet.app.run()
