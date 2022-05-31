from datetime import date
from billClass import Bill
import functions

def create_new_bill(name : str, members : list, participation : list, payments : list):
    aux_member = list()
    #TODO change this to be a received value
    creation_day = date.today()
    value = 0

    if len(name) > 0 and len(name) < 50 and name.isidentifier():
        name = name.strip()
        name = name.lower()
        name = name.capitalize()
    
    else:
        return False

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

    day = creation_day.day
    month = creation_day.month
    year = creation_day.year

    new_bill = Bill(name, aux_member, value, day, month, year)
    return new_bill