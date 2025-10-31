# 💸 Smart Expense Splitter 2.0 🧾
# by Team of 5 - Beginner Friendly Python Project
# -----------------------------------------------
# Features:
# 1️⃣ Add participants
# 2️⃣ Add expenses (who paid, amount, split among)
# 3️⃣ Show balances (who owes whom)
# 4️⃣ Settlement summary
# 5️⃣ Auto save session history
# 6️⃣ Fresh new round after settlement
# -----------------------------------------------

import json
from datetime import datetime

# Store all participant balances
balances = {}

# FUNCTION 1: Add Participants
def add_participants():
    print("\n--- Add Participants ---")
    names = input("Enter names separated by commas: ").split(",")
    for name in names:
        name = name.strip().title()
        if name and name not in balances:
            balances[name] = 0.0
    print(f"✅ Added participants: {', '.join(balances.keys())}")


# FUNCTION 2: Add an Expense
def add_expense():
    if not balances:
        print("❌ No participants added yet!")
        return

    print("\n--- Add Expense ---")
    payer = input("Who paid? ").title()
    if payer not in balances:
        print("❌ Payer not found!")
        return

    try:
        amount = float(input("Enter amount paid: ₹"))
    except ValueError:
        print("❌ Invalid amount!")
        return

    # Choose who the expense is shared among
    involved = input("Who shared this expense? (comma separated names or 'all'): ").strip().lower()
    if involved == "all":
        share_list = list(balances.keys())
    else:
        share_list = [name.strip().title() for name in involved.split(",") if name.strip()]

    if not share_list:
        print("❌ No participants selected!")
        return

    share = round(amount / len(share_list), 2)
    print(f"Each owes ₹{share}")

    # Adjust balances
    for person in share_list:
        if person not in balances:
            print(f"⚠️ Skipping unknown person: {person}")
            continue
        balances[person] -= share
    balances[payer] += amount

    print("✅ Expense added successfully!")


# FUNCTION 3: Show Balances
def show_balances():
    print("\n--- Current Balances ---")
    for name, bal in balances.items():
        if bal > 0:
            print(f"{name} should receive ₹{bal:.2f}")
        elif bal < 0:
            print(f"{name} owes ₹{abs(bal):.2f}")
        else:
            print(f"{name} is settled up.")
    print("--------------------------")


# FUNCTION 4: Save session history
def save_to_history(summary_lines):
    """Save the completed round (balances + settlement summary) to session_history.json"""
    history_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "balances": balances.copy(),
        "settlement_summary": summary_lines
    }

    history_file = "session_history.json"

    # Load existing history if available
    try:
        with open(history_file, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    # Append new round
    history.append(history_entry)

    # Save back
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    print("🧾 Session saved to history file 'session_history.json'.")


# FUNCTION 5: Start New Session (fresh)
def start_new_session(auto=False):
    global balances
    balances.clear()
    if auto:
        print("\n🆕 Starting a new session automatically...\n")
    else:
        print("\n🔄 All previous data cleared. Starting fresh...\n")


# FUNCTION 6: Settlement Summary + Save + Restart
def settle_up():
    print("\n--- Settlement Summary ---")
    debtors = {n: -b for n, b in balances.items() if b < 0}
    creditors = {n: b for n, b in balances.items() if b > 0}

    if not debtors and not creditors:
        print("✅ Everyone is already settled up.")
        return

    summary_lines = []

    while debtors and creditors:
        debtor, debt_amt = debtors.popitem()
        creditor, credit_amt = creditors.popitem()

        payment = min(debt_amt, credit_amt)
        line = f"{debtor} pays ₹{payment:.2f} to {creditor}"
        print(line)
        summary_lines.append(line)

        # Adjust remaining
        if debt_amt > payment:
            debtors[debtor] = debt_amt - payment
        if credit_amt > payment:
            creditors[creditor] = credit_amt - payment

    print("\n✅ Settlement complete! Everyone is even now.")

    # ✅ Save this round before clearing
    save_to_history(summary_lines)

    # Start a new fresh session automatically
    start_new_session(auto=True)


# FUNCTION 7: Load and Show Past Sessions
def show_history():
    print("\n📜 --- Past Session History ---")
    try:
        with open("session_history.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        print("❌ No session history found yet.")
        return

    if not history:
        print("ℹ️ History file is empty.")
        return

    for i, session in enumerate(history, start=1):
        print(f"\n📅 Session {i} - {session['timestamp']}")
        print("Balances:")
        for name, bal in session["balances"].items():
            print(f"  {name}: ₹{bal:.2f}")
        print("Settlement Summary:")
        for line in session["settlement_summary"]:
            print(f"  ➤ {line}")
        print("-" * 30)


# FUNCTION 8: Save/Load Current Data
def save_data():
    with open("expenses.json", "w") as f:
        json.dump(balances, f)
    print("💾 Data saved to 'expenses.json'")


def load_data():
    global balances
    try:
        with open("expenses.json", "r") as f:
            balances = json.load(f)
        print("📂 Data loaded successfully!")
    except FileNotFoundError:
        print("❌ No previous data found.")


# MAIN FUNCTION
def main():
    print("💸 Welcome to Smart Expense Splitter 💸")
    load_data()
    while True:
        print("""
============================
1. Add Participants
2. Add Expense
3. Show Balances
4. Show Settlement Summary
5. Show Past Sessions
6. Start New Session
7. Save & Exit
============================
""")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_participants()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_balances()
        elif choice == "4":
            settle_up()
        elif choice == "5":
            show_history()
        elif choice == "6":
            start_new_session()
        elif choice == "7":
            save_data()
            print("👋 Goodbye! Data saved.")
            break
        else:
            print("❌ Invalid choice, try again!")


if __name__ == "__main__":
    main()
