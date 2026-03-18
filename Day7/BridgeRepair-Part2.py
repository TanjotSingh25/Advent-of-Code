# Using Recursion 
def canMatchTarget(target, numbers):
    def search(index, currentValue):
        if currentValue > target:
            return False

        if index == len(numbers):
            return currentValue == target

        nextNumber = numbers[index]

        concatNumber  = int(str(currentValue) + str(numbers[index]))
        return (
            search(index + 1, currentValue + nextNumber)
            or search(index + 1, currentValue * nextNumber)
            or search(index + 1, concatNumber) 
        ) # Using the Concatinated numbers at the end to have the + and * branches take care of equations that can be solved by just + and *

    return search(1, numbers[0])

# Parse the line and convert int and [int]
def parseEquation(line):
    targetText, numbersText = line.strip().split(":")
    target = int(targetText)
    numbers = [int(value) for value in numbersText.split()]
    return target, numbers


def main():
    total = 0

    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            target, numbers = parseEquation(line)

            if canMatchTarget(target, numbers):
                total += target

    print(f'Total: {total}')


if __name__ == "__main__":
    main()