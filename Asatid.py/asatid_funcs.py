def sort_by_name(course_list):

    def get_lecturers_name(course):
        return course["lecturer"]
    
    return sorted(course_list, key = get_lecturers_name)

def add_units(total, course):
    lecturer = course["lecturer"]
    if lecturer in total:
        total[lecturer] += course["units"]
    else:
        total[lecturer] = course["units"]
    return total

def print_totals(lecturer_units):
    lecturers = []
    for lecturer in lecturer_units:
        lecturers.append(lecturer)
    lecturers.sort()
    
    for lecturer in lecturers:
        total = lecturer_units[lecturer]
        print(f"{lecturer:12} | {'TOTAL':9} | {total:5}")