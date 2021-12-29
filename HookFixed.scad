// File: Hook.stl
// X size: 46.0
// Y size: 18.0
// Z size: 24.0
// X position: 134.0
// Y position: -78.0
// Z position: -5.0
NE=1; NW=2; SW=3; SE=4; CTR=5;
module obj2origin (where) {
	if (where == NE) {
		objNE ();
	}

	if (where == NW) {
		translate([ -46.0 , 0 , 0 ])
		objNE ();
	}

	if (where == SW) {
		translate([ -46.0 , -18.0 , 0 ])
		objNE ();
	}

	if (where == SE) {
		translate([ 0 , -18.0 , 0 , ])
		objNE ();
	}

	if (where == CTR) {
	translate([ -23.0 , -9.0 , -12.0 ])
		objNE ();
	}
}

module objNE () {
	translate([ -134.0 , 78.0 , 5.0 ])
		import("Hook.stl");
}
