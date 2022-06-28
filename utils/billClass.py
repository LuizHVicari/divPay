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
        self.solved = False
        Bill.calculate(self)
        self.how_to_pay = Bill.how_to_pay(self)
        
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
            self.payments.append([member[0], round(must_pay, 2)])


    def edit_member_name(self, old_name : str, new_name : str):
        '''
        Edits the name of a member
        @param old_name: old name of the member	
        @param new_name: new name of the member
        @return True if the name was changed, False otherwise
        '''
        for member in self.members:
            if member[0] == old_name:
                member[0] = new_name
                return True
        return False
    
    def edit_member_contribution(self, name : str, value : int):
        '''
        Edits the contribution of a member
        @param name: name of the member	
        @param value: new value of the member
        @return True if the value was changed, False otherwise
        '''
        for member in self.members:
            if member[0] == name:
                member[1] = value
                return True
        return False
    
    def edit_member_pay(self, name : str, pay : float):
        '''
        Edits the pay of a member
        @param name: name of the member
        @param pay: new pay of the member
        @return True if the pay was changed, False otherwise
        '''
        for member in self.members:
            if member[0] == name:
                member[2] = pay
                return True
        return False

    def edit_bill_name(self, name : str):
        '''
        Edits the name of the bill
        @param name: new name of the bill
        @return True if the name was changed
        '''
        self.name = name
        return True
    
    def delete_member(self, name : str):
        '''
        Deletes a member from the bill
        @param name: name of the member
        @return True if the member was deleted, False otherwise
        '''
        for member in self.members:
            if member[0] == name:
                self.members.remove(member)
                return True

    def how_to_pay(self):
        '''
        Calculates how much each member should pay
        @return a list of tuples in the format: ("debitor's name", "creditor's name", value to pay)
        '''
        creditor = list()
        debitor = list()
        payments = list()
        for member in self.payments:
            if member[1] < 0:
                creditor.append(member)
            if member[1] > 0:
                debitor.append(member)

        creditor_index = 0
        debitor_index = 0

        while(creditor_index < len(creditor) and debitor_index < len(debitor)):
            if round(debitor[debitor_index][1], 2) == -round(creditor[creditor_index][1], 2):
                payments.append((debitor[debitor_index][0], creditor[creditor_index][0], debitor[debitor_index][1]))
                debitor[debitor_index][1] = 0
                creditor[creditor_index][1] = 0
                creditor_index += 1
                debitor_index += 1
            elif round(debitor[debitor_index][1], 2) < -round(creditor[creditor_index][1], 2):
                payments.append((debitor[debitor_index][0], creditor[creditor_index][0], debitor[debitor_index][1]))
                creditor[creditor_index][1] += debitor[debitor_index][1]
                creditor[creditor_index][1] = round(creditor[creditor_index][1], 2)
                debitor[debitor_index][1] = 0
                debitor_index += 1
            else:
                payments.append((debitor[debitor_index][0], creditor[creditor_index][0], -creditor[creditor_index][1]))
                debitor[debitor_index][1] += creditor[creditor_index][1]
                debitor[debitor_index][1] = round(debitor[debitor_index][1], 2)
                creditor[creditor_index][1] = 0
                creditor_index += 1

        print(payments)

        return payments
    
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
        return [self.name, self.members, self.value, self.payments, self.day, self.month, self.year]

###########################################################################################################################

from datetime import date

def create_new_bill(name : str, members : list, participation : list, payments : list, day : int, month : int, year : int):
    '''
    Creates a new bill
    @param name: name of the bill
    @param members: list of members
    @param participation: list of participation values
    @param payments: list of payments
    @return a new Bill object if it was succesfull, False otherwise
    '''
    aux_member = list()
    value = 0

    # Validates the name
    if len(name) >= 0 and len(name) < 50:
        name = name.strip()
        name = name.lower()
        name = name.capitalize()
    
    else:
        print(1)
        return False

    for member in members:
        if members.count(member) == 1:
            pass
        else:
            print(2)
            return False
    
    # Validates the members and their participation
    if len(members) == len(participation) and len(members) == len(payments) and len(members) > 0:
        for (member, contribution, pay) in zip(members, participation, payments):
            if type(member) == str:
                member = member.strip()
                member = member.lower()
                member = member.capitalize()
            else:
                print(3)
                return False
            
            contribution = validate_int(contribution)
            if contribution <= 0:
                print(contribution)
                print(4)
                return False

            pay = validate_float(pay)
            if pay < 0:
                print(5)
                return False
            
            value += pay
            
            aux_member.append([member, contribution, pay])
    else:
        print(6)
        return False

    print(8)

    return Bill(name, aux_member, value, day, month, year)

def edit_member_name(bill : Bill, old_name : str, new_name : str):
    ''' "
    Edits the name of a member
    @param bill: bill object
    @param old_name: old name of the member
    @param new_name: new name of the member
    @return True if the name was changed, False otherwise
    '''
    if type(new_name) == str:
            new_name = new_name.strip()
            new_name = new_name.lower()
            new_name = new_name.capitalize()
    else:
        return False

    for member in bill.members:
        if member[0] == new_name:
            return False

    for member in bill.members:
        if member[0] == old_name:
            member[0] = new_name
            return True
    return False

def edit_bill_name(bill : Bill, new_name : str):
    '''
    Edits the name of a bill
    @param bill: bill object
    @param new_name: new name of the bill
    @return True if the name was changed, False otherwise
    '''
    if type(new_name) == str:
            new_name = new_name.strip()
            new_name = new_name.lower()
            new_name = new_name.capitalize()
    else:
        return False

    bill.name = new_name
    return True

def solve_bill(bill : Bill):
    '''
    Solves a bill
    @param bill: bill object
    @return True if the bill was solved, False otherwise
    '''
    if bill.solved:
        return False
    else:
        bill.solved = True
        return True

def unsolve_bill(bill : Bill):
    '''
    Unsolves a bill
    @param bill: bill object
    @return True if the bill was unsolved, False otherwise
    '''
    if not bill.solved:
        return False
    else:
        bill.solved = False
        return True



def validate_int(string :str):
    try:
        return int(string)
    except:
        return -1


def validate_float(string : str):
    try:
        return float(string)
    except:
        return -1