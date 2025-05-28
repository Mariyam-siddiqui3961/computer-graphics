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
pygame.display.set_caption("Drawing rectangle with user input") 
 
# Initialize Orthographic projection 
def init_ortho(): 
    glMatrixMode(GL_PROJECTION) 
    gluOrtho2D(0, screen_width, 0, screen_height) 
     
 
# Function to draw line 
 
def draw_line_dda(x1, y1, x2, y2): 
    dx = x2 - x1 
    dy = y2 - y1 
    steps = int(max(abs(dx), abs(dy))) 
    x_increment = dx / steps 
    y_increment = dy / steps 
 
    x = x1 
    y = y1 
    glBegin(GL_POINTS) 
    glVertex2i(round(x), round(y)) 
 
    for _ in range(steps): 
        x += x_increment 
        y += y_increment 
        glVertex2i(round(x), round(y)) 
    glEnd() 
 
done = False 
init_ortho() 
   
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glPointSize(5) 
    draw_line_dda(100,200,600,400) 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()