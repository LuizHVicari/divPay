class Bill:
    def __init__(self, name : str, members : dict, value : float, day : int, month : int, year : int):
        '''
        Builder for the Bill class
        @param name: name of the bill
        @param members: list of members
        @param value: total value of the bill
        @param day: day of the bill, month: month of the bill
        @param year: year of the bill
        @return a new Bill object
        '''
        self.name = name
        self.members = members
        self.day = day
        self.month = month
        self.year = year
        self.value = value
        self.weight = 0
        self.payments = list()
        Bill.calculate(self)
        
    def new_payment(self, value : float, name : str):
        '''
        Executes a new payment for the bill
        @param value: value of the payment, name: name of the member	
        @return True if the payment was successful, False otherwise
        '''
        if value > 0 and name in self.members.keys():
            self.value += value
            self.members[name] += value
            return True
        return False

    def calculate(self):
        '''
        Calculates how much each member should pay
        @return a list of lists with the name of the member and the value to pay
        '''
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

    def bill_info_string(self):
        '''
        @return a string with the information of the bill
        '''
        info = f'Name: {self.name} \nCreated on: {self.day}/{self.month}/{self.year}'
        for member in self.members:
            info += '\n' + member[0] + f': contribution: {member[1]}, payed: {member[2]}'
        
        return info

    def bill_info_list(self):
        '''
        @return a string with the information of the bill
        '''
        return [self.name, self.members, self.value, self.payments,self.day, self.month, self.year]
