#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇``
def tip_calculator():
    bill = input('Please input the bill price: ')
    tip = input('Tip percentage: ')
    people_num = input('How many people should pay for the bill: ')

    if(bill.isnumeric() and tip.isnumeric() and people_num.isnumeric()):
        bill_per_person = (float(bill) / float(people_num)) * (float(tip) / 100 + 1)
        result = '{:.2f}'.format(bill_per_person)
        print(result)
        return result

tip_calculator()