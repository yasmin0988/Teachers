import sqlite3

teachers_data = [
    {"lecture": "python", "lecturer": "Molaie", "units": 4},
    {"lecture": "python", "lecturer": "Rezaie", "units": 7},
    {"lecture": "python", "lecturer": "Mohammadi", "units": 3},
    {"lecture": "java", "lecturer": "Molaie", "units": 9},
    {"lecture": "java", "lecturer": "Rezaie", "units": 8},
    {"lecture": "java", "lecturer": "Mohammadi", "units": 4},
    {"lecture": "c++", "lecturer": "Molaie", "units": 1},
    {"lecture": "c++", "lecturer": "Mohammadi", "units": 5},
]

def init_database():
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lecture TEXT,
            lecturer TEXT, 
            units INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_teachers_data(data_list):
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()
    
    for teacher in data_list:
        cursor.execute('''
            INSERT INTO teachers (lecture, lecturer, units)
            VALUES (?, ?, ?)
        ''', (teacher['lecture'], teacher['lecturer'], teacher['units']))
    
    conn.commit()
    conn.close()

def add_teacher(lecture, lecturer, units):
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO teachers (lecture, lecturer, units)
        VALUES (?, ?, ?)
    ''', (lecture, lecturer, units))

    conn.commit()
    conn.close()

def delete_teacher(id_):
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM teachers WHERE id = ?''', (id_,))

    conn.commit()
    conn.close()

def edit_teacher(id_, new_lecture, new_lecturer, new_units):
    conn = sqlite3.connect('table.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE teachers
        SET lecture = ?, lecturer = ?, units = ?
        WHERE id = ?
    ''', (new_lecture, new_lecturer, new_units, id_))

    conn.commit()
    conn.close()


init_database()
insert_teachers_data(teachers_data)
add_teacher("c++", "rezaie", 2)
delete_teacher(10)


# import sqlite3

# connection = sqlite3.connect('table.db')
# cursor = connection.cursor()

# cursor.execute('''
# create table if not exists teachers(
#                id integer primary key AUTOINCREMENT,
#                lecture text,
#                lecturer text,
#                units integer
# )              
# ''')

# cursor.execute('''
#     insert into teachers(lecture,lecturer, units)
#     values (?, ?, ?)
#     ('python', 'molaie', 4)
#     ('python', 'rezaie', 7)
#     ('python', 'mohammadi', 3)
#     ('java', 'molaie', 9)
#     ('java', 'rezaie', 8)
#     ('java', 'mohammadi', 4)
#     ('c++', 'molaie', 1)
#     ('c++', 'mohammadi', 5)
# ''')

# connection.commit()
# connection.close()