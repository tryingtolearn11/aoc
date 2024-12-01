# Part One

def f(x):
    lines = x.read().splitlines()

    for line in lines[0:1]:
        print(line)
        escaped_literals_count = 0
        num_chars = 2
        for char in line:
            # If a backslash is read
            if char == "\\":
                # Check the next character after
                c = line.find(char) + 1
                t = line[c]
                match t:
                    case "\\":
                        print("Found a single backslash")
                    case "\"":
                        print("Found a single double quote")
                    case "x":
                        print("Found the ascii stuff")







print(f(x=open("input.txt", "r")))

