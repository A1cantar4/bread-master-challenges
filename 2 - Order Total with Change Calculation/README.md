# 🧙‍♂️ CHALLENGE 02 — Credit? Only Tomorrow

## 🎯 Description:
You are still working at the Master of Bread Bakery.

In this challenge, you must handle a common situation: some customers want to buy now and pay later.  
Your task is to build a simple credit system that asks whether the customer paid or wants to leave it on credit, and record that choice.

## 📌 Rules:
1. Ask for the customer's name.
2. Then, ask if they **paid** or will leave it on **credit**.
3. If the answer is **credit**, add the customer's name to a list of debtors.
4. At the end, display all names of customers who left on credit during the shift.
5. Use a loop to handle multiple customers.

## 💡 Example:
> What is the customer's name? Maria
> Did they pay or leave it on credit? credit

> What is the customer's name? Pedro
> Did they pay or leave it on credit? paid

> What is the customer's name? End

> Customers who left on credit: ['Maria']

## 🧪 Tests:
- Handle different customer names and answers (`paid`, `credit`, etc.).

## 🧪 Extra Challenge (optional):
- Normalize user input by converting to lowercase (`.lower()`).
- Do not accept empty names.