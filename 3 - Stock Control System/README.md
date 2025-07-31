# 🧙‍♂️ CHALLENGE 03 — The Missing Bread

## 🎯 Description:

The Bread Master is worried: the attendants are selling bread without checking the stock!  
Create a system that keeps track of how many units of each type of bread are in stock and prevents sales beyond what's available.

## 📌 Rules:

1. Define an initial stock with the quantity of three types of bread (Ex.: Francês, Integral e Doce).
2. The customer can request a type and a quantity.
3. The system must check if there is enough stock:
   - If yes, deduct from the stock and confirm the sale.
   - If not, inform that there isn’t enough quantity.
4. The system should allow multiple orders until the attendant types "exit".

## 💡 Example execution:

> Initial stock: French=10, Whole Wheat=5, Sweet=8  
 
> What type of bread? French  
> How many would you like? 3  
> Order confirmed! 7 French breads remaining.  

> What type of bread? Whole Wheat  
> How many would you like? 6  
> Not enough Whole Wheat bread in stock!  

> What type of bread? exit  

> Final stock: {'French': 7, 'Whole Wheat': 5, 'Sweet': 8}

## 🧪 Extra challenge (optional):

- Use `.lower()` and `.strip()` to process the bread type.
- Warn the user if the bread type doesn’t exist.
