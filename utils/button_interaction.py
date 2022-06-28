from datetime import date
#from billClass import Bill
#import functions

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

    for member in members:
        if members.count(member) == 1:
            pass
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