import CoinClass as c # <--- name of the file 'CoinClass'
                      # 'as c' is just an alias

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss() # <-- calling toss method of instance
           my_coin.sideup = 'Heads'
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())


# Call the main function.

main()
