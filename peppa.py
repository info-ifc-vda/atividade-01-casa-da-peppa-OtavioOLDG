import glfw
from OpenGL.GL import *
import math

def init():
    glClearColor(1,0.5,1,1)

def draw_circle(x, y, radius, red, green, blue):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(red, green, blue)
    glVertex2f(x, y) # Centro do círculo
    num_segments = 100 # Quanto maior, mais "redonda" a bola
    for i in range(num_segments + 1):
        theta = 2.0 * 3.1415926 * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    

    glBegin(GL_QUADS)
    glColor3f(0, 0, 1) # Cor azul para a base
    glVertex2f(-0.6, -1)
    glVertex2f(0.6, -1)
    glVertex2f(0.6, 0)
    glVertex2f(-0.6, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0) # Cor azul para a base
    glVertex2f(-0.8,-0.2)
    glVertex2f(0.8,-0.2)
    glVertex2f(0,0.7)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0) # Cor azul para a base
    glVertex2f(-0.1, -1)
    glVertex2f(0.1, -1)
    glVertex2f(0.1, -0.6)
    glVertex2f(-0.1, -0.6)
    glEnd()

    draw_circle(0.6, 0.7, 0.15, 1, 1, 0) # Bolinha amarela no céu
    draw_circle(0.08, -0.8, 0.01, 1, 1, 1) # Bolinha amarela no céu



def main():
    glfw.init()
    window = glfw.create_window(800, 600, 'Teste', None, None)
    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__" :
    main()
