import json
def main():
    load_expenses()
    while True:
        user_input = get_user_input()
        if user_input == 7:
            break
        switch_on_user_selected_action(user_input)
        print("\n-----Take another action?-----\n")
    
    
    # print(user_input)

all_expenses = []
def get_user_input():
    
    while True:
        try:
            return int(input("""
                        Select a number for action you want to make
                        1. Add an expense
                        2. View all expenses
                        3. Calculate total spending
                        4. Calculate spending by category
                        5. Delete an expenses
                        6. Save expenses to a file
                        7. close or exit
                        """ ))
            # print(user_input)
            break
        except ValueError:
            print("Enter a valid whole number")
            
    # return user_input
def add_expenses():
    amount = None
    category = None
    description = None
    
    print("To add expenses!")
    while True:
    # or category is None or description is None:
        try:
            if amount is None or amount <= 0:
                amount = float(input("Enter the amount(eg '500')--> $ "))
                if amount <= 0:
                    print("Amount must be positive")
                    continue

        except ValueError:
            print("Enter a number")
            continue
        if category is None or category == "":    
            category = input("Enter the category(eg 'Food')--> ").strip().title()
            if category == "":
                print("category can not be empty")
                category=None
                continue
        if description is None:
            description = input("Enter the description(eg 'Lunch')--> ").strip()
        else:
            expense = {"amount": amount, "category":category, "description":description}
            all_expenses.append(expense)
            print("\nexpense added")
            break
    return expense
       
                
        
        
    
def view_all_expenses():
    if len(all_expenses) == 0:
        print("\nYou have not add any expense yet!!")
    elif len(all_expenses) > 1:
        print("Here are all your expenses")
        for item in all_expenses:
            print(item)
    else:
        print("Here is your expense")
        print(all_expenses)
    
    
def calculate_total_spending():
    total=0
    for item in all_expenses:
        total += item["amount"]
    print(f"Your total expenses is ${total}")
    
def calculate_spending_category():
    total_spend_by_category = {}
    
    
    for item in all_expenses:
        category = item["category"]
        amount_spend = item["amount"]
        if category not in total_spend_by_category:
            total_spend_by_category[category] = 0
        
        total_spend_by_category[category] += amount_spend
    # print(f"""\nCategory        Amount""")
    for category, amount_spend in total_spend_by_category.items():
        print(f"{category} ---{amount_spend}")

    # print(total_spend_by_category)
    
def delete_expenses(): # Return the deleted dic
    if len(all_expenses)==0:
        return "No save expense"
    for idex, expense in enumerate(all_expenses):
        print(idex, expense)
    while True:
        try:
            selected_number= int(input("Select a number to delete the expense(eg 2)--> "))
            if selected_number < 0 or selected_number >= len(all_expenses):
                print("select a valid number")
            else:
                item_to_delete = all_expenses[selected_number]
                del all_expenses[selected_number]
                break
        except ValueError:
            print("select a number")
    print(f"\n{item_to_delete} Deleted")
    return item_to_delete


def save_expenses():
    if len(all_expenses) == 0:
        print("No expenses to save.")
        return
        
    try:
    
        with open("expenses.json", "w") as file:
            json.dump(all_expenses, file, indent=4)
        print("Expenses saved successfully to 'expenses.json'!")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def load_expenses():
    global all_expenses 
    try:
        with open("expenses.json", "r") as file:
            all_expenses = json.load(file)
        print("Previous expenses loaded successfully!")
    except FileNotFoundError:
        print("No saved file found. Starting with an empty list.")
    except json.JSONDecodeError:
        print("The save file is corrupted. Starting with an empty list.")
    except Exception as e:
        print(f"An error occurred while loading: {e}") 
            
            

def switch_on_user_selected_action(selected_action: int):
    match selected_action:
        case 1:
            add_expenses()
        case 2:
            view_all_expenses()
        case 3:
            calculate_total_spending()
        case 4:
            calculate_spending_category()
        case 5:
            delete_expenses()
        case 6:
            save_expenses()
        case _:
            print("Select a number from the options")
            



if __name__ == "__main__":
    main()
