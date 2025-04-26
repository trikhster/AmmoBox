# ammobox/examples/example_9mm_box.py

from ammobox.outer_box import make_outer_box
from ammobox.grid_insert import make_grid_insert
from ammobox.slide_lid import make_slide_lid
from ammobox.viewer import view_shapes

# Create outer box
box = make_outer_box(
    length=278,   # in mm (about 11 inches)
    width=147,    # in mm (about 5.8 inches)
    height=177    # in mm (about 7 inches)
)

# Create 9mm insert
insert = make_grid_insert(
    round_diameter=9.5,  # 9mm bullet size
    round_height=29,     # Approximate height of a 9mm cartridge
    wall_thickness=1.2
)

# Create slide lid
lid = make_slide_lid(
    length=278,
    width=147,
    thickness=2.5
)

# (Optional) Visualization code will go here later.
print("Successfully generated 9mm box, insert, and lid!")
view_shapes(box, insert, lid)