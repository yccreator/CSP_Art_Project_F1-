# SimpleGraphicsStarter
Starter code for creating a static image with Python's Tkinter canvas.

This repository contains two Python code files:
`simple_graphics.py`  and 
`my_picture.py`
which will be used for the generative art project

# simple_graphics.py
This is intended to function as a library or drawing API; it contains functions for drawing basic shapes, 
adjusting the state of the canvas tools (such as setting fill color, line thinkness, etc),
and helper functions for determining colors. 

## Examples of functions that adjust drawing state:
Call these before using the drawing functions.

```python
def set_fill_color(color_name):
    """Sets the inside color for shapes drawn after this point."""
    ...

def set_outline_color(color_name):
    """Sets the border color for shapes drawn after this point."""
    ...

def set_line_thickness(thickness):
    """Sets the thickness of lines and shape borders."""
    ...
```

## Example drawing functions
Call these with appropriate arguments. If you call this with an x or y coordinate that changes
inside the draw_frame() function (see below) you can create moving objects. 

```python

def fill_background(color_name):
    """Fills the entire canvas with one solid color."""
    ...

def draw_line(x1, y1, x2, y2):
    """Draws a line connecting point (x1, y1) to point (x2, y2)."""
   ...

def fill_circle(center_x, center_y, radius):
    """Draws a solid circle given its center point and radius."""
    ...

def draw_circle(center_x, center_y, radius):
    """Draws an empty circle outline given its center point and radius."""
    ...
```

Usage:  users should import this module into a separate script, such as my_picture.py
then use the functions inside a draw_frame function body. 

# my_picture.py
In this file you'll write the code to draw your scene or animation. Most changes should go
inside the draw_picture function, unless you're defining additional funtions or variables to help organize
the code.

If you would like to enhance the functionality of the drawing library, 
additional drawing functions should instead go into the other file: simple_graphics.py

```python
import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    triangle_height = height/5
    triangle_width = width / 3
    
    # Draw the tesselation
    # code for red triangles
    sg.set_fill_color(colors[0])
    
    # call fill
    sg.fill_circle(450, 50,50)
    
    sg.set_fill_color("#827e7e") # relatively dark gray
    sg. fill_triangle(300, 150, 400, 20, 350, 150)
    sg.set_fill_color("#c7c1c1") # lighter gray
    sg. fill_triangle(350, 150, 400, 20, 550, 150)
    
    sg.set_outline_color("black")
    sg.set_line_thickness(1)
    sg.draw_line(0, 150, 600, 150)
    
    # Define the points the curve should bend through
    river_points = [
        (100, 150), # Start point
        (300, 200), # Bends towards here
        (200, 350), # Bends back here
        (500, 500)  # End point
    ]

    sg.set_outline_color("blue")
    sg.set_line_thickness(8)
    sg.draw_curve(river_points)
    

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)

```
<img width="596" height="400" alt="image" src="https://github.com/user-attachments/assets/5c562afc-e346-4240-9a14-1bb0aaecab54" />


# Project Goals

In this project you'll create a static scene or animation (for animations, use the other starter code). 

You'll need to do the following:
- expand on the functionality of the library by adding additional functions for drawing and/or movement
- use the available functions to create your scene or animation 
