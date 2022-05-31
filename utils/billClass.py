# TODO: criar o método para dividir as contas 
class Bill:
    def __init__(self, name : str, members : dict, day : int, month : int, year : int):
        self.name = name
        self.members = members
        self.day = day
        self.month = month
        self.year = year
        self.value = 0

    def new_payment(self, value : float, name : str):
        if value > 0 and name in self.members.keys():
            self.value += value
            self.members[name] += value
            return True
        return False

    # function to pay off the debt between members
    def pay_debt():
        pass

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

    def bill_info(self):
        info = f'Name: {self.name} \nCreated on: {self.day}/{self.month}/{self.year}'
        for member in self.members:
            info += '\n' + member[0] + f': {member[1]}'
        
        return info

    