phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

print phonebook_dict['Alice']
phonebook_dict['Kareem'] = "938-489-1234"
print phonebook_dict['Kareem']
del phonebook_dict['Alice']
print phonebook_dict.get('Alice')
phonebook_dict['Bob'] = "968-345-2345"
print phonebook_dict['Bob']
entries = phonebook_dict.items()
print entries
