cash_vals = {
    'One Hundred Dollar Bill': 100,
    'Fifty Dollar Bill': 50,
    'Twenty Dollar Bill': 20,
    'Ten Dollar Bill': 10,
    'Five Dollar Bill': 5,
    'Two Dollar Bill': 2,
    'One Dollar Bill': 1,
    'Quarter': 0.25,
    'Dime': 0.10,
    'Nickel': 0.05,
    'Penny': 0.01,
}

def exact_change(item_cost, money_paid):
    change_due = money_paid - item_cost
    print('change due:', change_due)
    total_change = change_due
    print('total change', total_change)
    change_due_format = '{:.2f}'.format(change_due)
    message = f"Your total is {change_due_format}: "
    change = {
        'One Hundred Dollar Bill': 0,
        'Fifty Dollar Bill': 0,
        'Twenty Dollar Bill': 0,
        'Ten Dollar Bill': 0,
        'Five Dollar Bill': 0,
        'Two Dollar Bill': 0,
        'One Dollar Bill': 0,
        'Quarter': 0,
        'Dime': 0,
        'Nickel': 0,
        'Penny': 0,
    }
    
    if change_due < 0:
        message = "You can't afford this item."
        return message

    for currency in cash_vals:
        while cash_vals[currency] <= total_change:
            change[currency] += 1
            total_change -= cash_vals[currency]
            
    print('change:', change)
    print('total change:', total_change)
            
    change_reduce = []
    
    for currency in change:
        if change[currency] > 1:
            if currency == 'Penny':
                currency_plural = 'Pennies'
            else:
                currency_plural = currency + 's'
            change_reduce.append((change[currency], currency_plural))
        elif change[currency] > 0:
            change_reduce.append((change[currency], currency))

    
    if len(change_reduce) == 0:
        message = f"Your total is {change_due_format}."
    elif len(change_reduce) == 1:
        for input in change_reduce:
            message += f"{input[0]} {input[1]}."
    elif len(change_reduce) == 2:
        last_input = change_reduce.pop(-1)
        for input in change_reduce:
            message += f"{input[0]} {input[1]} "
        message += f"and {last_input[0]} {last_input[1]}."
    elif len(change_reduce) > 2:
        last_input = change_reduce.pop(-1)
        for input in change_reduce:
            message += f"{input[0]} {input[1]}, "
        message += f"and {last_input[0]} {last_input[1]}."

    return message

# TEST THREE
print(exact_change(9.99, 20))
# Intended output: "Your total is 10.01: 1 Ten Dollar Bill and 1 Penny."
# Not giving penny because for some reason after subracting 10 from 10.001 it gives barely less than a penny...

# TEST SIX
print(exact_change(17.53, 30))
# Intended output: "Your total is 12.47: 1 Ten Dollar Bill, 1 Two Dollar Bill, 1 Quarter, 2 Dimes, and 2 Pennies." 
# This one is also not giving pennies correctly, this time it looks like it's getting messed up in the initial change_due equation by less than a penny...


# TEST TEN
print(exact_change(0, 999.99))
# Intended output: "Your total is 999.99: 9 One Hundred Dollar Bills, 1 Fifty Dollar Bill, 2 Twenty Dollar Bills, 1 Five Dollar Bill, 2 Two Dollar Bills, 3 Quarters, 2 Dimes, and 4 Pennies."
# This one is correct, I just wanted to show that this only effects tests with pennies, but there are some tests with pennies that do work correctly...