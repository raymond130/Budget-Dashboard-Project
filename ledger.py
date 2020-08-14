# main accounting ledger for the budget tool
# keeps item name, description, category,  debit/credit,  notes, entry date, and last entry date
# works  with the file ledger.txt

import json
import os


# creates ledger_entry class with a contsructor that includes the relevant information
# ledger_output will be a dictonary with the relevant information
# another ledger constructor (for reading from the JSON) will take a dictionary and construct an object

# reads current ledger first, then allows modification and creation

# todo: open and read in ledger entries on file initialization - only reads in the JSON dict
#   must create a backup of the ledger first
# modifying ledger entries by reading an entry from the dictionary returned by the json read and overwriting the dict entries
#   first creates a new ledger entry with the information from the json dump
#   modifies the information as necessary
#   outputs the data as a dict, then overwriters the relevant ledger entry
#   refers to ledger entries by number
# outputting to the ledger in a json format

class Account:
    def __init__(self, json_dict=None, ledger=[], name="", total_amount=0, periodicEntries=[]):
        if json_dict is not None:
           self.ledger = json_dict['ledger']
           self.name = json_dict['name']
           self.total_amount = json_dict['total_amount']
           self.periodic_entries = json_dict['periodic_entries']
        else:
            self.ledger = []
            self.name = ""
            self.total_amount = 0
            self.periodic_entries = []


class ledger_list:

    def __init__(self,json = None, entries = None):
        if (json is not None):
            self.entries = jason['entries']


class ledger_entry:
    def __init__(self, ledger, json=None, number=0, name=None, description=None \
                 , category=None, debit_credit=None, notes=None, entry_date=None, last_update_date=None):
        if (json is not None):
            self.ledger = json['ledger']
            self.number = json["number"]
            self.name = json["name"]
            self.description = json["description"]
            self.category = json["category"]
            self.debit_credit = json["debit_credit"]
            self.notes = json["notes"]
            self.entry_date = json["entry_date"]
            self.last_update_date = json["last_update_date"]

        else:
            self.ledger = ledger
            self.number = number
            self.name = name
            self.description = description
            self.category = category
            self.debit_credit = debit_credit
            self.notes = notes
            self.date = entry_date
            self.update_date = last_update_date

    def printOut(self):
        printed = {
            "ledger": self.leger,
            "number": self.number,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "debit_credit": self.debit_credit,
            "notes": self.notes,
            "entry_date": self.entry_date,
            "last_update_date": self.last_update_date
        }

        return printed


def new_ledger_entry(account, entry):
    # adds a new ledger entry, sets the number of the ledger entry after the number of the last entry in ledger
    num = str(len(account.ledger))
    account.ledger.update(num, entry)


def cash_Update(account, amount):
    account.total_amount = amount


def add_periodical(ledger, entry):
    ledger['periodic entries'].update(str(len(ledger['periodic entries'])), entry)


ledger = {}
ledger['entries'] = []
ledger["index"] = 0
ledger['remaining budget'] = 0
ledger['periodic entries'] = []



with open('fileledger.txt', 'w+') as ledgerFile:
    if os.stat('fileledger.txt').st_size > 0:
        data = json.load(ledgerFile)
    else:
        data = ''
ledger = data

with open('ledger.txt.', 'w') as fileout:
    storedData = json.dumps((ledger))
    json.dump(storedData, fileout)
