print("\n--Student Weekly Expenses--\n")
categories = [
    "Food & Drinks       [e.g. Lunch, snacks, coffee]",
    "Transportation      [e.g. Bus, jeepney, ride-share]",
    "Mobile / Internet   [e.g. Load, data plan, WiFi top-up]",
    "School Supplies     [e.g. Notebook, pen, bond paper]",
    "Entertainment       [e.g. Games, movies, hangout]"
]

while True:
    name_input = input("Student name: ").strip()
    
    if (not name_input or 
        name_input.isdigit() or 
        any(char.isdigit() for char in name_input)):
        print("Invalid name! Name must contain letters, not just numbers. Please try again.")
    else:
        name = ""
        i = 0
        while i < len(name_input):
            if name_input[i] != " " or len(name) > 0:
                name = name + name_input[i].upper() if i == 0 or name_input[i-1] == " " else name + name_input[i].lower()
            i = i + 1
        
        if len(name) > 0:
            break
        else:
            print("Name cannot be empty. Please try again.")

while True:
    budget_input = input("Weekly budget: ")
    is_valid = True
    has_digit_or_dot_or_minus = False
    for char in budget_input:
        if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' or char == '.' or char == '-':
            has_digit_or_dot_or_minus = True
        else:
            is_valid = False
            break
    if is_valid:
        if has_digit_or_dot_or_minus:
            budget = float(budget_input)
            if budget > 0:
                break
            else:
                print("Budget must be greater than 0. Please try again.")
    print("Please enter a valid number.")

print("\n" + "="*65)
title = "WEEKLY EXPENSE -- CATEGORIES"
print(f"{title:>45}")
print("="*65)

i = 1
while i <= 5:
    print(f" {i}. {categories[i-1]}")
    i = i + 1

print("="*65 + "\n")

expenses = []
total_spent = 0

i = 1
while i <= 4:
    print(f"--- EXPENSE {i} ---")
    
    skip_expense = False
    
    while True:
        cat_input = input("Category (0 to skip): ")
        is_valid_cat = True
        has_digit = False
        for char in cat_input:
            if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
                has_digit = True
            else:
                is_valid_cat = False
                break
        if is_valid_cat:
            if has_digit:
                cat_num = int(cat_input)
                if cat_num == 0:
                    print()
                    skip_expense = True
                    break 
                elif 1 <= cat_num <= 5:
                    skip_expense = False
                    break 
                else:
                    print("Invalid category. Please enter 0-5.")
        print("Please enter a valid number (0-5).")
    
    if skip_expense:
        i = i + 1
    else:
        while True:
            desc_input = input("Description: ")
            desc = ""
            for char in desc_input:
                if char != " " or len(desc) > 0:
                    desc = desc + char
            if len(desc) > 0:
                break
            else:
                print("Description cannot be empty. Please try again.")
        
        while True:
            amount_input = input("Amount: ")
            is_valid_amount = True
            has_digit_or_dot_or_minus = False
            for char in amount_input:
                if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' or char == '.' or char == '-':
                    has_digit_or_dot_or_minus = True
                else:
                    is_valid_amount = False
                    break
            if is_valid_amount:
                if has_digit_or_dot_or_minus:
                    amount = float(amount_input)
                    if amount > 0:
                        break
                    else:
                        print("Amount must be greater than 0. Please try again.")
            print("Please enter a valid number.")
        
        threshold = 0.25 * budget
        high_expense = amount > threshold
        
        expenses.append({
            'num': len(expenses) + 1,
            'cat_num': cat_num,
            'desc': desc,
            'amount': amount,
            'high_expense': high_expense
        })
        total_spent += amount
        
        i = i + 1
        print()

remaining = budget - total_spent
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("="*66)
print(f"{name:>25} -- WEEKLY EXPENSE LOG")
print("="*66)
print(f"  Weekly Budget  : P{budget}0")

i = 0
while i < len(expenses):
    exp = expenses[i]
    cat_name = ""
    j = 0
    while j < len(categories[exp['cat_num'] - 1]):
        if categories[exp['cat_num'] - 1][j] == '[':
            break
        cat_name = cat_name + categories[exp['cat_num'] - 1][j]
        j = j + 1
    
    print(f"\n  [{exp['num']}] {cat_name}")
    print(f"      {exp['desc']:<25} P{exp['amount']:>10}0",end="")
    if exp['high_expense']:
        print(f"  {'High Expense Alert!':<20}", end="")
    print()
    i += 1

print("-"*66)
print(f"{'Total Spent':<31}: P{total_spent:>10}0")
print(f"{'Remaining':<31}: P{remaining:>10}0")
print(f"{'Status':<31}: {status}")
print("="*66)

#MANDOLADO, ZYLK ALLEN P.
#BSIT SOFTWARE ENGINEERING 1A
#MIDTERM EXAMINATION
#04/18/26