# Your code needs to at least start here so the
# autograder can find it.

with open("time.dat") as file:
    for line in file.readlines():
        t = int(line)

        h = t // 3600
        m = (t % 3600) // 60
        s = (t % 60)

        print(f"{t} seconds is {h} hour(s), {m} minute(s), and {s} second(s).")

        #9999 seconds is 2 hour(s), 46 minute(s), and 39 second(s).
