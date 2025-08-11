from algorithms import bubble_sort, merge_sort, quick_sort, insertion_sort
from sorting_visualizer import sorting_visualizer
from pathfinding_visualizer import pathfinding_visualizer
from maze import maze,cell,Direction
import random
import sys

#LIST_SIZE = 200

def main(sort,list_size):
    list = [i for i in range(1,list_size+1)]
    random.shuffle(list)
    sv = sorting_visualizer(list)

    if sort=="insertion":
        insertion_sort.sort(sv)
    elif sort=="quick":
        quick_sort.sort(sv)
    elif sort=="merge":
        merge_sort.sort(sv)
    elif sort=="bubble":
        bubble_sort.sort(sv)
    else:
        print("Faulty first arguement")
    sv.display(5)
    print(sv.list)

def main2(list_size):
    width =list_size
    height = width
    maze_cells = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(width):
        for j in range(height):
            maze_cells[i][j] = cell([],(i,j))
    maze2 = maze(maze_cells,width,height)
    maze2.generate((0,0))
    pv = pathfinding_visualizer(maze2)
    pv.display_maze()
    while(True):
        print



if __name__ == "__main__":
    if len(sys.argv)==3:
        main(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv)==2:
        main2(int(sys.argv[1]))
