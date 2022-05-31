from datetime import date
from kivy.properties import ObjectProperty
from billClass import Bill

def create_new_bill(name : str, members : list, participation : list):
    aux_member = list()
    #TODO change this to be a received value
    create_day = date.today()

    if len(name) > 0 and len(name) < 50 and name.isidentifier():
        name = name.strip()
        name = name.lower()
        name = name.capitalize()
    
    else:
        return False

    if len(members) == len(participation) and len(members) > 0:
        for (member, contribution) in zip(members, participation):
            if type(member) == str:
                member = member.strip()
                member = member.lower()
                member = member.capitalize()
                aux_member.append([member, int(contribution)])
            else:
                return False

    day = create_day.day
    month = create_day.month
    year = create_day.year

    new_bill = Bill(name, aux_member, day, month, year)
    return new_bill