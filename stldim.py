import math
import stl
from stl import mesh
import numpy

import os
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: %s [stl file]' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: file %s was not found!' % sys.argv[1])

# this stolen from numpy-stl documentation
# https://pypi.python.org/pypi/numpy-stl

# find the max dimensions, so we can know the bounding box, getting the height,
# width, length (because these are the step size)...
def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

main_body = mesh.Mesh.from_file(sys.argv[1])

minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(main_body)

minx=round(minx,3)
maxx=round(maxx,3)
miny=round(miny,3)
maxy=round(maxy,3)
minz=round(minz,3)
maxz=round(maxz,3)

xsize = round(maxx-minx,3)
ysize = round(maxy-miny,3)
zsize = round(maxz-minz,3)

midx = round(xsize/2,3)
midy = round(ysize/2,3)
midz = round(zsize/2,3)

# the logic is easy from there
if 'OUTPUT_STDOUT' in os.environ:
    print ("// File:", sys.argv[1])
    lst = ['obj =("',sys.argv[1],'");']
    obj = ['\t\timport("',sys.argv[1],'");']

    print ("// X size:",xsize)
    print ("// Y size:", ysize)
    print ("// Z size:", zsize)
    print ("// X position:",minx)
    print ("// Y position:",miny)
    print ("// Z position:",minz)
    print ("// X midpoint:",midx)
    print ("// Y midpoint:",midy)
    print ("// Z midpoint:",midz)
    #--------------------
    # print("NE=1; NW=2; SW=3; SE=4; CTR=5;")


    # print ("module obj2origin (where) {")
    # print ("\tif (where == NE) {")
    # print ("\t\tobjNE ();")
    # print("\t}")
    # print("")

    # print("\tif (where == NW) {")
    # print("\t\ttranslate([",-xsize,",",0,",",0,"])")
    # print ("\t\tobjNE ();")
    # print("\t}")
    # print("")

    # print ("\tif (where == SW) {")
    # print("\t\ttranslate([",-xsize,",",-ysize,",",0,"])")
    # print ("\t\tobjNE ();")
    # print("\t}")
    # print("")

    # print ("\tif (where == SE) {")
    # print("\t\ttranslate([",0,",",-ysize,",",0,",","])")
    # print ("\t\tobjNE ();")
    # print("\t}")
    # print("")

    # print ("\tif (where == CTR) {")
    # print("\ttranslate([",-midx, ",",-midy,",",-midz,"])")
    # print ("\t\tobjNE ();")
    # print("\t}")
    # print("}")
    # print("")
    print("translate([",-minx,",",-miny,",",-minz,"])")
    print ("".join(obj))

if 'OUTPUT_SCAD_FILE' in os.environ:
    # print("Writing to file:", os.environ['OUTPUT_SCAD_FILE'])
    with open('/output/foo.scad', 'w') as f:
        f.write("translate([\",-minx-midx,\",\",-miny-midy,\",\",-minz-midz,\"])\n")
        f.write("".join(obj))
        f.close()

if 'OUTPUT_BASH_FILE' in os.environ:
    # print("Writing to file:", os.environ['OUTPUT_BASH_FILE'])
    with open('/output/foo.sh', 'w') as f:
        f.write(f"XSIZE={xsize}"+"\n")
        f.write(f"YSIZE={ysize}"+"\n")
        f.write(f"ZSIZE={zsize}"+"\n")
        f.write(f"XPOS={minx}"+"\n")
        f.write(f"YPOS={miny}"+"\n")
        f.write(f"ZPOS={minz}"+"\n")
        f.write(f"XTRANS={-minx}"+"\n")
        f.write(f"YTRANS={-miny}"+"\n")
        f.write(f"ZTRANS={-minz}"+"\n")
        f.write(f"XMID={midx}"+"\n")
        f.write(f"YMID={midy}"+"\n")
        f.write(f"ZMID={midz}"+"\n")
        f.close()