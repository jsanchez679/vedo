# Example directories
Check out more examples in the above directories.

## Get Started tutorial
Download the tutorial:
```bash
git clone https://github.com/marcomusy/vtkplotter.git
cd vtkplotter/examples
python tutorial.py  # on mac OSX try 'pythonw' instead
```

The content of the python script and its output is the following:
```python
from random import gauss, uniform as u
from vtkplotter import Plotter
import math

# Declare an instance of the class
vp = Plotter(title='first example')

# Load a vtk file as a vtkActor derived object and visualize it.
# (The actual mesh corresponds to the outer shape of 
# an embryonic mouse limb at about 11 days of gestation).
# Choose a tomato color for the internal surface of the mesh, and no transparency.
vp.load('data/270.vtk', c='b', bc='tomato') # c=(R,G,B), letter or color name, b=blue
vp.show()  # picks what was stored in python list vp.actors 
# Press Esc to close the window and exit python session, or q to continue
```
![tut1](https://user-images.githubusercontent.com/32848391/50738980-d9227400-11d9-11e9-8a7c-14b2abc4d41f.jpg)


```python
# Load 3 actors assigning each a different color, 
# by default use their file names as legend entries.
# No need to use any variables, as actors are stored internally in vp.actors:
vp = Plotter(title='3 shapes')
vp.load('data/250.vtk', c=(1,0.4,0), alpha=0.3) # set opacity to 30%
vp.load('data/270.vtk', c=(1,0.6,0), alpha=0.3)
vp.load('data/290.vtk', c=(1,0.8,0), alpha=0.3)
print('Loaded vtkActors: ', len(vp.actors))
vp.show()
```
![tut2](https://user-images.githubusercontent.com/32848391/50738979-d9227400-11d9-11e9-8865-a51515b2647f.jpg)

```python
# Draw splines through a set of points, with different smoothing factors:
vp = Plotter(title='Example of splines through random points')

pts = [ (u(0,2), u(0,2), u(0,2)+i) for i in range(8) ] # build python list of points
vp.points(pts, legend='random points')                 # create the Actor

for i in range(10):
    vp.spline(pts, smooth=i/10., degree=2, c=i, legend='smoothing '+str(i/10.))
vp.show(viewup='z')
```
![tut3](https://user-images.githubusercontent.com/32848391/50738978-d889dd80-11d9-11e9-90f1-485dc8212760.jpg)

```python
# Draw a cloud of points each point with a different color
# which depends on the point position itself
vp = Plotter(title='color points')

rgb = [(u(0,255), u(0,255), u(0,255)) for i in range(5000)]

vp.points(rgb, c=rgb, alpha=0.7, legend='RGB points')
vp.show()
```
![tut4](https://user-images.githubusercontent.com/32848391/50738977-d889dd80-11d9-11e9-9fba-6d7bd7b74e93.jpg)

```python
# Draw a bunch of simple objects on separate parts of the rendering window:
# split window automatically to best accomodate 9 renderers
vp = Plotter(N=9, title='basic shapes', axes=0) # split window in 9 frames
vp.sharecam = False                             # each object can be moved independently
vp.show(at=0, actors=vp.arrow([0,0,0],[1,1,1]),    legend='arrow' )
vp.show(at=1, actors=vp.line([0,0,0],[1,1,1]),     legend='line' )
vp.show(at=2, actors=vp.points([[0,0,0],[1,1,1]]), legend='points' )
vp.show(at=3, actors=vp.text('Hello!') )
vp.show(at=4, actors=vp.sphere() )
vp.show(at=5, actors=vp.cube(),     legend='cube')
vp.show(at=6, actors=vp.ring(),     legend='ring')
vp.show(at=7, actors=vp.helix(),    legend='helix')
vp.show(at=8, actors=vp.cylinder(), legend='cylinder', interactive=1)
```
![tut6](https://user-images.githubusercontent.com/32848391/50738976-d889dd80-11d9-11e9-8b13-9bc3436956ac.jpg)

```python
# Draw a bunch of objects from various mesh formats. Loading is automatic.
vp = Plotter(shape=(3,3), title='mesh formats') # split window in 3 rows and 3 columns
vp.sharecam = False                             # each object can be moved independently
vp.show('data/beethoven.ply', at=0, c=0, axes=0)    # dont show axes
vp.show('data/cow.g',         at=1, c=1, zoom=1.15) # make it 15% bigger
vp.show('data/limb.pcd',      at=2, c=2)
vp.show('data/ring.gmsh',     at=3, c=3, wire=1)    # show mesh as wireframe
vp.show('data/images/dog.jpg',at=4)                 # 2d images can be loaded the same way
vp.show('data/shuttle.obj',   at=5, c=5)
vp.show('data/shapes/man.vtk',at=6, c=6, axes=2)    # show negative axes segments
vp.show('data/teapot.xyz',    at=7, c=7, axes=3)    # hide negative axes
vp.show('data/pulley.vtu',    at=8, c=8, interactive=1) # try to click object and press k
```
![tut7](https://user-images.githubusercontent.com/32848391/50738975-d889dd80-11d9-11e9-97a1-647a9a044718.jpg)


```python
# Increase the number of vertices of a mesh using subdivide().
# Show the mesh before and after in two separate renderers defined by shape=(1,2)
vp = Plotter(shape=(1,2), axes=0) # dont show axes
a1 = vp.load('data/beethoven.ply')

coords1 = a1.coordinates() # get coordinates of mesh vertices
pts1 = vp.points(coords1, r=4, c='g', legend='#points = '+str(len(coords1)))
vp.show([a1, pts1], at=0) # show a specific list of actors on renderer nr.0

a2 = a1.subdivide() # Increase the number of points of the mesh
coords2 = a2.coordinates()
pts2 = vp.points(coords2, r=1, legend='#points = '+str(len(coords2)))
vp.show([a2, pts2], at=1, interactive=True)
```
![tut5](https://user-images.githubusercontent.com/32848391/50738974-d889dd80-11d9-11e9-8134-de690f6796ac.jpg)


```python
#########################################################################################
# Cut a set of shapes with a plane that goes through the
# point at x=500 and has normal (0, 0.3, -1).
# Wildcards can be used to load multiple files or entire directories:
vp = Plotter(title='Cut a surface with a plane')
vp.load('data/2*0.vtk', c='orange', bc='aqua')
for a in vp.actors:
    vp.cutPlane(a, origin=(500,0,0), normal=(0,0.3,-1), showcut=True)
vp.show()
```
![tut8](https://user-images.githubusercontent.com/32848391/50738973-d889dd80-11d9-11e9-9885-1c2d0a7df30d.jpg)



