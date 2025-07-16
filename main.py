import random

def play_game():
    number_to_guess = random.randint(1,100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("now guess the number between 1 to 100")
    
    while True:
        try:
           guess = int(input("enter the number between 1 to 100 : "))
           attempts += 1
           
           if guess < number_to_guess:
               print("Too low! try again")
           elif guess>number_to_guess:
                   print("Too high! try again")
           else:
                print(f"congratulation! you guessed it in {attempts} attempts. ")
                break
        except ValueError:
             print("please enter the right number.")

                    
def main():
    while True:
         play_game()
         play_again = input("do you want to play again? (y/n): ").lower()
         if play_again != 'y':
              print(" thanks for playing! goodbye")
              break
if __name__ =="__main__":
    main()