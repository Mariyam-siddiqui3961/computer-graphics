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
# Define the square's vertices in homogeneous coordinates 
square_vertices = np.array([ 
[200, 200, 1.0], 
[300, 200, 1.0], 
[300, 300, 1.0], 
[200, 300, 1.0] 
], dtype=np.float32) 
# Transformation parameters 
translate_x = 0.0 
translate_y = 0.0 
rotation_angle = 0.0  # in degrees 
scale_factor = 1.0 
 
def create_translation_matrix(tx, ty): 
    """Create a 3x3 translation matrix.""" 
    return np.array([ 
        [1.0, 0.0, tx], 
        [0.0, 1.0, ty], 
        [0.0, 0.0, 1.0] 
    ], dtype=np.float32) 
 
def create_rotation_matrix(angle_degrees): 
    """Create a 3x3 rotation matrix.""" 
    angle_radians = math.radians(angle_degrees) 
    cos_a = math.cos(angle_radians) 
    sin_a = math.sin(angle_radians) 
    return np.array([ 
        [cos_a, -sin_a, 0.0], 
        [sin_a,  cos_a, 0.0], 
        [0.0,    0.0,   1.0] 
    ], dtype=np.float32) 
 
def create_scaling_matrix(s): 
    """Create a 3x3 scaling matrix.""" 
    return np.array([ 
        [s,   0.0, 0.0], 
        [0.0, s,   0.0], 
        [0.0, 0.0, 1.0] 
    ], dtype=np.float32) 
 
def apply_transformation(vertices, matrix): 
    """Apply a transformation matrix to a set of vertices.""" 
    return np.dot(vertices, matrix.T) 
 
# Function to draw square 
def draw_square(vertices): 
    """Render the square using the transformed vertices.""" 
    glBegin(GL_QUADS) 
    glColor3f(0.0, 1.0, 0.0)  # Green color 
    for vertex in vertices: 
        glVertex2f(vertex[0], vertex[1]) 
    glEnd() 
 
done = False 
init_ortho() 
   
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
                elif event.key == pygame.K_r: 
                    rotation_angle += 5.0  # Rotate 5 degrees 
                elif event.key == pygame.K_e: 
                    rotation_angle -= 5.0  # Rotate -5 degrees 
                elif event.key == pygame.K_s: 
                    scale_factor += 1.5 
                 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW) 
    glPointSize(5) 
    # Create transformation matrices 
    translation_matrix = create_translation_matrix(translate_x, translate_y) 
    rotation_matrix = create_rotation_matrix(rotation_angle) 
    scaling_matrix = create_scaling_matrix(scale_factor) 
 
    # Combine transformations: Translation * Rotation * Scaling 
    transformation_matrix = np.dot(translation_matrix, np.dot(rotation_matrix, scaling_matrix)) 
 
    # Apply the combined transformation to the square's vertices 
transformed_vertices = apply_transformation(square_vertices, transformation_matrix) 
# Draw the transformed square 
draw_square(transformed_vertices) 
pygame.display.flip() 
pygame.time.wait(100) 
pygame.quit() 