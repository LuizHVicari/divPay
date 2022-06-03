from datetime import date
from billClass import Bill
import functions

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
    if len(name) > 0 and len(name) < 50 and name.isidentifier():
        name = name.strip()
        name = name.lower()
        name = name.capitalize()
    
    else:
        return False
    
    # Validates the members and their participation
    if len(members) == len(participation) and len(members) == len(payments) and len(members) > 0:
        for (member, contribution, pay) in zip(members, participation, payments):
            if type(member) == str:
                member = member.strip()
                member = member.lower()
                member = member.capitalize()
            else:
                return False
            
            contribution = functions.validate_int(contribution)
            if contribution <= 0:
                print(contribution)
                return False

            pay = functions.validate_float(pay)
            if pay < 0:
                return False
            
            value += pay
            
            aux_member.append([member, contribution, pay])
    else:
        return False

    if month > 12:
        return False
    
    if day > 31:
        return False
    elif day > 30 and month == 4 or month == 6 or month == 9 or month == 11:
        return False
    elif day > 28 and year % 4 != 0 and month == 2:
        return False
    elif day > 29 and month == 2:
        return False
    elif day < 0 or month < 0 or year < 0:
        return False

    return Bill(name, aux_member, value, day, month, year)