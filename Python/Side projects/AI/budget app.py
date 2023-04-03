import tkinter as tk

# Global variables
budgets = []

# Create a new budget
def create_budget():
    budget_name = name_entry.get()
    budget_limit = float(limit_entry.get())
    budget = {"name": budget_name, "limit": budget_limit, "expenses": []}
    budgets.append(budget)
    budgets_listbox.insert(tk.END, budget_name)
    name_entry.delete(0, tk.END)
    limit_entry.delete(0, tk.END)

def view_budget():
    global current_budget_index
    try:
        budget_index = budgets_listbox.curselection()[0]
        current_budget_index = budget_index
        selected_budget = budgets[budget_index]
        current_budget_name.set(selected_budget.name)
        current_budget_limit.set(selected_budget.limit)
        expenses_listbox.delete(0, END)
        for expense in selected_budget.expenses:
            expenses_listbox.insert(END, f"{expense.name} ({expense.category}): ${expense.amount}")
        status_label.config(text=f"Total spent: ${selected_budget.total_spent()}, Remaining: ${selected_budget.remaining_budget()}")
    except IndexError:
        pass


# Add a new expense to the currently selected budget
def add_expense():
    if len(budgets) == 0:
        status_label.config(text="Error: No budget selected")
        return
    budget_index = budgets_listbox.curselection()[0]
    expense_name = expense_name_entry.get()
    expense_category = expense_category_entry.get()
    expense_amount = float(expense_amount_entry.get())
    if expense_amount > budgets[budget_index]["limit"]:
        status_label.config(text="Warning: Expense exceeds budget limit")
    budget = budgets[budget_index]
    budget["expenses"].append({"name": expense_name, "category": expense_category, "amount": expense_amount})
    update_expenses_listbox()

# Update the expenses listbox to display the expenses for the currently selected budget
def update_expenses_listbox():
    expenses_listbox.delete(0, tk.END)
    if len(budgets) == 0:
        return
    budget_index = budgets_listbox.curselection()[0]
    budget = budgets[budget_index]
    for expense in budget["expenses"]:
        expenses_listbox.insert(tk.END, f"{expense['name']} ({expense['category']}): {expense['amount']}")

# Update the status label to display the remaining budget amount for the currently selected budget
def update_status_label():
    if len(budgets) == 0:
        return
    budget_index = budgets_listbox.curselection()[0]
    budget = budgets[budget_index]
    total_expenses = sum([expense['amount'] for expense in budget['expenses']])
    remaining_budget = budget['limit'] - total_expenses
    status_label.config(text=f"Remaining budget: {remaining_budget:.2f}")

# Initialize the tkinter window
root = tk.Tk()
root.title("Budget Tracker")

# Create the GUI elements
budget_name_label = tk.Label(root, text="Budget name:")
name_entry = tk.Entry(root)
limit_label = tk.Label(root, text="Budget limit:")
limit_entry = tk.Entry(root)
create_budget_button = tk.Button(root, text="Create budget", command=create_budget)

budgets_listbox_label = tk.Label(root, text="Budgets:")
budgets_listbox = tk.Listbox(root)
budgets_listbox.bind("<<ListboxSelect>>", lambda event: update_expenses_listbox() or update_status_label())

expense_name_label = tk.Label(root, text="Expense name:")
expense_name_entry = tk.Entry(root)
expense_category_label = tk.Label(root, text="Expense category:")
expense_category_entry = tk.Entry(root)
expense_amount_label = tk.Label(root, text="Expense amount:")
expense_amount_entry = tk.Entry(root)
add_expense_button = tk.Button(root, text="Add expense", command=add_expense)

expenses_listbox_label = tk.Label(root, text="Expenses:")
expenses_listbox = tk.Listbox(root)

status_label = tk.Label(root, text="")

# Define the layout of the user interface elements using grid layout
budget_name_label.grid(row=0, column=0, sticky="w")
name_entry.grid(row=0, column=1)
limit_label.grid(row=1, column=0, sticky="w")
limit_entry.grid(row=1, column=1)
create_budget_button.grid(row=2, column=0)

budgets_listbox_label.grid(row=3, column=0, sticky="w")
budgets_listbox.grid(row=4, column=0)

expense_name_label.grid(row=3, column=1, sticky="w")
expense_name_entry.grid(row=4, column=1)
expense_category_label.grid(row=5, column=1, sticky="w")
expense_category_entry.grid(row=6, column=1)
expense_amount_label.grid(row=7, column=1, sticky="w")
expense_amount_entry.grid(row=8, column=1)
add_expense_button.grid(row=9, column=1)

expenses_listbox_label.grid(row=10, column=0, sticky="w")
expenses_listbox.grid(row=11, column=0)

status_label.grid(row=12, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

