import colorsys
import random
import math
import tkinter as tk

# Internal state variables to track the "paintbrush"
_canvas = None
_fill_color = "black"
_outline_color = "black"
_line_thickness = 1

def start(draw_function, width=800, height=600):
    """Sets up the window and calls the student's drawing function."""
    global _canvas
    
    root = tk.Tk()
    root.title("Simple Graphics")
    root.resizable(False, False)
    
    # Create the drawing canvas
    _canvas = tk.Canvas(root, width=width, height=height, bg="white", highlightthickness=0)
    _canvas.pack()
    
    # Call the student's function, passing only the width and height
    draw_function(width, height)
    
    # Start the GUI loop
    root.mainloop()

# =====================================================================
# HELPER FUNCTIONS
# Use these functions in your code!
# You can add new functions here to draw more things
# =====================================================================

def map_value(value, start1, stop1, start2, stop2):
    """Re-maps a number from one range to another."""
    # Calculate how far the value is into the first range (as a percentage)
    percentage = (value - start1) / (stop1 - start1)
    # Apply that percentage to the second range
    return start2 + percentage * (stop2 - start2)


def hls_to_rgb_hex(h, l, s):
    """
    Converts HLS values (0.0 to 1.0) into a hex color string (e.g., '#ff0000').
    H: Hue (Color wheel position: 0.0 is red, 0.33 is green, 0.66 is blue).
    L: Lightness (0.0 is black, 0.5 is pure color, 1.0 is white).
    S: Saturation (0.0 is gray, 1.0 is fully vibrant).
    """
    # 1. colorsys does the complex math, returning RGB floats (0.0 to 1.0)
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    
    # 2. Convert the floats to integers from 0 to 255
    r_int = int(r * 255)
    g_int = int(g * 255)
    b_int = int(b * 255)
    
    # 3. Format them as a 2-digit hexadecimal string
    return f"#{r_int:02x}{g_int:02x}{b_int:02x}"


def rgb_hex_to_hls(hex_str):
    """Converts rgb hex string to hls value tuple, each in range 0.0 - 1.0
    H: Hue (Color wheel position: 0.0 is red, 0.33 is green, 0.66 is blue).
    L: Lightness (0.0 is black, 0.5 is pure color, 1.0 is white).
    S: Saturation (0.0 is gray, 1.0 is fully vibrant).
    """
    # Remove '#' if present
    hex_str = hex_str.lstrip('#')
    
    # Convert hex to RGB (0-255) then normalize to 0.0-1.0
    r, g, b = tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    
    # Convert RGB to HLS
    return colorsys.rgb_to_hls(r, g, b)

# =====================================================================
# DRAWING API FOR STUDENTS
# Use these functions in your code!
# You can add new functions here to draw more things
# =====================================================================

def set_fill_color(color_name):
    """Sets the inside color for shapes drawn after this point."""
    global _fill_color
    _fill_color = color_name
    
def random_color():
    """Returns a random hex color code like #A1B2C3."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"    

def set_outline_color(color_name):
    """Sets the border color for shapes drawn after this point."""
    global _outline_color
    _outline_color = color_name

def set_line_thickness(thickness):
    """Sets the thickness of lines and shape borders."""
    global _line_thickness
    _line_thickness = thickness

def fill_background(color_name):
    """Fills the entire canvas with one solid color."""
    w = int(_canvas['width'])
    h = int(_canvas['height'])
    _canvas.create_rectangle(0, 0, w, h, fill=color_name, outline="")

def draw_line(x1, y1, x2, y2):
    """Draws a line connecting point (x1, y1) to point (x2, y2)."""
    _canvas.create_line(x1, y1, x2, y2, fill=_outline_color, width=_line_thickness)

def fill_rectangle(x, y, width, height):
    """Draws a solid rectangle with its top-left corner at (x, y)."""
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_rectangle(x, y, width, height):
    """Draws an empty rectangle outline with its top-left corner at (x, y)."""
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill="", outline=_outline_color, width=_line_thickness)

def fill_circle(center_x, center_y, radius):
    """Draws a solid circle given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_circle(center_x, center_y, radius):
    """Draws an empty circle outline given its center point and radius."""
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill="", outline=_outline_color, width=_line_thickness)
    
def fill_triangle(x1, y1, x2, y2, x3, y3):
    """Draws a solid triangle connecting the three given points."""
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    """Draws an empty triangle outline connecting the three given points."""
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill="", outline=_outline_color, width=_line_thickness)
    
def fill_arc(x, y, width, height, start_angle, extent_angle):
    """
    Draws a filled pie-slice shape. 
    start_angle is where the slice begins (0 is East).
    extent_angle is how many degrees the slice covers.
    """
    _canvas.create_arc(x, y, x + width, y + height, 
                       start=start_angle, extent=extent_angle, 
                       fill=_fill_color, outline=_outline_color, width=_line_thickness)
    
def draw_curve(points_list):
    """
    Draws a smooth, curved line passing near or through a list of (x, y) coordinates.
    Expects a list of tuples: [(x1, y1), (x2, y2), (x3, y3), ...]
    """
    if len(points_list) < 2:
        print("Error: A curve needs at least 2 points.")
        return
        
    # Tkinter expects a flat sequence of numbers (x1, y1, x2, y2...)
    # This loop unpacks the tuples into a single flat list
    flat_coordinates = []
    for x, y in points_list:
        flat_coordinates.append(x)
        flat_coordinates.append(y)
        
    # Draw the line with smooth=True to make it a curve
    _canvas.create_line(
        *flat_coordinates, 
        smooth=True, 
        fill=_outline_color, 
        width=_line_thickness
    )
    

def draw_text(x, y, text_string, font_size=16):
    """Draws text on the screen with the top-left corner at (x, y)."""
    _canvas.create_text(x, y, text=text_string, fill=_fill_color, 
                        anchor="nw", font=("Arial", font_size))
