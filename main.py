from prettytable import PrettyTable

order = 0
quantity = 0
sub_total = 0
tax = 0
total = 0
chang = 0

stor_name = 'OUT WORLD CLEAN\t  '
location = '\nLocation:\n12574 Nest-Side Drive\nWater Bowl, Moon 77777'
phone = '\nPhone:\n(000) 794 562 54'

table = PrettyTable([stor_name])

products = open('database.txt', 'r')
print('Products\n' + products.read())
print()

print("To submit your order press ctrl + c")
print()
# Order loop.
while True:
    try:
        number = input('Please enter a 5 digit number from list of products above: ').strip()
        if number == '':
            continue
    except:
        print()
        print('Here is your order.')
        break
    found = False
    with open('database.txt', 'r') as f:
        for i in f.readlines():
            w = i.split('\t')
            if w[0].strip() == number:
                found = True
                print(i)
                order = i.strip()
                cost = float(i.strip('\t')[-6:])
                break
        if not found:
            print('Sku not found. Please input the given sku. ')
            continue

    table.add_row([order])
    sub_total += cost
    tax = round(sub_total * 0.09, 2)
    total = round(sub_total + tax, 2)


table.add_row(['----\t----\t----\t----'])
table.add_row(['sub_total\t\t' + '$' + str(sub_total)])
table.add_row(['tax\t\t\t' + '$' + str(tax)])
table.add_row(['total\t\t\t' + '$' + str(total)])
print(table)
print()

# payment only_number loop
while True:
    try:
        while True:
            try:
                print('To delete your order enter ctrl + c.')
                print()
                pay = float(input('The cost with tax is $' + str(total) + ' pay here:  '))
                break

            except ValueError:
                print('input only numbers.')

        print()
        chang = round(pay - total, 2)

        print()

        # When payment is too low.
        while True:
            if pay < total:
                own = round(total - pay, 2)
                try:
                    ask_again = float(input('you are $' + str(own) + ' short: '))
                    pay += round(ask_again, 2)
                    chang = round(pay - total, 2)
                    if pay >= total:
                        break

                except ValueError:
                    print('please input numbers.')

            elif pay >= total:
                break

        print()
        print('Your recipe...')
        table.add_row(['Pay\t\t\t' + '$' + str(pay)])
        table.add_row(['chang\t\t\t' + '$' + str(chang)])
        print(table)
        break
    except KeyboardInterrupt:
        print()
        print('THANK YOU FOR SHOPPING')
        break
