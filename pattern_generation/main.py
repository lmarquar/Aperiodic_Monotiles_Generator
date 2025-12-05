import sys
from pattern_generator import *
from graphics_tk import draw_tiles

SCALAR = 1
ITERATIONS = 7  # more than 8 might break
COLORQUINTETT = "black", "seagreen", "White", "sandybrown", "sandybrown"

colors = [5]
scalar = SCALAR
colorqintett = COLORQUINTETT
iterations = ITERATIONS
i = 1
# if (i < len(sys.argv)) and sys.argv[i].isnumeric:
#     scalar = int(sys.argv[i])
# for i in range(len(sys.argv)):
#     if (sys.argv[i].isnumeric):


for i in range(iterations):
    next_generation(colorqintett)
s = draw_tiles(vertices_to_draw, width=5000, height=5000,
               scalar=scalar, show_window=False)
print(s)
