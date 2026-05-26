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
def draw_house(x, y, width, height, house_color):
    """
    Draws a house with a base, triangular roof, chimney, windows, and a door
    based on the student's grid sketch planning sheet.
    
    AI Attribution: This function was generated using Gemini.
    Original Student Prompt: "can you draw this its a house" with x, y, width, height, house_color parameters.
    """
    # 1. Draw the Chimney (drawn first so it sits behind the roof)
    # Positions it on the right side of the roof, like the sketch
    chimney_width = width * 0.15
    chimney_height = height * 0.4
    chimney_x = x + (width * 0.65)
    chimney_y = y - (height * 0.3)
    _canvas.create_rectangle(
        chimney_x, chimney_y, 
        chimney_x + chimney_width, chimney_y + chimney_height,
        fill=house_color, outline=_outline_color, width=_line_thickness
    )
    
    # 2. Draw the Main House Body (Rectangle)
    _canvas.create_rectangle(
        x, y, 
        x + width, y + height, 
        fill=house_color, outline=_outline_color, width=_line_thickness
    )
    
    # 3. Draw the Roof (Triangle)
    # Peak is centered above the house; bottom corners match the house top corners
    _canvas.create_polygon(
        x, y,                          # Bottom-left corner
        x + (width / 2), y - (height * 0.5), # Top peak
        x + width, y,                  # Bottom-right corner
        fill=house_color, outline=_outline_color, width=_line_thickness
    )
    
    # 4. Draw the Left Window
    win_size = width * 0.2
    win1_x = x + (width * 0.15)
    win_y = y + (height * 0.2)
    _canvas.create_rectangle(
        win1_x, win_y, 
        win1_x + win_size, win_y + win_size, 
        fill="white", outline=_outline_color, width=_line_thickness
    )
    # Window grid lines
    _canvas.create_line(win1_x + (win_size / 2), win_y, win1_x + (win_size / 2), win_y + win_size, fill=_outline_color, width=_line_thickness)
    _canvas.create_line(win1_x, win_y + (win_size / 2), win1_x + win_size, win_y + (win_size / 2), fill=_outline_color, width=_line_thickness)
    
    # 5. Draw the Right Window
    win2_x = x + (width * 0.55)
    _canvas.create_rectangle(
        win2_x, win_y, 
        win2_x + win_size, win_y + win_size, 
        fill="white", outline=_outline_color, width=_line_thickness
    )
    # Window grid lines
    _canvas.create_line(win2_x + (win_size / 2), win_y, win2_x + (win_size / 2), win_y + win_size, fill=_outline_color, width=_line_thickness)
    _canvas.create_line(win2_x, win_y + (win_size / 2), win2_x + win_size, win_y + (win_size / 2), fill=_outline_color, width=_line_thickness)
    
    # 6. Draw the Door
    door_w = width * 0.25
    door_h = height * 0.4
    door_x = x + (width * 0.55)
    door_y = y + height - door_h
    _canvas.create_rectangle(
        door_x, door_y, 
        door_x + door_w, door_y + door_h, 
        fill="brown", outline=_outline_color, width=_line_thickness
    )
    # Doorknob
    knob_r = door_w * 0.1
    _canvas.create_oval(
        door_x + door_w * 0.75 - knob_r, door_y + door_h * 0.5 - knob_r,
        door_x + door_w * 0.75 + knob_r, door_y + door_h * 0.5 + knob_r,
        fill="gold", outline="black", width=1
    )
def draw_balloons(anchor_x, anchor_y, num_balloons):
    """Draws a cluster of random balloons tied to an anchor point."""
    for _ in range(num_balloons):
        # Pick a random spot for each balloon high above the anchor point
        balloon_x = random.randint(int(anchor_x - 150), int(anchor_x + 150))
        balloon_y = random.randint(int(anchor_y - 250), int(anchor_y - 50))
        radius = random.randint(15, 30)
        
        # Draw the string first so it sits behind the balloon
        set_outline_color("gray")
        set_line_thickness(1)
        draw_line(anchor_x, anchor_y, balloon_x, balloon_y)
        
        # Draw the balloon using a random color
        set_fill_color(random_color())
        set_outline_color("black")
        fill_circle(balloon_x, balloon_y, radius)

def my_drawing(width, height):
    # Give it a nice sky blue background
    fill_background("#87CEEB")
    
    # House variables
    house_x = 300
    house_y = 350 # Pushed down to leave room for the balloons!
    house_width = 200
    house_height = 150
    
    # Calculate where the tip of the roof is to tie the balloons
    roof_peak_x = house_x + (house_width / 2)
    roof_peak_y = house_y - (house_height / 2)
    
    # Draw 75 balloons tied to the roof peak
    draw_balloons(roof_peak_x, roof_peak_y, 75)
    
    # Draw the house right on top of the balloon strings
    set_line_thickness(2)
    draw_house(house_x, house_y, house_width, house_height, "#D9D5C8")

# it starts the function
start(my_drawing)

def draw_text(x, y, text_string, font_size=16):
    """Draws text on the screen with the top-left corner at (x, y)."""
    _canvas.create_text(x, y, text=text_string, fill=_fill_color, 
                        anchor="nw", font=("Arial", font_size))

# draws a house
def my_drawing(width, height):
    set_line_thickness(2)
    draw_house(300, 250, 200, 200, "#D9D5C8")

# draws a house with a sky background
def my_drawing(width, height):
    # 1. Fill the background first so everything else sits on top
    fill_background("#C2E6F5")
    
    # 2. Draw the rest of your scene
    set_line_thickness(2)
    draw_house(300, 250, 200, 200, "#D9D5C8")

# =====================================================================
# NEW HELPER FUNCTION
# =====================================================================
def draw_cloud(center_x, center_y, size):
    """Draws a fluffy cloud by overlapping multiple white circles."""
    # Save the current line thickness so we can restore it later
    global _line_thickness
    old_thickness = _line_thickness
    
    # Hide the outlines by matching fill and outline to white
    set_fill_color("white")
    set_outline_color("white")
    set_line_thickness(0)
    
    # Draw overlapping circles to create the fluffy cloud shape
    fill_circle(center_x, center_y, size)                  # Center puff
    fill_circle(center_x - size * 0.6, center_y, size * 0.7)  # Left puff
    fill_circle(center_x + size * 0.6, center_y, size * 0.7)  # Right puff
    fill_circle(center_x - size * 0.3, center_y - size * 0.3, size * 0.8) # Top-left puff
    fill_circle(center_x + size * 0.3, center_y - size * 0.3, size * 0.8) # Top-right puff
    
    # Restore original line thickness
    set_line_thickness(old_thickness)


# =====================================================================
# MAIN DRAWING FUNCTION
# =====================================================================
def my_drawing(width, height):
    # 1. Fill the background sky
    fill_background("#C2E6F5")
    
    # 2. Draw some clouds at different positions and sizes
    draw_cloud(150, 120, 40)   # A cloud on the top left
    draw_cloud(600, 150, 50)   # A larger cloud on the right
    draw_cloud(400, 80, 30)    # A smaller, higher cloud in the middle
    
    # 3. Draw the house on top of the sky and clouds
    set_outline_color("black") # Reset outline color for the house
    set_line_thickness(2)
    draw_house(300, 250, 200, 200, "#D9D5C8")


# draws a house with a sky, clouds, and a grassy lawn
def my_drawing(width, height):
    # 1. Fill the background sky
    fill_background("#C2E6F5")
    
    # 2. Draw the clouds
    draw_cloud(150, 120, 40)
    draw_cloud(600, 150, 50)
    draw_cloud(400, 80, 30)
    
    # 3. Draw the flat green grass 
    # Starts at X=0, Y=450, stretches across the full width, and goes down 150 pixels
    set_fill_color("#5cb85c")      # A nice, vibrant grass green
    set_outline_color("#5cb85c")   # Match outline to fill so the grass looks smooth
    set_line_thickness(1)
    fill_rectangle(0, 450, width, 150)
    
    # 4. Draw the house on top of the grass
    set_outline_color("black")     # Reset outline color for the house
    set_line_thickness(2)
    draw_house(300, 250, 200, 200, "#D9D5C8")


# it starts the function
start(my_drawing)
