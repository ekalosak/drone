
#         # White
#         glColor3ub(255, 255, 255)
#         glVertex3f(50,50,50)

#         # Yellow
#         glColor3ub(255, 255, 0)
#         glVertex3f(50,-50,50)

#         # Red
#         glColor3ub(255, 0, 0)
#         glVertex3f(-50,-50,50)
#         glVertex3f(-50,50,50)

#         # Blue
#         glColor3f(0, 0, 1)
#         glVertex3f(-50,50,-50)


# @window.event
# def on_show():
#     print("setting up window...")
#     pyglet.gl.glClear(
#             pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT
#             )
#     # Set up projection matrix.
#     pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
#     pyglet.gl.glLoadIdentity()
#     pyglet.gl.gluPerspective(
#             46.0,
#             float(window.width)/window.height,
#             0.1,
#             360)

# @window.event
# def on_draw():
#     glClear(GL_COLOR_BUFFER_BIT)
#     glLoadIdentity()
#     # glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 2)
#     glBegin(GL_POINTS)
#     glVertex2i(50, 50)
#     glVertex2i(75, 100)
#     glVertex2i(100, 150)
#     glEnd()

# def update(dt):
#     print("update loop")
#     #TODO move camera here

# @window.event
# def on_key_press(symbol, modifiers):
#     #TODO take input and prep for camera move here

#     global box_x, box_y, box_z
#     if symbol == key.LEFT:
#         pass
#     elif symbol == key.RIGHT:
#         pass
#     elif symbol == key.UP:
#         pass
#     elif symbol == key.DOWN:
#         pass
#     elif symbol == key.SPACE:
#         print("space, screenshotting")
#         pyglet.image.get_buffer_manager().get_color_buffer().save(
#                 'screenshot.png')
