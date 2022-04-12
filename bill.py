from datetime import datetime
from pathlib import PurePath
from user import User
from purchase import Purchase


class Bill:
    # Builder
    def __init__(self, name : str, members : list()):
        self.name = name
        self.value =float(0)
        self.initDate = datetime.today()
        self.memberDict = dict()
        for member in members:
            newMember = {member, 0}
            memberDict.update(newMember)


    def addMember(self, member : User):
        self.memberDict.append([member, 0, datetime.today()])

    def removeMember(self, member : User):
        self.memberDict.pop(member)

    def newPurchase(self, purchase : Purchase):
        self.memberDict{purchase.owner}