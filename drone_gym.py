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
# import pyshaders as shaders

from resources import vertices, surfaces, win_sz, colors, cube_sz

INCREMENT = 12

class Window(pyglet.window.Window):

    xRotation = yRotation = 30 # initial cube rotations
    xTrans = yTrans = 0 # initial cube translations

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title,
                resizable=True)
        # glClearColor(0, 0, 0, 1)
        # Load shaders
        # shader = shaders.from_files_names('main.glsl.vert', 'main.glsl.frag')
        # shader.use()
        # shader.enable_all_attributes()
        # shader.owned = False
        # self.shader = shader
        # glEnable(GL_DEPTH_TEST)

    def on_draw(self):
        self.clear()
        glPushMatrix() # push mx onto stack

        # glRotatef(self.xRotation, 1, 0, 0)
        # glRotatef(self.yRotation, 0, 1, 0)

        glTranslatef(self.xTrans, 1, 0)
        glTranslatef(0, self.yTrans, 0)

        # BEGIN: Draw the cubes
        glBegin(GL_QUADS)

        cs = [colors['red'], colors['blue']]
        i = 0
        for surface in surfaces:
            for vert_ix in surface:
                vert_coords = [a*cube_sz for a in vertices[vert_ix]]
                color = cs[i]
                i = (i + 1) %len(cs)
                glColor3ub(*color)
                glVertex3f(*vert_coords)

        cs = [colors['green'], colors['blue']]
        for surface in surfaces:
            for vert_ix in surface:
                vert_coords = [a*cube_sz - 75 for a in vertices[vert_ix]]
                color = cs[i]
                i = (i + 1) %len(cs)
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

    def on_text_motion(self, motion):

        if motion == key.UP:
            self.xRotation -= INCREMENT
            self.yTrans -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
            self.yTrans += INCREMENT

        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
            self.xTrans -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT
            self.xTrans += INCREMENT

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save(
                    'screenshot.png')
        elif symbol == key.ESCAPE:
            exit(0)

def main():
    # pyglet.clock.schedule_interval(update, 0.5)
    window = Window(*win_sz, 'Drone AI Gym')
    # window.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()

if __name__ == '__main__':
    main()
