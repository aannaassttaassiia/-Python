# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    total = 0
    for item in data:
        total += item["score"] * item["weight"]
    return round(total, 3)

print(task())
