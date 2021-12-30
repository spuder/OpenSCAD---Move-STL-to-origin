# stl2origin

Takes an STL file and centers the object to the origin

Forked from: https://github.com/lar3ry/OpenSCAD---Move-STL-to-origin  
Origional Python script credit: https://www.reddit.com/r/3Dprinting/comments/7ehlfc/python_script_to_find_stl_dimensions/


## Dockerhub

`Arm/M1` :apple: and `Intel/AMD` :computer: docker containers are published to dockerhub :whale:
```
docker pull spuder/stl2origin:latest
```

[View on dockerhub](https://hub.docker.com/repository/docker/spuder/stl2origin)

New docker containers are automatically pushed with :octocat: [gitub actions](https://github.com/spuder/OpenSCAD---Move-STL-to-origin/actions) on every tag&release

|Before |After|
|---|---|
| ![before](./before.gif) | ![after](./after.gif) |

**Note: This script only centers the png output, it doesn't actually create an animated gif**, but it is super trivial to [add animations as shown here:](https://stackoverflow.com/questions/70468797/how-to-convert-stl-to-rotating-gif-using-openscad/70468907#70468907)


Runs in a docker container. Takes one of several environment variables. You may combine 1 or more environment variables depending on your workflow. 

| Variable | Example | Description | 
|---|---|---|
| `OUTPUT_BASH_FILE` | `/output/foo.sh` | x,y,z cordinates to a file that can be sourced in bash scripts|
| `OUTPUT_SCAD_FILE` | `/output/foo.scad` | Generates a simple openscad file to translate the object to origin
| `OUTPUT_STDOUT` | `true` | Prints text to STDOUT


A full example of how to use this container can be found in [spuder/CAD-scripts/stl2gif.sh](https://github.com/openscad/openscad/issues/1797) which is used in my template for CAD files [spuder/CAD-template/Makefile](https://github.com/spuder/CAD-template/blob/main/Makefile#L15)


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

Will create `foo.sh` with the following content
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
XMID="xxx" # mid point of the object. Offset by this amount to move origin from corner to center
YMID="yyy" # mid point of the object. Offset by this amount to move origin from corner to center
ZMID="zzz" # mid point of the object. Offset by this amount to move origin from corner to center
```

1. `-e OUTPUT_SCAD_FILE=/output/foo.scad`
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

1. `-e OUTPUT_STDOUT=true`
Prints output to stdout (as scad format)

```
translate([ 65.123 , 37.133 , -126.776 ])
                import("/input/foo.stl");
```
