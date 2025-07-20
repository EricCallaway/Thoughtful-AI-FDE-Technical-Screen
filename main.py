from src.factory import Factory
from src.package import Package
from src.stack import Stack

import csv

if __name__ == "__main__":
    # Generate Factory Object
    main_factory = Factory(name="Thouhgtful AI: Robotic Factory")

    with open('data/input.csv', mode='r', newline='') as file:
        file_reader = csv.reader(file)
        next(file_reader)   # We need to skip the header file

        for row in file_reader:
            width, height, length, mass = float(row[0]), float(row[1]), float(row[2]), float(row[3])
            try:
                print(main_factory.sort_package(width=width, height=height, length=length, mass=mass))
            except Exception as e:
                print(e)
