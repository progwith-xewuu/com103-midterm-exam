# Description

This program is a simple student weekly expense tracker designed to help manage and monitor personal spending within a set budget.
It begins by asking the student to input their name and weekly budget, ensuring that both entries are valid. The program then displays a list of common expense categories such as food, transportation, mobile/data usage, school supplies, and entertainment. These categories guide the student in organizing their expenses.

The user can record up to four different expenses for the week. For each entry, the student selects a category, provides a short description, and inputs the amount spent. The program validates all inputs to prevent errors, such as empty descriptions or invalid numbers.
A key feature of the program is its ability to flag “high expenses.” If a single expense exceeds 25% of the total weekly budget, it is marked with a warning to alert the student of potentially excessive spending.

After all entries are recorded, the program calculates the total amount spent and compares it to the initial budget. It then displays a detailed summary showing each expense, the total spending, the remaining balance, and an overall status indicating whether the student stayed within budget or overspent. Overall, this program serves as a practical budgeting tool for students, encouraging financial awareness, responsible spending habits, and better money management on a weekly basis.

# How to use

1. Start the Program: Run the code in Python (IDLE, VS Code, or terminal). Once it starts, it will guide you step by step.

2. Enter Your Name: Student name, Type your name and press Enter, You cannot leave this blank or add numbers.

3. Enter Your Weekly Budget: Enter how much money you have for the week (example: 1000), It must be a number greater than 0.

4. Look at the Categories: The program will show 5 categories:
<pre>

- Food & Drinks
- Transportation
- Mobile / Internet
- School Supplies
- Entertainment
</pre>
   You will choose from these when adding expenses.

5. Add Your Expenses (Up to 4): The program will ask you to enter up to 4 expenses or skip it when you type 0.
<pre>
For each expense:

Step 1: Choose Category
Category (0 to skip):
Type a number from 1 to 5
Type 0 if you want to skip this entry

Step 2: Write Description
Description:
Example: Lunch, Bus fare, Load, Notebook
Cannot be empty

Step 3: Enter Amount
Amount:
Enter how much you spent (example: 150)
Must be greater than 0

</pre>

High Expense Warning: If one expense is more than 25% of your budget, the program will warn you "High Expense Alert!". This helps you avoid spending too much on one thing.

6. Check the Final Report
   After entering expenses, the program will show:
   Your name
   Your weekly budget
   All the expenses you entered
   The total amount spent
   The remaining money

<pre>
It will also show your status: 

Budget OK! - You still have money left 
Overspent! - You spent more than your budget
</pre>
