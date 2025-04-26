# ammobox/grid_insert.py
# Grid Insert Generator for AmmoBox project (Auto-sized to fit box)

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.gp import gp_Trsf, gp_Vec
import math

from ammobox.common_helpers import add_sacrificial_tabs

def make_grid_insert(
    round_diameter=9.5,
    round_height=29,
    wall_thickness=1.2,
    insert_length=278,     # NEW: available length (matches outer box inner dimensions)
    insert_width=147,      # NEW: available width
    snap_tab_height=3.0,
    trapezoid_angle_deg=5.0,
    sacrificial_tab_size=5.0,
    sacrificial_tab_thickness=0.3
):
    """
    Create a modular hex grid insert based on available box size and round size
    """

    # Constants
    radius = round_diameter / 2.0
    spacing = round_diameter + wall_thickness  # center-to-center distance between cells

    # Calculate rows and columns to fill available space
    rows = int(insert_length // spacing)
    cols = int(insert_width // (spacing * 0.866))  # hexagonal packing factor

    # Adjust grid footprint
    grid_width = spacing * cols * 0.866
    grid_length = spacing * rows

    insert_thickness = round_height + 2  # a little extra for base and strength

    # Create base plate
    base = BRepPrimAPI_MakeBox(grid_length, grid_width, insert_thickness).Shape()

    # Cut hexagonal holes
    holes = []
    for row in range(rows):
        for col in range(cols):
            x_offset = row * spacing
            y_offset = col * spacing * 0.866  # hex grid Y spacing
            if row % 2 == 1:
                y_offset += (spacing * 0.866) / 2  # offset odd rows

            # Create vertical cylinder hole
            hole = BRepPrimAPI_MakeCylinder(radius, insert_thickness + 1).Shape()

            # Move it into position
            trsf = gp_Trsf()
            trsf.SetTranslation(gp_Vec(x_offset, y_offset, 0))
            moved_hole = BRepBuilderAPI_Transform(hole, trsf).Shape()

            holes.append(moved_hole)

    # Fuse all holes together
    if holes:
        from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
        fused_holes = holes[0]
        for hole in holes[1:]:
            fused_holes = BRepAlgoAPI_Fuse(fused_holes, hole).Shape()

        # Cut fused holes out of base
        insert_with_holes = BRepAlgoAPI_Cut(base, fused_holes).Shape()
    else:
        insert_with_holes = base

    # Add sacrificial tabs
    final_insert = add_sacrificial_tabs(
        shape=insert_with_holes,
        shape_length=grid_length,
        shape_width=grid_width,
        tab_size=sacrificial_tab_size,
        tab_thickness=sacrificial_tab_thickness
    )

    return final_insert
