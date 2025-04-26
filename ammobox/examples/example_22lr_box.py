# ammobox/examples/example_22lr_box.py

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

# Create .22LR insert
insert = make_grid_insert(
    round_diameter=5.7,  # .22LR bullet size
    round_height=15,     # Approximate height of .22LR
    wall_thickness=1.2
)

# Create slide lid
lid = make_slide_lid(
    length=278,
    width=147,
    thickness=2.5
)

print("Successfully generated .22LR box, insert, and lid!")
view_shapes(box, insert, lid)