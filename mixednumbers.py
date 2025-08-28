# Your code needs to at least start here so the
# autograder can find it.

with open("mixed.dat") as file:
    for line in file.readlines():
        [a, b] = [int(x) for x in line.split(" ")]
        i = a // b
        f = a % b

        print(f"The mixed number derived from {a}/{b} is {i} {f}/{b}.")
