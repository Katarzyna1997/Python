try:
    name, surname, year = input('Enter name, surname, year (e.g. Katarzyna Mrugała 1997): ').split()
    print('Your data: ', name, surname, year)
except ValueError:
    print('Enter the data in the correct format ("Katarzyna Mrugała 1997")')