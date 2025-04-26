# AmmoBox

AmmoBox is a fully modular, parametric 3D model generator for ammunition storage boxes, inspired by the Gridfinity system.  
It uses PythonOCC / OCCT libraries to create stackable, interchangeable ammo boxes and grid inserts optimized for FDM 3D printing (PLA-ready, no supports required).

## Features
- Parameterized box sizes to fit within a parent container (5.8" x 11" x 7" by default)
- Modular, removable hexagonal grid inserts sized by round diameter and height
- Support-free printing with angled (trapezoidal) profiles and sacrificial adhesion tabs
- Slide-in lids to prevent ammunition spillage
- Rounded corners for easy handling
- Designed for pistol and rifle calibers (.22LR, 9mm, .45ACP, .223, .308, etc.)

## Repository Structure

AmmoBox/
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── ammobox/
│   ├── __init__.py
│   ├── common_helpers.py
│   ├── outer_box.py
│   ├── grid_insert.py
│   ├── slide_lid.py
│   ├── viewer.py
│   └── examples/
│       ├── example_9mm_box.py
│       ├── example_22lr_box.py
│       ├── example_45acp_box.py
├── assets/
│   ├── example_renders/
│   └── diagrams/
└── tests/
    ├── test_outer_box.py
    ├── test_grid_insert.py
    ├── test_slide_lid.py

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Ammobox.git
   cd AmmoBox
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

You can generate different ammo boxes and inserts by running the examples in `ammobox/examples/` or importing the modules into your own scripts.

Example:

```python
from ammobox.outer_box import make_outer_box
from ammobox.grid_insert import make_grid_insert
from ammobox.slide_lid import make_slide_lid

# Generate a 9mm insert
insert = make_grid_insert(round_diameter=9.5, round_height=29)
```

## License

AmmoBox is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

This means you are free to use, modify, and share the project, but **commercial use is not permitted**.

## Credits

This project was developed with the assistance of **ChatGPT**, an AI model created by OpenAI, in collaboration with the project owner.  
All design decisions and final integrations were directed by the project owner.

## Contributions

Contributions, feature requests, and bug reports are welcome!  
Please open an issue or submit a pull request.

---
```

---

✅ You can **copy this full text into a `README.txt`**,  
✅ Then rename it **`README.md`** to make it markdown-renderable on GitHub or wherever you use it.

---

# 🚀 Would you like me to generate the **LICENSE text** in the same way too?  
(Same idea — plain text ready to save!)  
Just say **"generate license"** if you want it! 🎯