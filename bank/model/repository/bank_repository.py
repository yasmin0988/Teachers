import sqlite3

class BankRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/bank.db")
        self.cusor = self.connection.cursor()

    def disconnect(self):
        self.cusor.close()
        self.connection.close()

    def save(self):
        self.connect()
        self.cursor.execute("insert into bank (name, description,) values (?,?)")
        self.disconnect()
    
    def update(self):
        self.connect()
        self.cursor.execute("update bank name=?, description=?, where id=?")
        self.connection.commit()
        self.disconnect()
    
    def delete(self):
        self.connect()
        self.cursor.execute("delete from bank where id=?")
        self.connection.commit()
        self.disconnect()
    
    def find_all(self):
        self.connect()
        self.cursor.execute("select * from bank")
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]     #TODO
        self.connection.commit()
        self.disconnect()
    
    def find_by_id(self):
        self.connect()
        self.cursor.execute("select * from bank where id=?")
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]     #TODO
        self.connection.commit()
        self.disconnect()