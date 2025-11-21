with open("/usr/include/X11/cursorfont.h", "r") as cursorfont:
    lines = cursorfont.readlines()
    useful_lines = [line for line in lines if "#" in line]
    parsed_lines = []
    for line in useful_lines:
        if "XC_" in line:
            parsed_temp = line.split()[1][3:]
            parsed_lines.append(parsed_temp)

with open("output.csv", "x") as output:
    for word in parsed_lines:
        output.write(f"{word}\n")

print(parsed_lines)