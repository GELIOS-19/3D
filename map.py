# map

from settings import *

# w for wall tile, . for empty tile
tile_map = [
    "WWWWWWWWWWWW",
    "W..........W",
    "W.WW..WWWW.W",
    "WW.....W.W.W",
    "W..WWW...W.W",
    "W.WW.WWWWW.W",
    "W..W.......W",
    "WWWWWWWWWWWW",
]

world_map = set()
for j, row in enumerate(tile_map):
    for i, char in enumerate(row):
        if char == "W":
            world_map.add((i * TILE, j * TILE))
