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
 
def draw_line_bresanham(x1, y1, x2, y2): 
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1) 
    p = 2*dy-dx 
    twoDy = 2*dy 
    twoDyDx = 2*(dy-dx) 
    if(x1>x2): 
        x = x2 
        y = y2 
        xend = x1 
    else: 
        x = x1 
        y = y1 
        xend = x2 
    glBegin(GL_POINTS) 
    glVertex2i(x,y) 
    while(x<xend): 
        x = x+1 
        if(p<0): 
            p+=twoDy 
        else: 
            y=y+1 
            p+=twoDyDx 
        glVertex2i(x,y)  
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
    draw_line_bresanham(100,200,600,400) 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()