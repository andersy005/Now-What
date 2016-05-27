// Model to take externally-generated surface data
// and then create a surface with it

difference(){
    translate([0, 0,2]) 
    surface(file = "sinusoids.dat", 
                    center = true, 
                    convexity = 5);
    surface(file = "sinusoids.dat", 
                    center = true, 
                    convexity = 5);
}