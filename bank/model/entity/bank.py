class Bank:
    def __init__(self, title=str, branch=str,
                  description=str, balance= int, employee_number = int):
        self.title = title
        self.branch = branch
        self.description = description
        self.balance = balance
        self.employee_number = employee_number
    
    def __repr__(self):
        return f"{self.__dict__}"