import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
 
# Initialize Pygame 
pygame.init() 
 
# Set up display 
screen_width = 1000 
screen_height = 800 
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("OpenGL in Python") 
 
# Initialize Orthographic projection 
def init_ortho(): 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(0, screen_width, 0, screen_height) 
     
 
# Function to draw primitives 
def draw_primitives(): 
    glPointSize(5) 
 
    # Draw Points 
    glBegin(GL_POINTS) 
    glColor3f(1.0, 0.0, 0.0)  # Red 
    glVertex2i(100, 50) 
    glVertex2i(630, 450) 
    glEnd() 
 
    # Draw Lines 
    glBegin(GL_LINES) 
    glColor3f(0.0, 1.0, 0.0)  # Green 
    glVertex2i(200, 150) 
    glVertex2i(400, 150) 
    glEnd() 
 
    # Draw Triangles 
    glBegin(GL_TRIANGLES) 
    glColor3f(0.0, 0.0, 1.0)  # Blue 
    glVertex2i(500, 100) 
    glVertex2i(600, 300) 
    glVertex2i(700, 100) 
    glEnd() 
 
    # Draw Quads 
    glBegin(GL_QUADS) 
    glColor3f(1.0, 1.0, 0.0)  # Yellow 
    glVertex2i(100, 500) 
    glVertex2i(300, 500) 
    glVertex2i(300, 700) 
    glVertex2i(100, 700) 
    glEnd() 
 
    # Draw Polygon (Pentagon) 
    glBegin(GL_POLYGON) 
    glColor3f(1.0, 0.0, 1.0)  # Magenta 
    glVertex2i(500, 500) 
    glVertex2i(550, 600) 
    glVertex2i(650, 600) 
    glVertex2i(700, 500) 
    glVertex2i(600, 450) 
    glEnd() 
 
done = False 
init_ortho() 
     
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    glPointSize(5) 
    draw_primitives() 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()