def love_calculator():
    print('Welcome to the Love Calculator!')
    name1 = input('What is your name? \n').lower()
    name2 = input('What is their name? \n').lower()
    combine_name = name1 + name2

    true_count = 0
    love_count = 0

    for letter in 'true':
        true_count += combine_name.count(letter)
    
    for letter in 'love':
        love_count += combine_name.count(letter) 

    love_scores = int(f'{true_count}{love_count}')
    
    if love_scores < 10 or love_scores > 90:
        print(f'Your score is {love_scores}, you go together like coke and mentos.')
    elif 40 <= love_scores <= 50:
        print(f'Your score is {love_scores}, you are alright together.')
    else:
        print(f'Your score is {love_scores}')

love_calculator()