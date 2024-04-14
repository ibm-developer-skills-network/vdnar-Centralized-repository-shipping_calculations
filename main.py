import sys
from modules.converter import calculate_cbm_shipping_unit_price, calculate_kg_shipping_unit_price

def display_menu():
    print("Welcome to the shipping cost calculator")
    print("1. Calculate shipping cost by CBM")
    print("2. Calculate shipping cost by KG")
    print("0. Exit")


def get_user_choice():
    while True:
        display_menu()
        try:
            user_choice = (input("Enter choice: "))
            if user_choice == "1":
                x = float(input("Enter length: "))
                y = float(input("Enter width: "))
                z = float(input("Enter height: "))
                print('Unit convert m = meter \n dm = decimeter \n cm = centimeter \n mm = millimeter')
                l = input("Enter unit: ")
                u = float(input("Enter unit price (USD): "))
                return calculate_cbm_shipping_unit_price(x, y, z, l, u)
            
            elif user_choice == "2":
                w = float(input("Enter weight: "))
                u = float(input("Enter unit price (USD): "))
                return calculate_kg_shipping_unit_price(w, u)
            elif user_choice == 0:
                print("Goodbye!")
                sys.exit()
                
            else:
                print("Invalid input. Please enter cbm or kg.")
        except ValueError:
            print("Invalid input. Please enter cbm or kg.")
            
def main():
    unit_price = get_user_choice()
    print(f"Shipping cost: {unit_price} USD")
    
if __name__ == "__main__":
    main()