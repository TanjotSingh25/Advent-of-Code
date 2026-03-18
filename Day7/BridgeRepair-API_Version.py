from pathlib import Path
import time

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel


app = FastAPI(title="Bridge Repair API")


class BridgeRepairResponse(BaseModel):
    part: int
    filename: str
    recordCount: int
    totalCalibrationResult: int
    timeTakenSeconds: float


def canMatchTargetPart1(target, numbers):
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


def canMatchTargetPart2(target, numbers):
    def search(index, currentValue):
        if currentValue > target:
            return False

        if index == len(numbers):
            return currentValue == target

        nextNumber = numbers[index]
        concatNumber = int(str(currentValue) + str(nextNumber))

        return (
            search(index + 1, currentValue + nextNumber)
            or search(index + 1, currentValue * nextNumber)
            or search(index + 1, concatNumber)
        )

    return search(1, numbers[0])


def parseEquation(line):
    targetText, numbersText = line.strip().split(":")
    target = int(targetText)
    numbers = [int(value) for value in numbersText.split()]
    return target, numbers


def readInputFile(filename):
    filePath = Path(filename)

    if not filePath.exists():
        raise HTTPException(status_code=404, detail=f"File '{filename}' was not found.")

    if not filePath.is_file():
        raise HTTPException(status_code=400, detail=f"'{filename}' is not a valid file.")

    try:
        with filePath.open("r", encoding="utf-8") as file:
            return [line for line in file if line.strip()]
    except PermissionError:
        raise HTTPException(status_code=500, detail=f"Permission denied while reading '{filename}'.")
    except OSError:
        raise HTTPException(status_code=500, detail="Error reading input file.")


@app.get("/bridge-repair/solve", response_model=BridgeRepairResponse)
def solveBridgeRepair(
    part: int,
    filename: str = "input.txt",
):
    if part not in (1, 2):
        raise HTTPException(status_code=400, detail="Part must be 1 or 2.")

    startTime = time.perf_counter()
    lines = readInputFile(filename)

    total = 0
    recordCount = len(lines)

    try:
        for line in lines:
            target, numbers = parseEquation(line)

            if part == 1:
                if canMatchTargetPart1(target, numbers):
                    total += target
            else:
                if canMatchTargetPart2(target, numbers):
                    total += target
    except ValueError:
        raise HTTPException(status_code=500, detail="Invalid equation format in input file.")
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected processing error occurred.")

    endTime = time.perf_counter()

    return BridgeRepairResponse(
        part=part,
        filename=filename,
        recordCount=recordCount,
        totalCalibrationResult=total,
        timeTakenSeconds=round(endTime - startTime, 6),
    )