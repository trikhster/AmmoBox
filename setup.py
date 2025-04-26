from setuptools import setup, find_packages

setup(
    name="AmmoBox",
    version="0.1.0",
    author="Your Name Here",
    description="Modular parametric 3D model generator for ammunition boxes",
    packages=find_packages(),
    install_requires=[
        "pythonocc-core>=7.5.1",   # adjust depending on installed OCC version
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Creative Commons Attribution-NonCommercial 4.0 International",
        "Programming Language :: Python :: 3",
    ],
)
