# Your code needs to at least start here so the
# autograder can find it.

with open("number.dat") as file:
    for line in file.readlines():
        print(line)
        for [index, digit] in enumerate(line):
            s = "th"
            if index == 0:
                s = "st"
            elif index == 1:
                s = "nd"
            elif index == 2:
                s = "rd"
              
            print(str(index+1)+s + " digit: " + digit)
