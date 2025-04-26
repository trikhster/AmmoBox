# ammobox/export.py
# Shape Exporter for AmmoBox project

from OCC.Core.StlAPI import StlAPI_Writer
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs, STEPControl_ShellBasedSurfaceModel
from OCC.Core.IFSelect import IFSelect_RetDone

def export_stl(shape, filename):
    """
    Export a shape as an STL file
    """
    writer = StlAPI_Writer()
    writer.SetASCIIMode(False)  # Binary STL is smaller
    writer.Write(shape, filename)
    print(f"Exported STL: {filename}")

def export_step(shape, filename):
    """
    Export a shape as a STEP file
    """
    step_writer = STEPControl_Writer()
    step_writer.Transfer(shape, STEPControl_AsIs)
    status = step_writer.Write(filename)
    if status == IFSelect_RetDone:
        print(f"Exported STEP: {filename}")
    else:
        print("STEP export failed.")
