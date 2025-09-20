from tkinter import *
from datetime import *
import sqlite3

product_list = [
    {"title": "milk","brand": "pak","price": 90000, "expiredate": date(2025, 10, 1)},
    {"title": "pickle","brand": "badr","price": 50000, "expiredate": date(2026, 2, 10)},
    {"title": "ice cream","brand": "mihan","price": 30000, "expiredate": date(2024, 10, 6)},
    {"title": "cheese","brand": "roozaneh","price": 60000, "expiredate": date(2025, 11, 13)},
    {"title": "bread","brand": "senan","price": 80000, "expiredate": date(2025, 3, 8)},
]




def show_expired():

    window = Tk()
    window.title("Expired products")
    window.geometry("400x400")
    window.configure(bg="lavender")
    y=20

    expired_list = []

    for product in product_list:
        if product["expiredate"] < datetime.now().date():
            expired_list.append(product)

    lable_style = {"bg": "lavender", "fg": "MediumPurple4", "font": ("Gill sans", 14)}

    if expired_list:
        Label(window, text="Expired products", **lable_style).place(x=20, y=y)
        y += 30
        for product in expired_list:
            Label(window, text=product["title"], **lable_style).place(x=20, y=y)
            y += 30
    else:
        Label(window, text="No expired products.", **lable_style).place(x=20, y=y)

    window.mainloop()

def product_table():
    connection = sqlite3.connect("product.db") 
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS product(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   brand TEXT,
                   price INTEGER,
                   expiredate TEXT)
    ''')
    connection.commit()
    connection.close() 

    data = [
    ('milk', 'pak', 90000, '2025-10-01'),
    ('pickle', 'badr', 50000, '2025-02-10'),
    ('ice cream', 'mihan', 30000, '2024-10-06'),
    ('cheese', 'roozaneh', 60000, '2025-11-13'),
    ('bread', 'senan', 80000, '2025-03-08')
]

    connection = sqlite3.connect("product.db") 
    cursor = connection.cursor()
    cursor.execute('''
                INSERT INTO product(title,brand,price,expiredate)
                VALUES(?,?,?,?)
    ''', data) 
    connection.commit()
    connection.close() 