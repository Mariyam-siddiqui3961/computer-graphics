import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
import math 
 
# Initialize Pygame 
pygame.init() 
 
# Set up display 
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("OpenGL Primitives with GL_POINTS") 
 
# Initialize Orthographic projection 
def init_ortho(): 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    gluOrtho2D(0, screen_width, 0, screen_height) 
 
# Function to draw a circle using GL_POINTS 
def draw_circle(center_x, center_y, radius): 
    glBegin(GL_POINTS) 
    for angle in range(360): 
        rad = math.radians(angle) 
        x = center_x + radius * math.cos(rad) 
        y = center_y + radius * math.sin(rad) 
        glVertex2f(x, y) 
    glEnd() 
 
# Function to draw a rectangle using GL_POINTS 
def draw_rectangle(x, y, width, height): 
    glBegin(GL_POINTS) 
    for i in range(int(x), int(x + width)): 
        glVertex2f(i, y) 
        glVertex2f(i, y + height) 
    for j in range(int(y), int(y + height)): 
        glVertex2f(x, j) 
        glVertex2f(x + width, j) 
    glEnd() 
 
# Function to draw an arc using GL_POINTS 
def draw_arc(center_x, center_y, radius, start_angle, end_angle): 
    glBegin(GL_POINTS) 
    for angle in range(start_angle, end_angle + 1): 
        rad = math.radians(angle) 
        x = center_x + radius * math.cos(rad) 
        y = center_y + radius * math.sin(rad) 
        glVertex2f(x, y) 
    glEnd() 
 
# Function to draw an ellipse using GL_POINTS 
def draw_ellipse(center_x, center_y, radius_x, radius_y): 
    glBegin(GL_POINTS) 
    for angle in range(360): 
        rad = math.radians(angle) 
        x = center_x + radius_x * math.cos(rad) 
        y = center_y + radius_y * math.sin(rad) 
        glVertex2f(x, y) 
    glEnd() 
 
# Function to divide the screen and draw shapes 
def draw_primitives(): 
    # Top-left quadrant: Circle 
    glViewport(0, screen_height // 2, screen_width // 2, screen_height // 2) 
    glColor3f(1.0, 0.0, 0.0)  # Red 
    draw_circle(screen_width // 4, screen_height // 4, 100) 
 
    # Top-right quadrant: Rectangle 
    glViewport(screen_width // 2, screen_height // 2, screen_width // 2, screen_height // 2) 
    glColor3f(0.0, 1.0, 0.0)  # Green 
    draw_rectangle(screen_width // 4, screen_height // 4, 200, 100) 
 
    # Bottom-left quadrant: Arc 
    glViewport(0, 0, screen_width // 2, screen_height // 2) 
    glColor3f(0.0, 0.0, 1.0)  # Blue 
    draw_arc(screen_width // 4, screen_height // 4, 100, 0, 180) 
 
    # Bottom-right quadrant: Ellipse 
    glViewport(screen_width // 2, 0, screen_width // 2, screen_height // 2) 
    glColor3f(1.0, 1.0, 0.0)  # Yellow 
    draw_ellipse(screen_width // 4, screen_height // 4, 150, 75) 
 
done = False 
init_ortho() 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    glPointSize(2) 
    draw_primitives() 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()