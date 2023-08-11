from enum import Enum, auto
from typing import Union
import random

class Board:
    
    def __init__(self, height: int = 10, width: int = 10):
        self.height = height
        self.width = width
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    
    def get(self, row, col):
        return self.grid[row][col]
        
    def set(self, row, col, val):
        self.grid[row][col] = val
    
    def get_8_neighbours(self, row, col):
        neighbors = []
        for dr, di in [(1, 1),
                       (0, 1),
                       (-1, 1),
                       (-1, 0),
                       (-1, -1),
                       (0, -1),
                       (1, -1),
                       (1, 0)
                       ]:
            if self.point_in_board(row + dr, col+di):
                neighbors.append((row + dr, col+di))
        return neighbors
    
    def point_in_board(self, row, col):
        if row < 0 or self.height <= row:
            return False
        if col < 0 or self.width <= col:
            return False
        return True
        

class SpecialCell(Enum):
    MINE = auto()

ViewCELL = Union[int, SpecialCell]

class MaskCell:
    OPEN = auto()
    COVERED = auto()    

class Player:
    
    def __init__(self):
        self.info = None
    
    def update_info(self,  new_info)
    
class MineField:
    
    def __init__(self, height: int = 10, width: int = 10) -> None:
        self.board = Board(height=height, width=width)
    
    def clear_board(self):
        for row in range(self.board.height):
            for col in range(self.board.width):
                self.board.set(row, col, 0)
    
    def init_board(self, num_mines: int):
        self.clear_board()
        mine_points = []
        for i in range(num_mines):
            point = (random.randint(0, self.board.height-1),
                     random.randint(0, self.board.width-1)
                     )
            if point in mine_points:
                continue
            else:
                mine_points.append(point)
        # Put out mines
        for row, col in mine_points:
            self.board.set(row,col, SpecialCell.MINE)
        # Label res
        for row in range(self.board.height):
            for col in range(self.board.width):
                if self.board.get(row, col) == SpecialCell.MINE:
                    continue
                num_surrounding_mines = 0
                for n_row, n_col in self.board.get_8_neighbours(row, col):
                    if self.board.get(n_row, n_col) == SpecialCell.MINE:
                        num_surrounding_mines += 1
                self.board.set(row, col, num_surrounding_mines)
    
    def print_internal_board(self):
        for row in range(self.board.height):
            row_str = ''
            for col in range(self.board.width):
                if self.board.get(row, col) == SpecialCell.MINE:
                    row_str = row_str + '@'
                else:
                    row_str = row_str + str(self.board.get(row, col))
            print(row_str) 



        
        
game = MineField()
game.init_board(5)

game.print_internal_board()
player = Player(()





