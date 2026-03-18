import sys
import time

# Using Recursion 
def canMatchTarget(target, numbers):
    def search(index, currentValue):
        if currentValue > target:
            return False

        if index == len(numbers):
            return currentValue == target

        nextNumber = numbers[index]

        return (
            search(index + 1, currentValue + nextNumber)
            or search(index + 1, currentValue * nextNumber)
        ) 
    
    return search(1, numbers[0])

# Parse the line and convert int and [int]
def parseEquation(line):
    targetText, numbersText = line.strip().split(":")
    target = int(targetText)
    numbers = [int(value) for value in numbersText.split()]
    return target, numbers


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "input.txt"

    total = 0

    # METRIC MANAGEMENT
    recordCount = 0
    startTime = time.perf_counter()


    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                
                # METRIC MANAGEMENT
                recordCount += 1

                target, numbers = parseEquation(line)

                if canMatchTarget(target, numbers):
                    total += target

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
        return
    except OSError as error:
        print(f"Error: Could not read '{filename}': {error}")
        return  
    
    endTime = time.perf_counter()

    print("Results")
    print(f"Number of records: {recordCount}")
    print(f"Total calibration result: {total}")
    print(f"Time taken: {endTime - startTime:.6f} seconds")


if __name__ == "__main__":
    main()