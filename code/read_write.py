import csv
import os

def read(name):
    """Read the file with the name argument"""
    info = []
    with open(f".\\information\\{name}.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            info.append(row)
        return info      