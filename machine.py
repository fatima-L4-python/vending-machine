inventory={ 'F001': {'name':'Granola Bar',
        'price':5,
        'quantity':3},
        'F002': {'name':'Pretzels',
        'price':4,
        'quantity':6},
        'F003': {'name':'Water Bottle',
        'price':2,
        'quantity':6},
        'F004': {'name':'Clif Bar',
        'price':3,
        'quantity':4},
        'F005': {'name':'Starburst',
        'price':4,
        'quantity':6}, 
        'A006': {'name':'Mars',
        'price':2,
        'quantity':7},
        'A010': {'name':'Hazelnut Chocolate',
        'price':5,
        'quantity':9},
        'A011': {'name':'Coffee',
        'price':2,
        'quantity':6},
        'A012': {'name':'Energy Drink',
        'price':3,
        'quantity':6},
        'A013': {'name':'Lays',
        'price':4,
        'quantity':8},
  }

suggestions={
    'Granola Bar':'Pretzels',
    'Water Bottle':'Clif Bar',
    'Starburst':'Mars',
 }

def display_item():
  print("Welcome to the vending machine. The available inventory are:")
  for code, item in inventory.items():
    print(f"Code:{code}\tItem:{item['name']}\tPrice:AED{item['price']}\tQuantity:{item['quantity']}")

def vending_machine():
    code=input('ENTER CODE FOR THE ITEM:')
    if code in inventory:
     item=inventory[code]['name']
     price=inventory[code]['price']
     quantity=inventory[code]['quantity']
     print(f"Selected item:{item}\nPrice: AED {price}\nQuantity:{quantity}")

     amount=float(input("Please insert coins: AED"))
    if amount < price:
      print('Insufficient Amount')
    else:
      change=amount - price
      print(f"Dispensing {item}...\nPlease collect your change of AED {change:.2f}")
      inventory[code]['quantity']-=1
      print(f"inventory left for {item}:{inventory[code]['quantity']}")
      
      if item in suggestions:
        suggestion=suggestions[item]
        print(f"If you bought {item}, you might also like {suggestion}.")
      else:
        print("Thank you for buying")
       
display_item()
vending_machine()
       

