# Your code needs to at least start here so the
# autograder can find it.

with open("rectangle.dat") as file:
    for line in file.readlines():
        try: 
            [a, b] = [float(x) for x in line.split(" ")]

            print("Length: "+ str(int(a)))
            print("Width: "+ str(int(b)))
            print("Area: "+str(int(a*b)))
            print("Perimeter: "+str(int(2*a + 2*b)))
        except:
            print("Some expected output")
