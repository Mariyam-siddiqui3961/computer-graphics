import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
import numpy as np 
import math 
# Initialize Pygame 
pygame.init() 
# Set up display 
screen_width = 1000 
screen_height = 800 
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("applying transformations") 
# Initialize Orthographic projection 
def init_ortho(): 
    glMatrixMode(GL_PROJECTION) 
    gluOrtho2D(0, screen_width, 0, screen_height) 
# Define the house-like shape (base + roof) 
    house_vertices = np.array([ 
    [300, 200, 1.0],  # Bottom-left 
    [300, 300, 1.0],  # Top-left 
    [400, 400, 1.0],  # Roof peak 
    [500, 300, 1.0],  # Top-right 
    [500, 200, 1.0]   # Bottom-right 
    ], dtype=np.float32) 
    # Transformation parameters 
    translate_x = 0.0 
    translate_y = 0.0 
    scale_factor = 1.0 
    ref_point = np.array([400, 300, 1.0], dtype=np.float32)  # Arbitrary point 
def create_translation_matrix(tx, ty): 
"""Create a 3x3 translation matrix.""" 
    return np.array([ 
        [1.0, 0.0, tx], 
        [0.0, 1.0, ty], 
        [0.0, 0.0, 1.0] 
    ], dtype=np.float32) 
 
def create_scaling_matrix(sx,sy): 
    """Create a 3x3 scaling matrix.""" 
    return np.array([ 
        [sx,   0.0, 0.0], 
        [0.0, sy,   0.0], 
        [0.0, 0.0, 1.0] 
    ], dtype=np.float32) 
 
def create_scaling_about_point_matrix(sx, sy, px, py): 
    to_origin = create_translation_matrix(-px, -py) 
    scaling = create_scaling_matrix(sx, sy) 
    back = create_translation_matrix(px, py) 
    return np.dot(back, np.dot(scaling, to_origin)) 
 
def apply_transformation(vertices, matrix): 
    """Apply a transformation matrix to a set of vertices.""" 
    return np.dot(vertices, matrix.T) 
 
# Function to draw house 
def draw_house(vertices, color=(1.0, 1.0, 1.0)): 
    glColor3f(*color) 
    glBegin(GL_POLYGON) 
    for vertex in vertices: 
        glVertex2f(vertex[0], vertex[1]) 
    glEnd() 
 
done = False 
init_ortho() 
scaling_about_origin = True  # Toggle between modes 
 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    translate_x -= 10 
                elif event.key == pygame.K_RIGHT: 
                    translate_x += 10 
                elif event.key == pygame.K_DOWN: 
                    translate_y -= 10 
                elif event.key == pygame.K_UP: 
                    translate_y += 10 
                elif event.key == pygame.K_s: 
                    scale_factor += 0.2 
                elif event.key == pygame.K_d: 
                    scale_factor -=0.2 
                elif event.key == pygame.K_t: 
                    scaling_about_origin = not scaling_about_origin  # Toggle 
                 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glPointSize(5) 
 
    if scaling_about_origin: 
        # Scaling about origin followed by translation 
        scale_matrix = create_scaling_matrix(scale_factor, scale_factor) 
        translate_matrix = create_translation_matrix(translate_x, translate_y) 
        transform = np.dot(translate_matrix, scale_matrix) 
        color = (1.0, 0.0, 0.0)  # Red 
 
    else: 
        # Scaling about arbitrary point 
        transform = create_scaling_about_point_matrix(scale_factor, scale_factor, ref_point[0], 
ref_point[1]) 
        color = (0.0, 0.0, 1.0)  # Blue 
 
    # Apply the combined transformation to the square's vertices 
    transformed_vertices = apply_transformation(house_vertices, transform) 
 
    # Draw the transformed square 
    draw_house(transformed_vertices, color) 
    pygame.display.flip() 
    pygame.time.wait(100) 
 
pygame.quit()