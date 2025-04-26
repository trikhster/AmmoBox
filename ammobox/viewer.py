# ammobox/viewer.py
# Simple 3D Viewer for AmmoBox project using pythonocc

from OCC.Display.SimpleGui import init_display

def view_shapes(*shapes):
    """
    Simple function to display one or more TopoDS_Shapes
    """
    display, start_display, add_menu, add_function_to_menu = init_display()

    for shape in shapes:
        display.DisplayShape(shape, update=True)

    display.FitAll()
    start_display()
