# https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
# https://pyglet.readthedocs.io/en/latest/programming_guide/gl.html#guide-gl

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.gl import *

# from opengl_test import vertices, edges, colors, surfaces

vertices= (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        # (5,4),
        (5,7)
    )

assert(all([all([e2 < len(vertices) for e2 in e1]) for e1 in edges]))

colors = (
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (0,1,0),
        (1,1,1),
        (0,1,1),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,0,0),
        (1,1,1),
        (0,1,1),
    )

surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
    )


window = pyglet.window.Window(800, 600)

def Cube():
    glBegin(GL_QUADS)
    x = 1
    for surface in surfaces:
        # x = 0
        for vertex in surface:
            # x+=1
            glColor3fv(*colors[x])
            glVertex3fv(*vertices[vertex])
    glEnd()

@window.event
def on_draw():
    # glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0, 0)
    # glVertex2f(window.width, 0)
    # glVertex2f(window.width, window.height)
    # glEnd()

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glBegin(GL_QUADS)
    # for s in surfaces:
    #     for v in s:
    #         glVertex2f(*vertices[v])
    for v in surfaces[0]:
        glVertex2f(*vertices[v])

    # glBegin(GL_TRIANGLES)
    # glVertex2i(*(300,300))
    # glColor3f(*(0,1,0))
    # glVertex2i(400,200)
    # glColor3f(*(1,0,0))
    # glVertex2i(200,200)
    # glColor3f(*(0,0,1))
    # glEnd()

    # Cube()

# window.push_handlers(pyglet.window.event.WindowEventLogger())

if __name__ == '__main__':
    pyglet.app.run()
