# ammobox/common_helpers.py
# Common helper functions for AmmoBox project

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Trsf, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform, BRepBuilderAPI_MakeCompound
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse

def add_sacrificial_tabs(shape, shape_length, shape_width, tab_size=5, tab_thickness=0.3):
    """
    Add small sacrificial tabs at the four corners of the base.
    """

    compound = BRepBuilderAPI_MakeCompound()

    # Offsets for the four corners
    offsets = [
        (0, 0),
        (shape_length - tab_size, 0),
        (0, shape_width - tab_size),
        (shape_length - tab_size, shape_width - tab_size)
    ]

    for dx, dy in offsets:
        tab = BRepPrimAPI_MakeBox(dx, dy, 0, tab_size, tab_size, tab_thickness).Shape()
        compound.Add(tab)

    # Merge tabs with original shape
    final_shape = BRepAlgoAPI_Fuse(shape, compound.Shape()).Shape()

    return final_shape

def create_trapezoidal_extrusion(length, width_top, width_bottom, height):
    """
    Creates a trapezoidal prism with different widths at top and bottom
    """

    # This function can be expanded if needed for grid inserts or lid profiles
    pass  # We'll complete this as needed
