import pygame, sys
from pygame import mixer_music
from pygame import mixer
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import os
import time
import numpy as np


            
class Pathfinder:
    def __init__(self,matrix):
        
        # setup
        self.matrix = matrix
        self.grid = Grid(matrix = matrix)
        self.select_surf = pygame.image.load('selection.png').convert_alpha()
        
        #PATHFINDING
        self.path = []
        
    def draw_active_cell(self):
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // (28)
        col = mouse_pos[0] // (28)
        current_cell_value = self.matrix[row][col]
        
        if current_cell_value == 1:
            rect = pygame.Rect((col*(28), row*(28)),((28),(28)))
            screen.blit(self.select_surf,rect)
    
    def create_path(self):
        #start
        start_x, start_y = [0,21]
        start = self.grid.node(start_x,start_y)
        
        #end
        mouse_pos = pygame.mouse.get_pos()
        end_x, end_y = mouse_pos[0] // (28), mouse_pos[1] // (28) 
        end = self.grid.node(end_x, end_y)
        
         #path
        finder = AStarFinder()
        self.grid.cleanup()
        self.path,_ = finder.find_path(start, end, self.grid)
        print (self.path)

        

    def update(self):
        self.draw_active_cell()

pygame.init()
screen = pygame.display.set_mode((504,616))
clock = pygame.time.Clock()

start = (0,21)
end = ()

#game setup
bg_surf = pygame.image.load('map.png').convert()
matrix = [
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,]
]
pathfinder = Pathfinder(matrix)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("Calculating Path...")
            #os.system('cls')
            os.system('echo Calculating Path...\n')
            time.sleep(.25)
            #os.system('echo Starting at {} and ending at {}\n'.format(start, end))
            time.sleep(.25)
            pathfinder.create_path()
            os.system('echo Done!\n')
        
            
    screen.blit(bg_surf,(0,0))
    pathfinder.draw_active_cell()
    pygame.display.update()
    clock.tick(60)