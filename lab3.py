import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
import math 
 
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
     
 
def draw_circle(center_x, center_y, radius, color): 
    glColor3f(*color) 
    glBegin(GL_TRIANGLE_FAN) 
    glVertex2f(center_x, center_y)  # Center of circle 
    for angle in range(361): 
        x = center_x + math.cos(math.radians(angle)) * radius 
        y = center_y + math.sin(math.radians(angle)) * radius 
        glVertex2f(x, y) 
    glEnd() 
 
def draw_ellipse(center_x, center_y, radius_x, radius_y, color): 
    glColor3f(*color) 
    glBegin(GL_TRIANGLE_FAN) 
    glVertex2f(center_x, center_y)  # Center of ellipse 
    for angle in range(361): 
        x = center_x + math.cos(math.radians(angle)) * radius_x 
        y = center_y + math.sin(math.radians(angle)) * radius_y 
        glVertex2f(x, y) 
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
    draw_circle(400,500,50, (1,0,0)) 
    draw_circle(375,525,10, (0,0,0)) 
    draw_circle(425,525,10, (0,0,0)) 
    draw_ellipse(400,500,5,10, (0,1,0)) 
    draw_ellipse(400,475,20,5, (0,1,0)) 
    draw_ellipse(400,350,200,75,(1,0,1)) 
    draw_ellipse(400,350,50,100,(0,0,1)) 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()