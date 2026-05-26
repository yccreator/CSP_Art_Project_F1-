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

    # draw a mountain
    sg.set_fill_color("#827e7e") # relatively dark gray
    sg. fill_triangle(300, 150, 400, 20, 350, 150)
    sg.set_fill_color("#c7c1c1") # lighter gray
    sg. fill_triangle(350, 150, 400, 20, 550, 150)

    # draw horizon
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
