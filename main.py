from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)
    
    c = Cell(win)
    c.has_right_wall = False
    c.has_top_wall = False
    c.draw(100, 100, 150, 150)
    
    c = Cell(win)
    c.draw(200, 200, 250, 250)
    #l = Line(Point(50, 50), Point(400, 400))
    #win.draw_line(l, "black")
    win.wait_for_close()
    

main()