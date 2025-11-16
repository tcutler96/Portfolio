# [Finance Data Automation](https://github.com/tcutler96/Finance-Data-Automation)
Developed a collection of integrated Python scripts to automate personal finance management, covering income, expenses, and invoice processing through automated reporting. The system makes use of file and email automation (IMAP), PDF and CSV parsing, Excel manipulation, and data validation in order to streamline repetitive financial tracking tasks, reducing errors, and improving data transparency.

## Process Invoices
Connects securely to an Outlook inbox via IMAP, retrieves emails from predefined senders, extracts attached invoices or reports (PDF/CSV), and saves them in structured folders by financial year and date range.

## Process Income
Reads income transaction CSV files from multiple financial year directories, consolidates them into an Excel workbook, updates totals automatically, and prevents duplicate entries.

## Process Expenses
Records and organises expenses within an Excel workbook, automatically sorting them by date and financial year, calculating totals, and maintaining backup copies of previous files.
