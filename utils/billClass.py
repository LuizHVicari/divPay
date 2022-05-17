class Bill:
    def __init__(self, name : str, members : dict, day : int, month : int, year : int, participation : list):
        self.name = name
        self.members = members
        self.day = day
        self.month = month
        self.year = year
        self.participation = participation
        self.value = 0


    def new_payment(self, value : float, name : str):
        if value > 0 and name in self.members.keys():
            self.value += value
            self.members[name] += value
            return True
        return False


    def get_name(self):
        return self.name


    def get_members(self):
        info = str()
        for member in self.members:
            info += 'member '
        return info

    
    def get_day(self):
        return self.day

    
    def get_month(self):
        return self.month


    def get_year(self):
        return self.year


    def get_date(self):
        return '{self.day}}/{self.month}/{self.year}'


    def bill_info(self):
        info = f'Name: {self.name} \nCreated on: {self.day}/{self.month}/{self.year}'

        for member in self.members:
            info += f'\nMember: {member}'
        for participation in self.participation:
            info += f'\nParticipation (in order): {participation}'
        info += f'\nValue: {self.value}'
        
        return info

    