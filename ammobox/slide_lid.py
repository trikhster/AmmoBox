# ammobox/slide_lid.py
# Sliding Lid Generator for AmmoBox project

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakePolygon
from OCC.Core.gp import gp_Pnt, gp_Vec
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
import math

from ammobox.common_helpers import add_sacrificial_tabs

def make_slide_lid(length=278, width=147, thickness=2.5,
                   trapezoid_angle_deg=5.0, chamfer_depth=2.0,
                   sacrificial_tab_size=5.0, sacrificial_tab_thickness=0.3):
    """
    Create a trapezoidal lid that slides into the rails
    """

    angle_rad = math.radians(trapezoid_angle_deg)
    width_top = width
    width_bottom = width - 2 * math.tan(angle_rad) * thickness

    # Build a trapezoidal profile
    poly = BRepBuilderAPI_MakePolygon()
    poly.Add(gp_Pnt(0, 0, 0))                         # Bottom left
    poly.Add(gp_Pnt(length, 0, 0))                    # Bottom right
    poly.Add(gp_Pnt(length, width_bottom, thickness)) # Top right
    poly.Add(gp_Pnt(0, width_bottom, thickness))      # Top left
    poly.Close()

    wire = BRepBuilderAPI_MakeWire(poly.Wire()).Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()

    # Extrude
    vector = gp_Vec(0, 0, thickness)
    lid = BRepPrimAPI_MakePrism(face, vector).Shape()

    # Chamfer the front edge
    # (Advanced optional: can add a beveled chamfer manually if needed)

    # Add sacrificial tabs
    final_lid = add_sacrificial_tabs(
        shape=lid,
        shape_length=length,
        shape_width=width_bottom,
        tab_size=sacrificial_tab_size,
        tab_thickness=sacrificial_tab_thickness
    )

    return final_lid
