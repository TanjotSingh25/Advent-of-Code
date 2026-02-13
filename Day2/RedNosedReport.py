import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    safeReportCount = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            levels = line.split(" ")

            isSafe = True
            increasing = int(levels[0]) < int(levels[1])
            for i in range(1, len(levels)):
                if increasing:
                    diff = int(levels[i]) - int(levels[i - 1])
                    if diff < 1 or diff > 3:
                        isSafe = False
                        break
                else:
                    diff = int(levels[i - 1]) - int(levels[i])
                    if diff < 1 or diff > 3:
                        isSafe = False
                        break
            if isSafe:
                safeReportCount += 1

    print(f"Number of safe reports: {safeReportCount}")    


if __name__ == "__main__":    main()