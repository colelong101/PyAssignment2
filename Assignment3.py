import sys
from Shapes3D import Shape3D, Cube, Cuboid, Cylinder, Sphere, Prism

#making a solver that uses my Shapes3D file to read a csv file
def solve():
    total = 0
    shape_list = []

    #this part checks to see if you include the csv file as an arguement in the terminal
    if len(sys.argv) < 2:
        print("Please give the name of the data file as an argument in the terminal.")
        return
    filename = sys.argv[1]

    with open(filename) as file:
        #this will split the csv file by its commas
        for line in file:
            line_data = line.strip().split(',')

            my_shape = None
            #this will go through the first word on each line to see if it has the name of the shape, if it does it adds the shape to shape_list
            if line_data[0] == "cuboid":
                my_shape = Cuboid(
                    float(line_data[1]),
                    float(line_data[2]),
                    float(line_data[3])
                )
            elif line_data[0] == "cube":
                my_shape = Cube(
                    float(line_data[1])
                )
            elif line_data[0] == "cylinder":
                my_shape = Cylinder(
                    float(line_data[1]),
                    float(line_data[2])
                )
            elif line_data[0] == "sphere":
                my_shape = Sphere(
                    float(line_data[1])
                )
            elif line_data[0] == "prism":
                my_shape = Prism(
                    float(line_data[1]),
                    int(line_data[2]),
                    float(line_data[3])
                )
            #finds the area and volume of the shapes in the list and adds them up depending on the word in the 0 index spot in the csv file
            elif line_data[0] == "area":
                for shape in shape_list:
                    total += shape.GetSurfaceArea() * float(line_data[1])
                shape_list.clear()
                continue
            elif line_data[0] == "volume":
                for shape in shape_list:
                    total += shape.GetVolume() * float(line_data[1])
                shape_list.clear()
                continue
            else:
                raise ValueError(f"Unable to parse shape from name '{line_data[0]}'")

            shape_list.append(my_shape)
    #.2f makes the float go out 2 decimal points
    print(f"The sum of your measurements is {total:.2f}")
    
#checks if the script is being run as the main program or if it's being imported as a module in another script.
if __name__ == "__main__":
    solve()