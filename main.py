from src.factory import Factory
from src.package import Package
from src.stack import Stack

import csv

if __name__ == "__main__":
    
    def validate(row) -> bool:
        if len(row) < 4:
            return False
        for r in row:
            invalid_strings = {'None', ''}
            if r in invalid_strings:
                return False

            if not r.isnumeric():
                return False

            if '"' in r:
                r = r.strip('"')

        return True

    # Generate Factory Object
    main_factory = Factory(name="Thouhgtful AI: Robotic Factory")
    with open('data/packages.csv', mode='r', newline='') as file:
        total_packages = 0
        file_reader = csv.reader(file)
        for _ in file_reader:
            total_packages += 1

    with open('data/packages.csv', mode='r', newline='') as file:
        file_reader = csv.reader(file)
        next(file_reader)   # We need to skip the header file

        standard_stack = []
        rejected_stack = []
        special_stack = []
        for idx, row in enumerate(file_reader):
            if validate(row):
                width, height, length, mass = float(row[0]), float(row[1]), float(row[2]), float(row[3])
                try:
                    package = main_factory.sort_package(width=width, height=height, length=length, mass=mass)
                    if package[0] == 'standard':
                        standard_stack.append(package)
                    elif package[0] == 'rejected':
                        rejected_stack.append(package)
                    else:
                        special_stack.append(package)

                except Exception as e:
                    print(e)

        num_standard_stack = len(standard_stack)
        num_rejected_stack = len(rejected_stack)
        num_special_stack = len(special_stack)
        print('-'*50)
        print('Beginning of Report')
        print('-'*50)
        print(f"Number of packages in standard stack {num_standard_stack}")
        print(f"Number of packages in rejected stack {num_rejected_stack}")
        print(f"Number of packages in special stack {num_special_stack}")
        print('-'*50)
        standard_stack_perc = num_special_stack / total_packages
        rejected_stack_perc = num_rejected_stack / total_packages
        special_stack_perc = num_special_stack / total_packages
        print(f"Percentage of Standard Stack: {standard_stack_perc}")
        print(f"Percentage of Rejected Stack: {rejected_stack_perc}")
        print(f"Percentage of Special Stack: {special_stack_perc}")
        print('-'*50)
        print(f"Standard Stack minimum mass: {min(stack[1] for stack in standard_stack)}")
        print(f"Rejected Stack minimum mass: {min(stack[1] for stack in special_stack)}")
        print(f"Special Stack minimum mass: {min(stack[1] for stack in rejected_stack)}")
        print('-'*50)
        print(f"Standard Stack maximum mass: {max(stack[1] for stack in standard_stack)}")
        print(f"Rejected Stack maximum mass: {max(stack[1] for stack in special_stack)}")
        print(f"Special Stack maximum mass: {max(stack[1] for stack in rejected_stack)}")

        standard_stack_avg_mass = sum(stack[1] for stack in standard_stack) / len(standard_stack) 
        rejected_stack_avg_mass = sum(stack[1] for stack in rejected_stack) / len(rejected_stack)
        special_stack_avg_mass = sum(stack[1] for stack in special_stack) / len(special_stack)
        print('-'*50)
        print(f"Standard Stack Average Mass: {standard_stack_avg_mass}")
        print(f"Rejected Stack Average Mass: {rejected_stack_avg_mass}")
        print(f"Special Stack Average Mass: {special_stack_avg_mass}")

        standard_stack_avg_vol = sum(stack[2] for stack in standard_stack) / len(standard_stack) 
        rejected_stack_avg_vol = sum(stack[2] for stack in rejected_stack) / len(rejected_stack)
        special_stack_avg_vol = sum(stack[2] for stack in special_stack) / len(special_stack)
        print('-'*50)
        print(f"Standard Stack Average Volume: {standard_stack_avg_vol}")
        print(f"Rejected Stack Average Volume: {rejected_stack_avg_vol}")
        print(f"Special Stack Average Volume: {special_stack_avg_vol}")
        

"""
1. Ingest new packages.csv
2. Sub procedure to validate input data

Validation criteria
1. Data type: {float || int}
2. Needs to be positive

strip ("")
watch out for NULL col bc you are casting as float

Reports
- Total number of pckgs (total_packages)
    - Not exclusive to valid packages 
- calc_perc_<stack>
    - Take the num_packages in a stack / total_packages
- calc_avg_min (mass and vol)
- calc_avg_max (mass and vol)

Display
- Output in terminal, make legible
"""