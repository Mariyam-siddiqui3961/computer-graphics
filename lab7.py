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
def plot_circle_points(xc, yc, x, y): 
    # Plot the eight symmetric points 
    glBegin(GL_POINTS) 
    glVertex2i(xc + x, yc + y) 
    glVertex2i(xc - x, yc + y) 
    glVertex2i(xc + x, yc - y) 
    glVertex2i(xc - x, yc - y) 
    glVertex2i(xc + y, yc + x) 
    glVertex2i(xc - y, yc + x) 
    glVertex2i(xc + y, yc - x) 
    glVertex2i(xc - y, yc - x) 
    glEnd() 
 
def midpoint_circle(xc, yc, r): 
    x = 0 
    y = r 
    d = 1 - r 
    plot_circle_points(xc, yc, x, y) 
    while x < y: 
        x += 1 
        if d < 0: 
            d += 2 * x + 1 
        else: 
            y -= 1 
            d += 2 * (x - y) + 1 
        plot_circle_points(xc, yc, x, y) 
 
done = False 
init_ortho() 
   
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glPointSize(5) 
    midpoint_circle(400,500,50) 
    midpoint_circle(400,500,150) 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit() 