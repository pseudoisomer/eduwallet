import math

# functions
def default_calc() :
    try:
        budget = int(input('what is your budget?\n\n'))
        food_budget = budget*0.3
        necessities_budget = budget*0.3
        transportation_budget = budget*0.1
        savings_budget = budget*0.15
        extra_budget  = budget*0.15
        print('\naccording to you budget, this is how much money you are able to spend on each category:')
        print('---------')
        print('food ~ ' + str(food_budget) + '$')
        print('necessities ~ ' + str(necessities_budget) + '$')
        print('transportation ~ ' + str(transportation_budget) + '$')
        print('savings ~ ' + str(savings_budget) + '$')
        print('extra ~ ' + str(extra_budget) + '$')
        print('---------')
    except TypeError:
       print('please input numbers only ')

def custom_calc() :
    custom_categories = {

    }
    total_proportion = 0.0
    remaining = 100
    category_appender = ''
    # for updating the custom category dictionary
    while remaining > 0:
            category_appender = input('\nwhat should the name of the category be?\n\n')
            try:
                category_proportion = float(input('\nwhat proportion of your budget should it receive? enter a whole number percentage\n\n'))
                if total_proportion + category_proportion > 100:
                    print('\nthe total proportion exceeds 100%, please enter a smaller value')
                else:
                    custom_categories.update({category_appender: category_proportion})
                    total_proportion += category_proportion

                remaining = 100 - total_proportion
                print(f"\nremaining proportion = {remaining}%")
            except ValueError:
                print('\nplease enter numbers only\n')


    # calculation of the proportions
    try:
       budget = int(input('\nwhat is your budget?\n\n'))
       print('\n---------')
       for custom_category_name, custom_category_value in custom_categories.items():
               custom_category_name_budget = budget *custom_category_value*0.01
               print(f'{custom_category_name} ~  {custom_category_name_budget} $')
    except ValueError:
       print('please input numbers only')

# Welcome message
print('welcome to eduwallet!\n')

mode = (input('first of all please let me know how you would like to manage your money. \n\nyou can either use the default preset or create a custom one. \n\033[3mdefault/custom\033[0m\n\n')).lower()


if mode == 'default':
    print('you will be choosing the default scheme, which includes \n\n food ~ 30% \n necessities ~ 30% \n transportation ~ 10% \n savings ~ 15% \n extra ~ 15% \n ')
    calculated_budget = default_calc()
elif mode == 'custom':
    print('\nin the custom scheme, you can define the different categories and the proportion of money for them')
    calculated_budget = custom_calc()
else:
    print('please choose from either the default or custom mode')
