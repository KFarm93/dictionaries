import pickle
from os.path import exists
if exists("phonebook.pickle"):
        phonebook_file = open('phonebook.pickle', 'r')
        phonebook = pickle.load (phonebook_file)
        phonebook_file.close()
else:
    phonebook = {}

while True:
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save entries"
    print "6\. Quit"


    numSelected = int(raw_input("What do you want to do (1-6)? "))

    if numSelected == 1:
        name = raw_input("Who would you like to look up? ")
        if name in phonebook:
            print phonebook[name]
        else:
            print "%s is not in the phonebook." % name
    elif numSelected == 2:
        nameGiven = raw_input("Who would you like to set? ")
        numGiven = raw_input("What is their phone number? ")
        phonebook[nameGiven] = numGiven
        print "Entry for %s made." % nameGiven
    elif numSelected == 3:
        toDelete = raw_input("Whose entry should be deleted? ")
        del phonebook[toDelete]
        print "Entry %s deleted." % toDelete
    elif numSelected == 4:
        for name, number in phonebook.items():
            print "Found %s's number: %s" % (name, number)
    elif numSelected == 5:
        phonebook_file = open('phonebook.pickle', 'w')
        pickle.dump(phonebook, phonebook_file)
        phonebook_file.close()
        print "Entries saved."
    elif numSelected == 6:
        print "Goodbye."
        break
    else:
        print "Invalid input."
