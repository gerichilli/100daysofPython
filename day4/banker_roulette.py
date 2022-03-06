import random

def who_will_pay():
    names_string = input('Give me everybody\'s names, separated by a comma and a space.\n')
    names = names_string.split(', ')
    # rand_num = random.randint(0,(len(names) - 1))
    # person_will_pay = names[rand_num]

    person_will_pay = random.choice(names)
    print(f'{person_will_pay} will pay for the meal')

who_will_pay()