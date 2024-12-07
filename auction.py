logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

# using list

names =[]
bids = []
i=True
while(i):
    print(i)
    name = input('what is your name?\n')
    names.append(name)
    bid = input('what is your bid? \n')
    bids.append(bid)
    choice = input('Are there any other bidders? (type yes or no) \n')
    if choice == 'yes':
        continue
    else:
        ans = bids.index(max(bids))
        print(f'The winner is {names[ans]} with bid of {bids[ans]}')
        i=False


# using dictionary

details = {}
i=True
while(i):
    name = input('what is your name?\n')
    bid = int(input('what is your bid? \n'))
    details[name] = bid
    choice = input('Are there any other bidders? (type yes or no) \n')
    if choice == 'yes':
        continue
    else:
        ans = max(details.values())
        for key,val in details.items():
            if ans == val:
                print(f'The winner is {key} with bid of {ans}')
        i=False