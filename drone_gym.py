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

from resources import vertices, surfaces, win_sz, colors, cube_sz, floor_sz,\
    floor_verts

INCREMENT = 15

class Window(pyglet.window.Window):

    xRotation = yRotation = 0 # initial cube rotations
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
        glRotatef(self.yRotation, 0, 1, 0)

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
            self.yRotation += INCREMENT
        elif symbol == key.L:
            self.yRotation -= INCREMENT




def main():
    # pyglet.clock.schedule_interval(update, 0.5)
    window = Window(*win_sz, 'Drone AI Gym')
    window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()

if __name__ == '__main__':
    main()
