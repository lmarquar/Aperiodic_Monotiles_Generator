# Aperiodic_Monotiles_Generator
ultimatly it should be a website, where Users can adjust coloring, size, image_size, type-of-tile and download an image file. This way everyone can create designs with it!

## How to use:
 - install python tkinter package if you haven't already: `sudo apt install python3-tk`
 - configure main.py to your liking
 - run it and see results!

## Seed to Pattern Generation (copied)
This part of the program is able to generate an image from the pattern based on a seed. Each seed corresponds to a unique coordinate on the x-y plane and when I give the program a seed it zooms into that coordinate and outputs the image that it zoomed into. The algorithm that converts the seed to a coordinate is in the `seed_to_pattern.py` file. The seeds go in a spiral, starting from the top right and going clockwise increasing the layer every loop. This means that for each seed you will get a unique part of the pattern. But since this is an aperiodic pattern that does not mean that each image will be unique because parts of the pattern do repeat.

To run this you need the files `pattern_generator.py`, `geometry.py`, `graphics_cv2.py`, and `seed_to_pattern.py`. To launch the program run `seed_to_pattern.py` using: 

`python3 seed_to_pattern.py` 

You can specify the seed to generate at the bottom of the program in the function "seed_to_pattern". The program will output the image as a file in the same directory that it is in.

## References: 
- David Smith (amateur mathematician and Inventor of this pattern): https://cs.uwaterloo.ca/~csk/hat/
- Alexander Smolyanskiy: (forked repository for a python program which i wil base the backend on [https://github.com/lmarquar/Einstein_Tile_Generator_img])