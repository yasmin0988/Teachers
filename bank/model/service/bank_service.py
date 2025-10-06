from repository.bank_repository import BankRepository


class BankService:
    def __init__(self):
        self.repository = BankRepository()
    
    def save(self, bank):
        self.repository.save(bank)

    def update(self, bank):
        self.repository.update(bank)
    
    def delete(self, bank):
        self.repository.delete(bank)

    def find_all(self, bank):
        self.repository.find_all(bank)

    def find_by_id(self, bank):
        self.repository.find_by_id(bank)
    