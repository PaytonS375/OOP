import J_Customer
import J_Car
import J_ServiceQuote

def main():

    n = input('Enter your name: ')
    a = input('Enter your address: ')
    p = input('Enter your phone number: ')

    customer_info = J_Customer.Customer(n, a, p)

    mk = input('Enter the make of your car: ')
    m = input('Enter the model of your car: ')
    y = input('Enter the year of your car: ')

    car_info = J_Car.Car(mk, m, y)

    charges = J_ServiceQuote.ServiceQuote(600, 300, 180)
    
    print("Joe's Automotive Shop")
    print('Here is your Service Quote:')
    print()
    print('Customer Info')
    print('Name: ', customer_info.get_name())
    print('Address: ', customer_info.get_address())
    print('Phone Number: ', customer_info.get_phone())
    print()
    print('Car Info')
    print('Make: ', car_info.get_make())
    print('Model: ', car_info.get_model())
    print('Year: ', car_info.get_year())
    print()
    print('Parts and Labor Charges: $', format(charges.get_parts_charges() + charges.get_labor_charges(), ',.2f'), sep='')
    print('Sales Tax: $', format(charges.get_sales_tax(), ',.2f'), sep='')
    x = charges.get_parts_charges() + charges.get_labor_charges() + charges.get_sales_tax()
    print('Total Charges: $', format(x, ',.2f'), sep='')
    print()

main()