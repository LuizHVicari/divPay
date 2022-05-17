from datetime import date
from asyncio.windows_events import NULL
from kivy.properties import ObjectProperty
from billClass import Bill

def create_new_bill(name : str, members : list, participation : list):
    aux_member = dict()
    aux_participation = list()

    #name = ObjectProperty(None)
    #members = ObjectProperty(None)
    #participation = ObjectProperty(None)

    if len(name) > 0 and len(name) < 50 and name.isidentifier():
        name = name.capitalize()
        name = name.strip()
    
    else:
        return False

    for member in members:
        if len(member) > 0 and len(member) < 50 and member.isidentifier():
            member = member.capitalize()
            member = member.strip()  
            aux_member.update({member : 0})
        else:
            return False

    for member_part in participation:
        if member_part.isnumeric() and int(member_part) > 0 and int(member_part) == float(member_part):
            aux_participation.append(int(member_part))
        else:
            return False
    
    create_day = date.today()
    day = create_day.day
    month = create_day.month
    year = create_day.year

    new_bill = Bill(name, aux_member, day, month, year, participation)
    return new_bill