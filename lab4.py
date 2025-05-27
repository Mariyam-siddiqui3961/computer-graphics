import numpy as np 
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
ortho_left = 0 
ortho_right = 1000 
ortho_top = 800 
ortho_bottom = 0 
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("Rectangle in opengl") 
 
# Initialize Orthographic projection 
def init_ortho(): 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(ortho_left, ortho_right, ortho_bottom, ortho_top) 
 
def map_value(current_min, current_max, new_min, new_max, value): 
    current_range = current_max - current_min 
    new_range = new_max - new_min 
    return new_min + new_range * ((value - current_min) / current_range) 
 
def plot_rect(): 
    glColor(0,1,0,1) 
    glBegin(GL_QUADS) 
    for p in points: 
        glVertex2f(p[0], p[1]) 
    glEnd() 
    glColor(1,0,0,1) 
    for i in np.arange(0,len(points)-3,4): 
        glBegin(GL_LINE_LOOP)  
        glVertex2f(points[i][0], points[i][1]) 
        glVertex2f(points[i+1][0], points[i+1][1]) 
        glVertex2f(points[i+2][0], points[i+2][1]) 
        glVertex2f(points[i+3][0], points[i+3][1]) 
        glEnd() 
 
done = False 
init_ortho() 
points = [] 
glLineWidth(3)     
while not done: 
    p=None 
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == MOUSEBUTTONDOWN: 
                p = pygame.mouse.get_pos() 
                points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]), 
                           map_value(0, screen_height, ortho_top, ortho_bottom, p[1]))) 
             
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    plot_rect() 
    pygame.display.flip() 
pygame.quit()