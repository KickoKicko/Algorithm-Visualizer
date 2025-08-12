import pathfinding_visualizer
from maze import maze,cell,Direction
import time

def pathfind(pv,start_pos):
    queue = []
    queue.append(pv.maze.cells[start_pos[0]][start_pos[1]])
    pv.maze.cells[start_pos[0]][start_pos[1]].visited = True
    while len(queue)!=0:
        current_cell = queue.pop(len(queue)-1)
        pv.display_whole_maze()
        pv.draw_body(current_cell)
        if current_cell.coordinates == (pv.maze.width-1,pv.maze.height-1):
            break
        for d in current_cell.directions:
            if d==Direction.UP:
                new_cell=pv.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1]
                if(new_cell.visited):
                    continue
                new_cell.visited = True
                new_cell.previous = current_cell
                queue.append(new_cell)
            elif d==Direction.RIGHT:
                new_cell=pv.maze.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]]
                if(new_cell.visited):
                    continue
                new_cell.visited = True
                new_cell.previous = current_cell
                queue.append(new_cell)
            elif d==Direction.DOWN:
                new_cell=pv.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1]
                if(new_cell.visited):
                    continue
                new_cell.visited = True
                new_cell.previous = current_cell
                queue.append(new_cell)
            elif d==Direction.LEFT:
                new_cell=pv.maze.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]]
                if(new_cell.visited):
                    continue
                new_cell.visited = True
                new_cell.previous = current_cell
                queue.append(new_cell)
    

