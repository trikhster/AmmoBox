# ammobox/examples/example_45acp_box.py

from ammobox.outer_box import make_outer_box
from ammobox.grid_insert import make_grid_insert
from ammobox.slide_lid import make_slide_lid
from ammobox.viewer import view_shapes

# Create outer box
box = make_outer_box(
    length=278,
    width=147,
    height=177
)

# Create .45ACP insert
insert = make_grid_insert(
    round_diameter=11.5,  # .45 ACP bullet size
    round_height=32,      # Approximate height of .45ACP
    wall_thickness=1.2
)

# Create slide lid
lid = make_slide_lid(
    length=278,
    width=147,
    thickness=2.5
)

print("Successfully generated .45ACP box, insert, and lid!")
view_shapes(box, insert, lid)