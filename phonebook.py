import pickle


print "Electronic Phone Book"
print "====================="
print "1\. Look up an entry"
print "2\. Set an entry"
print "3\. Delete an entry"
print "4\. List all entries"
print "5\. Quit"

phonebook = {
'Steve': '629-826-0134',
'Britta': '217-264-1542',
'Sarah': '629-983-0956',
'Paul': '091-828-9070'
}

while True:
    numSelected = int(raw_input("What do you want to do (1-5)? "))
    if numSelected == 1:
        name = raw_input("Who would you like to look up? ")
        def look_up(x):
            print phonebook[x]
        look_up(name)
    elif numSelected == 2:
        nameGiven = raw_input("Who would you like to set? ")
        numGiven = raw_input("What is their phone number? ")
        def set_entry(y, z):
            phonebook[y] = [z]
        set_entry(nameGiven, numGiven)
    elif numSelected == 3:
        toDelete = raw_input("Who's entry should be deleted? ")
        def delete_entry(a):
            del phonebook[a]
        delete_entry(toDelete)
    elif numSelected == 4:
        print phonebook.items()
    elif numSelected == 5:
        print
    else:
        break
