from datetime import date
from pickletools import read_uint1
from billClass import Bill
import functions

def create_new_bill(name : str, members : list, participation : list, payments : list):
    aux_member = list()
    #TODO change this to be a received value
    create_day = date.today()

    if len(name) > 0 and len(name) < 50 and name.isidentifier():
        name = name.strip()
        name = name.lower()
        name = name.capitalize()
    
    else:
        print('1')
        return False

    if len(members) == len(participation) and len(members) == len(payments) and len(members) > 0:
        for (member, contribution, pay) in zip(members, participation, payments):
            if type(member) == str:
                member = member.strip()
                member = member.lower()
                member = member.capitalize()
            else:
                print('2')
                return False
            
            contribution = functions.validate_int(contribution)
            if contribution <= 0:
                print(contribution)
                return False

            pay = functions.validate_float(pay)
            if pay < 0:
                print(pay)
                return False
            
            aux_member.append([member, contribution, pay])
    else:
        return False

    day = create_day.day
    month = create_day.month
    year = create_day.year

    new_bill = Bill(name, aux_member, 0, day, month, year)
    return new_bill