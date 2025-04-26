# ammobox/outer_box.py
# Outer container generator for AmmoBox project

from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.gp import gp_Pnt, gp_Trsf, gp_Vec
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeCompound

from ammobox.common_helpers import add_sacrificial_tabs

def make_outer_box(length=278, width=147, height=177,
                   wall_thickness=1.5, fillet_radius=5.0,
                   lid_slot_depth=2.5, lid_slot_gap=1.0,
                   sacrificial_tab_size=5.0, sacrificial_tab_thickness=0.3):
    """
    Create the outer AmmoBox.
    :param length: Total outer length in mm
    :param width: Total outer width in mm
    :param height: Total height in mm
    :param wall_thickness: Wall thickness of the box
    :param fillet_radius: Radius for outer corners
    :param lid_slot_depth: How deep the lid slide-in slot should be
    :param lid_slot_gap: Vertical gap from the top edge
    :return: Final shape (TopoDS_Shape)
    """

    # Main outer box
    outer_box = BRepPrimAPI_MakeBox(length, width, height).Shape()

    # Inner cut box (the cavity)
    inner_length = length - 2 * wall_thickness
    inner_width = width - 2 * wall_thickness
    inner_height = height - 5  # leave 5mm gap above insert for lid space

    cavity = BRepPrimAPI_MakeBox(inner_length, inner_width, inner_height).Shape()

    # Position the cavity
    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(wall_thickness, wall_thickness, 0))
    cavity_translated = BRepBuilderAPI_Transform(cavity, trsf).Shape()

    # Cut the cavity out of the box
    box_with_cavity = BRepAlgoAPI_Cut(outer_box, cavity_translated).Shape()

    # Fillet the external edges
    fillet_maker = BRepFilletAPI_MakeFillet(box_with_cavity)
    edge_explorer = TopExp_Explorer(box_with_cavity, TopAbs_EDGE)
    while edge_explorer.More():
        edge = edge_explorer.Current()
        fillet_maker.Add(fillet_radius, edge)
        edge_explorer.Next()

    box_fillet = fillet_maker.Shape()

    # TODO: Add trapezoidal lid rails here (advanced feature coming soon)

    # Add sacrificial tabs for bed adhesion
    final_shape = add_sacrificial_tabs(
        shape=box_fillet,
        shape_length=length,
        shape_width=width,
        tab_size=sacrificial_tab_size,
        tab_thickness=sacrificial_tab_thickness
    )

    return final_shape

