# stl2origin

Takes an STL file and centers the object to the origin

Forked from: https://github.com/lar3ry/OpenSCAD---Move-STL-to-origin
Origional Python script credit: https://www.reddit.com/r/3Dprinting/comments/7ehlfc/python_script_to_find_stl_dimensions/


Runs in a docker container. Takes one of several environment variables. You may combine 1 or more environment variables depending on your workflow. 

| Variable | Example | Description | 
|---|---|---|
| `OUTPUT_BASH_FILE` | `/output/foo.sh` | x,y,z cordinates to a file that can be sourced in bash scripts|
| `OUTPUT_SCAD_FILE` | `/output/foo.scad` | Generates a simple openscad file to translate the object to origin
| `OUTPUT_STDOUT` | `true` | Prints text to STDOUT


## Usage

1. `-e OUTPUT_BASH_FILE=/output/foo.sh`
Take input /tmp/foo.stl and save to foo.sh
foo.sh can then be sourced for other scripts e.g.
`source foo.sh; echo "[${XTRANS},${YTRANS},${ZTRANS}]"`

```bash
file="/tmp/foo.stl"
docker run \
  -e OUTPUT_BASH_FILE=/output/foo.sh \
  -v $(dirname "$file"):/input \
  -v $(pwd):/output \
  --rm spuder/stl2origin:latest \
  /input/$(basename "$file")
```
```bash
XSIZE="10.0"
YSIZE="19.8"
ZSIZE="11.324"
XPOS="-65.123"
YPOS="-37.133"
ZPOS="126.776"
XTRANS="65.123"
YTRANS="37.133"
ZTRANS="-126.776"
```

2. `-e OUTPUT_SCAD_FILE=/output/foo.scad`
Take input /tmp/foo.stl and write a scad file to $(PWD)/foo.scad
```bash
file="/tmp/foo.stl"
docker run \
  -e OUTPUT_SCAD_FILE=/output/foo.scad \
  -v $(dirname "$file"):/input \
  -v $(pwd):/output \
  --rm spuder/stl2origin:latest \
  /input/$(basename "$file")
```

example foo.scad
```bash
translate([ 65.123 , 37.133 , -126.776 ])
                import("/input/foo.stl");
```

3. `-e OUTPUT_STDOUT=true`
Prints output to stdout (as scad format)

```
translate([ 65.123 , 37.133 , -126.776 ])
                import("/input/foo.stl");
```