import pygmae

import time

import sis

board[[0,0,0,0,0,0,0,0]
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0]]

class Piece:
    def __init__(self, team, type, image, killable):
        self.team = team
        self.type = type
        self.image = image
