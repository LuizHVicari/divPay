class Bill:
    def __init__(self, name : str, members : dict, value : float, day : int, month : int, year : int):
        self.name = name
        self.members = members
        self.day = day
        self.month = month
        self.year = year
        self.value = value
        self.weight = 0
        self.payments = list()
        Bill.calculate(self)
        

    #TODO chance this method so it works accordingly to the project
    def new_payment(self, value : float, name : str):
        if value > 0 and name in self.members.keys():
            self.value += value
            self.members[name] += value
            return True
        return False

    #TODO create this method to calculate how much the members should pay to each other
    def calculate(self):
        for member in self.members:
            self.weight += member[1]
        for member in self.members:
            must_pay = (self.value * member[1] / self.weight) - member[2]
            self.payments.append([member[0], must_pay])

    def get_name(self):
        return self.name

    def get_members(self):
        info = str()
        for member in self.members:
            info += f'{member}'
        return info
    
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_date(self):
        return f'{self.day}/{self.month}/{self.year}'

    def get_payments(self):
        return self.payments

    def bill_info(self):
        info = f'Name: {self.name} \nCreated on: {self.day}/{self.month}/{self.year}'
        for member in self.members:
            info += '\n' + member[0] + f': contribution: {member[1]}, payed: {member[2]}'
        
        return info
