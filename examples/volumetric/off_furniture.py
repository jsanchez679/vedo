# Pure vtk stuff.
# Create the furniture objects for the office.py example
import vtk

def furniture():
    # generate a whole bunch of planes which correspond to
    # the geometry in the analysis; tables, bookshelves and so on.

    from vedo import download
    reader = vtk.vtkStructuredGridReader()
    fpath = download('https://vedo.embl.es/examples/data/office.binary.vtk', verbose=0)
    reader.SetFileName(fpath)
    reader.Update()
    sgrid = reader.GetOutput()

    table1 = vtk.vtkStructuredGridGeometryFilter()
    table1.SetInputData(sgrid)
    table1.SetExtent(11, 15, 7, 9, 8, 8)
    mapTable1 = vtk.vtkPolyDataMapper()
    mapTable1.SetInputConnection(table1.GetOutputPort())
    mapTable1.ScalarVisibilityOff()
    table1Actor = vtk.vtkActor()
    table1Actor.SetMapper(mapTable1)
    table1Actor.GetProperty().SetColor(.59, .427, .392)

    table2 = vtk.vtkStructuredGridGeometryFilter()
    table2.SetInputData(sgrid)
    table2.SetExtent(11, 15, 10, 12, 8, 8)
    mapTable2 = vtk.vtkPolyDataMapper()
    mapTable2.SetInputConnection(table2.GetOutputPort())
    mapTable2.ScalarVisibilityOff()
    table2Actor = vtk.vtkActor()
    table2Actor.SetMapper(mapTable2)
    table2Actor.GetProperty().SetColor(.59, .427, .392)

    FilingCabinet1 = vtk.vtkStructuredGridGeometryFilter()
    FilingCabinet1.SetInputData(sgrid)
    FilingCabinet1.SetExtent(15, 15, 7, 9, 0, 8)
    mapFilingCabinet1 = vtk.vtkPolyDataMapper()
    mapFilingCabinet1.SetInputConnection(FilingCabinet1.GetOutputPort())
    mapFilingCabinet1.ScalarVisibilityOff()
    FilingCabinet1Actor = vtk.vtkActor()
    FilingCabinet1Actor.SetMapper(mapFilingCabinet1)
    FilingCabinet1Actor.GetProperty().SetColor(.8, .8, .6)

    FilingCabinet2 = vtk.vtkStructuredGridGeometryFilter()
    FilingCabinet2.SetInputData(sgrid)
    FilingCabinet2.SetExtent(15, 15, 10, 12, 0, 8)
    mapFilingCabinet2 = vtk.vtkPolyDataMapper()
    mapFilingCabinet2.SetInputConnection(FilingCabinet2.GetOutputPort())
    mapFilingCabinet2.ScalarVisibilityOff()
    FilingCabinet2Actor = vtk.vtkActor()
    FilingCabinet2Actor.SetMapper(mapFilingCabinet2)
    FilingCabinet2Actor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1Top = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1Top.SetInputData(sgrid)
    bookshelf1Top.SetExtent(13, 13, 0, 4, 0, 11)
    mapBookshelf1Top = vtk.vtkPolyDataMapper()
    mapBookshelf1Top.SetInputConnection(bookshelf1Top.GetOutputPort())
    mapBookshelf1Top.ScalarVisibilityOff()
    bookshelf1TopActor = vtk.vtkActor()
    bookshelf1TopActor.SetMapper(mapBookshelf1Top)
    bookshelf1TopActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1Bottom = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1Bottom.SetInputData(sgrid)
    bookshelf1Bottom.SetExtent(20, 20, 0, 4, 0, 11)
    mapBookshelf1Bottom = vtk.vtkPolyDataMapper()
    mapBookshelf1Bottom.SetInputConnection(bookshelf1Bottom.GetOutputPort())
    mapBookshelf1Bottom.ScalarVisibilityOff()
    bookshelf1BottomActor = vtk.vtkActor()
    bookshelf1BottomActor.SetMapper(mapBookshelf1Bottom)
    bookshelf1BottomActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1Front = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1Front.SetInputData(sgrid)
    bookshelf1Front.SetExtent(13, 20, 0, 0, 0, 11)
    mapBookshelf1Front = vtk.vtkPolyDataMapper()
    mapBookshelf1Front.SetInputConnection(bookshelf1Front.GetOutputPort())
    mapBookshelf1Front.ScalarVisibilityOff()
    bookshelf1FrontActor = vtk.vtkActor()
    bookshelf1FrontActor.SetMapper(mapBookshelf1Front)
    bookshelf1FrontActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1Back = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1Back.SetInputData(sgrid)
    bookshelf1Back.SetExtent(13, 20, 4, 4, 0, 11)
    mapBookshelf1Back = vtk.vtkPolyDataMapper()
    mapBookshelf1Back.SetInputConnection(bookshelf1Back.GetOutputPort())
    mapBookshelf1Back.ScalarVisibilityOff()
    bookshelf1BackActor = vtk.vtkActor()
    bookshelf1BackActor.SetMapper(mapBookshelf1Back)
    bookshelf1BackActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1LHS = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1LHS.SetInputData(sgrid)
    bookshelf1LHS.SetExtent(13, 20, 0, 4, 0, 0)
    mapBookshelf1LHS = vtk.vtkPolyDataMapper()
    mapBookshelf1LHS.SetInputConnection(bookshelf1LHS.GetOutputPort())
    mapBookshelf1LHS.ScalarVisibilityOff()
    bookshelf1LHSActor = vtk.vtkActor()
    bookshelf1LHSActor.SetMapper(mapBookshelf1LHS)
    bookshelf1LHSActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf1RHS = vtk.vtkStructuredGridGeometryFilter()
    bookshelf1RHS.SetInputData(sgrid)
    bookshelf1RHS.SetExtent(13, 20, 0, 4, 11, 11)
    mapBookshelf1RHS = vtk.vtkPolyDataMapper()
    mapBookshelf1RHS.SetInputConnection(bookshelf1RHS.GetOutputPort())
    mapBookshelf1RHS.ScalarVisibilityOff()
    bookshelf1RHSActor = vtk.vtkActor()
    bookshelf1RHSActor.SetMapper(mapBookshelf1RHS)
    bookshelf1RHSActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2Top = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2Top.SetInputData(sgrid)
    bookshelf2Top.SetExtent(13, 13, 15, 19, 0, 11)
    mapBookshelf2Top = vtk.vtkPolyDataMapper()
    mapBookshelf2Top.SetInputConnection(bookshelf2Top.GetOutputPort())
    mapBookshelf2Top.ScalarVisibilityOff()
    bookshelf2TopActor = vtk.vtkActor()
    bookshelf2TopActor.SetMapper(mapBookshelf2Top)
    bookshelf2TopActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2Bottom = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2Bottom.SetInputData(sgrid)
    bookshelf2Bottom.SetExtent(20, 20, 15, 19, 0, 11)
    mapBookshelf2Bottom = vtk.vtkPolyDataMapper()
    mapBookshelf2Bottom.SetInputConnection(bookshelf2Bottom.GetOutputPort())
    mapBookshelf2Bottom.ScalarVisibilityOff()
    bookshelf2BottomActor = vtk.vtkActor()
    bookshelf2BottomActor.SetMapper(mapBookshelf2Bottom)
    bookshelf2BottomActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2Front = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2Front.SetInputData(sgrid)
    bookshelf2Front.SetExtent(13, 20, 15, 15, 0, 11)
    mapBookshelf2Front = vtk.vtkPolyDataMapper()
    mapBookshelf2Front.SetInputConnection(bookshelf2Front.GetOutputPort())
    mapBookshelf2Front.ScalarVisibilityOff()
    bookshelf2FrontActor = vtk.vtkActor()
    bookshelf2FrontActor.SetMapper(mapBookshelf2Front)
    bookshelf2FrontActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2Back = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2Back.SetInputData(sgrid)
    bookshelf2Back.SetExtent(13, 20, 19, 19, 0, 11)
    mapBookshelf2Back = vtk.vtkPolyDataMapper()
    mapBookshelf2Back.SetInputConnection(bookshelf2Back.GetOutputPort())
    mapBookshelf2Back.ScalarVisibilityOff()
    bookshelf2BackActor = vtk.vtkActor()
    bookshelf2BackActor.SetMapper(mapBookshelf2Back)
    bookshelf2BackActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2LHS = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2LHS.SetInputData(sgrid)
    bookshelf2LHS.SetExtent(13, 20, 15, 19, 0, 0)
    mapBookshelf2LHS = vtk.vtkPolyDataMapper()
    mapBookshelf2LHS.SetInputConnection(bookshelf2LHS.GetOutputPort())
    mapBookshelf2LHS.ScalarVisibilityOff()
    bookshelf2LHSActor = vtk.vtkActor()
    bookshelf2LHSActor.SetMapper(mapBookshelf2LHS)
    bookshelf2LHSActor.GetProperty().SetColor(.8, .8, .6)

    bookshelf2RHS = vtk.vtkStructuredGridGeometryFilter()
    bookshelf2RHS.SetInputData(sgrid)
    bookshelf2RHS.SetExtent(13, 20, 15, 19, 11, 11)
    mapBookshelf2RHS = vtk.vtkPolyDataMapper()
    mapBookshelf2RHS.SetInputConnection(bookshelf2RHS.GetOutputPort())
    mapBookshelf2RHS.ScalarVisibilityOff()
    bookshelf2RHSActor = vtk.vtkActor()
    bookshelf2RHSActor.SetMapper(mapBookshelf2RHS)
    bookshelf2RHSActor.GetProperty().SetColor(.8, .8, .6)

    window = vtk.vtkStructuredGridGeometryFilter()
    window.SetInputData(sgrid)
    window.SetExtent(20, 20, 6, 13, 10, 13)
    mapWindow = vtk.vtkPolyDataMapper()
    mapWindow.SetInputConnection(window.GetOutputPort())
    mapWindow.ScalarVisibilityOff()
    windowActor = vtk.vtkActor()
    windowActor.SetMapper(mapWindow)
    windowActor.GetProperty().SetColor(.3, .3, .5)

    outlet = vtk.vtkStructuredGridGeometryFilter()
    outlet.SetInputData(sgrid)
    outlet.SetExtent(0, 0, 9, 10, 14, 16)
    mapOutlet = vtk.vtkPolyDataMapper()
    mapOutlet.SetInputConnection(outlet.GetOutputPort())
    mapOutlet.ScalarVisibilityOff()
    outletActor = vtk.vtkActor()
    outletActor.SetMapper(mapOutlet)
    outletActor.GetProperty().SetColor(1, 1, 1)

    inlet = vtk.vtkStructuredGridGeometryFilter()
    inlet.SetInputData(sgrid)
    inlet.SetExtent(0, 0, 9, 10, 0, 6)
    mapInlet = vtk.vtkPolyDataMapper()
    mapInlet.SetInputConnection(inlet.GetOutputPort())
    mapInlet.ScalarVisibilityOff()
    inletActor = vtk.vtkActor()
    inletActor.SetMapper(mapInlet)
    inletActor.GetProperty().SetColor(1, 1, 1)

    outline = vtk.vtkStructuredGridOutlineFilter()
    outline.SetInputData(sgrid)
    mapOutline = vtk.vtkPolyDataMapper()
    mapOutline.SetInputConnection(outline.GetOutputPort())
    outlineActor = vtk.vtkActor()
    outlineActor.SetMapper(mapOutline)
    outlineActor.GetProperty().SetColor(1, 1, 1)

    acts = []
    acts.append(table1Actor)
    acts.append(table2Actor)
    acts.append(FilingCabinet1Actor)
    acts.append(FilingCabinet2Actor)
    acts.append(bookshelf1TopActor)
    acts.append(bookshelf1BottomActor)
    acts.append(bookshelf1FrontActor)
    acts.append(bookshelf1BackActor)
    acts.append(bookshelf1LHSActor)
    acts.append(bookshelf1RHSActor)
    acts.append(bookshelf2TopActor)
    acts.append(bookshelf2BottomActor)
    acts.append(bookshelf2FrontActor)
    acts.append(bookshelf2BackActor)
    acts.append(bookshelf2LHSActor)
    acts.append(bookshelf2RHSActor)
    acts.append(windowActor)
    acts.append(outletActor)
    acts.append(inletActor)
    acts.append(outlineActor)

    return acts

if __name__ == "__main__":

    from vedo import show

    show(furniture())
