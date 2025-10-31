BACSE101 Problem Solving using Python

PROJECT REPORT 
on
Smart Expense Splitter
Prepared by
Tanya Pamnani 25BAI0168
Apurv Dubey 25BAI0224
Syed Armaan 25BAI0198
Aliza Uzma Syed 25BAI0197
Aditya Varma 25BAI0189

Under the supervision of
Prof. Farooq S M



School of Computer Science and Engineering
Vellore Institute of Technology, Vellore.

October 31, 2025 
Table of Contents
 Abstract
1. Introduction 
2. Problem Statement and Objectives 
3. Implementation Code
4. Demo Screenshots
5. Conclusion


ABSTRACT

The Smart Expense Splitter is a beginner-friendly Python program designed to simplify the process of managing shared expenses among groups. It allows users to add participants, record expenses, automatically calculate who owes whom, and generate a clear settlement summary. The system ensures fairness and transparency by using a simple logic of equal cost sharing and tracking each participant’s balance. Each session is automatically saved in a JSON file for future reference, and the program resets for new expense rounds after each settlement. This project demonstrates the use of core Python concepts like dictionaries, file handling, conditionals, loops, and modular programming — making it both practical and educational for first-year students.



1.	Introduction
Group expense management often becomes confusing, especially during trips, events, or daily shared living. Remembering who paid how much and how to split the total equally is prone to human error.
The Smart Expense Splitter automates this process using Python. Users can easily add names of participants, input the expenses paid by each person, and view real-time balance updates. At the end, the program calculates the minimum number of transactions required to settle all debts.
The project aims to build a console-based interactive system that not only splits expenses fairly but also keeps a digital record of all sessions. It encourages teamwork, problem-solving, and introduces file operations, logic building, and clean coding practices to beginner programmers.

1.1	Domain Information
From a technical standpoint, this domain integrates:
•	Python Programming — for logic implementation, data handling, and automation.
•	File Handling and JSON Data Storage — for persistent record keeping.
•	Algorithmic Balancing Logic — to ensure fair settlement among participants.
•	User Interaction & Data Visualization — to present results in a clear and friendly format.

1.2	Software Libraries Used
Library / Module	Purpose / Functionality	Description
json	Data storage and retrieval	Used to save and load participant balances and session history in JSON files (expenses.json, session_history.json). This enables persistent data saving even after the program closes.
built-in functions (print, input, etc.)	User interface and interaction	These built-in Python features handle menu displays, user input, and text-based output to guide the user through the program.
time	Time stamping sessions	Can be used to add timestamps for session history or logs (not essential but useful for enhancements).

1.3	Contributions by Team Members
•	Coding done by Tanya Pamnani
•	PPT , Creating Repositories and Github management done by Apurv Dubey, Syed Armaan
•	Debugging, Template file, Presentation PPT done by Aditya Varma and Aliza Uzma Syed
1.4	Challenges Faced
1.	Technical Implementation Challenges
2.	Testing Challenges
3.	Team and Collaboration Challenges
2. Problem Statement and Objectives
1.	Problem Statement:
When multiple people share expenses (such as during a trip or event), manual tracking becomes complex and error-prone. People often forget contributions or miscalculate shares, leading to disputes or confusion. There is a need for an automated, transparent, and easy-to-use system to manage shared expenses.

3.	Objectives:
4.	To design a Python program that records and splits expenses fairly among group members.
5.	To calculate balances automatically, showing who owes and who should receive money.
6.	To generate a settlement summary that minimizes transactions.
7.	To store data for each expense session for future reference using JSON files.
8.	To provide a user-friendly interface and allow starting a new round of expense tracking automatically.

3. Implementation
3 Feature
3.1 Overview
The implementation of the Smart Expense Splitter project is done using the Python programming language.
The program is menu-driven and allows users to add participants, record expenses, view balances, settle up payments, and save or reset data.
Each functionality is implemented as a separate function to ensure modularity and code readability.
The following subsections explain each implemented feature in detail along with its corresponding menu option.
3.2 Add Participants (Menu Option 1)
Purpose:
This feature allows the user to add names of participants involved in the expense splitting.
Each participant’s balance is initialized to zero.

Algorithm Steps:
1.	Ask the user to input participant names separated by commas.
2.	Process and store names in the global dictionary balances.
3.	Display confirmation of successfully added participants.
3.3 Add Expense (Menu Option 2)
Purpose:
To record an expense — who paid, how much, and who shared it — and update all balances accordingly.

Algorithm Steps:
1.	Ask the user to specify the payer and the amount paid.
2.	Ask which participants shared the expense (or “all”).
3.	Calculate equal share per person.
4.	Update balances — the payer’s balance increases, others decrease.
3.4 Show Balances (Menu Option 3)
Purpose:
To display the current balance of each participant — who owes money and who should receive money.

Algorithm Steps:
1.	Iterate through all participants in the balance dictionary.
2.	If balance > 0 → user should receive money.
3.	If balance < 0 → user owes money.
4.	If balance = 0 → user is settled.
3.5	Save to History (Session Archiving Feature)
When a session ends (after settlement), the function save_history() is called.
It stores details like:
Names of participants
Their final balances
Date and time of session completion
Data is appended (not overwritten) in a list inside session_history.json.
The file acts as a log of all past group expense activities.

3.6 Show Settlement Summary (Menu Option 4)
Purpose:
To automatically calculate who pays whom so that all balances become zero (settled).
After settlement, the project automatically starts a new session with fresh data.

Algorithm Steps:
1.	Identify debtors (negative balances) and creditors (positive balances).
2.	Match each debtor to a creditor based on owed and owed amounts.
3.	Display all transactions needed for settlement.
4.	Automatically start a new session.
3.7 Start New Session (Menu Option 6)
  	
Purpose:
Allows the user to reset all data manually and start fresh with new participants and expenses.
Automatically deletes old data files.

Algorithm Steps:
1.	Clear the balances dictionary.
2.	Remove expenses.json if it exists.
3.	Prompt the user to add new participants.
3.8 Save and Exit (Menu Option 5)
Purpose:
Saves all balances into a file (session_history.json) before exiting, ensuring data persistence.

Algorithm Steps:
1.	Convert balances into JSON format.
2.	Write them into a local file using the json.dump() method.
3.	Display a confirmation message before program exit.

3.9 Load Data on Startup
Purpose:
When the program starts, it automatically loads previously saved data from the file (if available).
This allows users to continue from where they left off.
4.	Demo Screenshots
Code:
 
 
 
 
 
 
 
 


Run/output screenshots:
 
 
 
 
 
 
5. Conclusion

The Smart Expense Splitter successfully automates the complex task of dividing group expenses. It is easy to use, accurate, and ensures transparency in shared financial management. Through this project, we learned essential programming concepts like file handling, modular coding, data storage using JSON, and designing user-friendly console applications.

This project demonstrates how Python can be applied to solve real-world problems efficiently. Future enhancements could include adding a graphical user interface (GUI), unequal splits, and exporting reports to Excel or PDF formats.
