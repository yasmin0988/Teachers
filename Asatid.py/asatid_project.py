from asatid_funcs import *
from functools import reduce


classes_list = [
    {"lecture" : "python", "lecturer" : "Molaie", "units" : 4},
    {"lecture" : "python", "lecturer" : "Rezaie", "units" : 7},
    {"lecture" : "python", "lecturer" : "Mohammadi", "units" : 3},
    {"lecture" : "java", "lecturer" : "Molaie", "units" : 9},
    {"lecture" : "java", "lecturer" : "Rezaie", "units" : 8},
    {"lecture" : "java", "lecturer" : "Mohammadi", "units" : 4},
    {"lecture" : "c++", "lecturer" : "Molaie", "units" : 1},
    {"lecture" : "c++", "lecturer" : "Mohammadi", "units" : 5},
]

sorted_classes = sort_by_name(classes_list)
lecturer_units = reduce(add_units, classes_list, {})

print(f"{'Lecturer':12} | {'Lecture':9} | {'Units':5}")
print("-" * 32)

for class_ in sorted_classes:
    print(f"{class_['lecturer']:12} | {class_['lecture']:9} | {class_['units']:5}")

print("-" * 32)

print_totals(lecturer_units)