import random
import string
colors = ["green", "black", "blue", "red", "yellow"]
numbers = [1,2,3,4,5,6,7,8,9,10]
print("\n" * 5)
print("*" * 50)
print("\n" * 5)
print("1. Island")
print("2. Seconds")
print("3. ROCK , PAPER , scissors")
print("4. The worker's wage")
print("5. How old are you")
print("6. Guess the correct number")
print("7. Origin of strong passwords")
print("8. Reverse the sentence")
print("9. Calculator")
print("10. Multiplication tableInvoice")
print("11. Invoice")
program_choice = int(input("Choose one of the programs: "))
if   program_choice == 1:
    choice = random.choice(colors)
    print("""
 ⢰⣿⣷⣦⣄⡀⠀⣀⣀⣀⣀⣀⡀⠀⢀⣠⣴⣶⣿⡆⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀
⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⢸⣿⣿⠟⠁⠀⠈⢹⣿⣿⣿⣿⠏⠁⠀⠙⢻⣿⣿⡇⠀⠀
⠀⠈⢿⣿⣷⣄⣀⣠⣼⣿⣿⣿⣿⣦⣀⣀⣠⣾⣿⡿⠀⠀⠀
⢠⣤⡀⠉⠻⠿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠿⠟⢁⣤⣄⠀
⣼⣿⣿⣦⣄⡀⠘⠿⠻⠿⠟⠿⡿⠻⠿⠀⢀⣀⣤⣾⣿⣧⡀
⠉⠉⠉⠉⠛⠿⣿⣷⣶⣤⣀⣀⣤⣶⣾⣿⠿⠟⠋⠉⠉⠛⠀
⢀⡀⠀⠀⢀⣀⣤⣴⣿⣿⠿⠿⣿⣿⣦⣤⣀⡀⠀⠀⢀⡀⠀
⢿⣿⣷⣾⠿⠟⠛⠋⠁⠀⠀⠀⠀⠈⠙⠛⠻⢿⣷⣶⣿⣿⠆
⠘⢿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡇⠀
    """)
    doors = input("Choose the correct door: door Blue, door Red, door Green, door Black, door Yellow: ")
    if doors == choice:
        print("You entered the next room.")
        choice1 = random.choice(colors)
        rooms = int(input("Choose the right gift: gift Red, gift Green, gift Black, gift Yellow: "))
        if rooms == choice1:
            print("You've got the treasure, you won!")
        else:
            print("Sorry, you lost.")
    else:
        print("Sorry, you lost.")        
elif program_choice == 2:
    seconds = int(input("Enter the number of seconds: "))
    hours = (seconds // 3600) % 60
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print(f"The number of seconds you entered = Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
elif program_choice == 3:

    import random

    rock = """
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)"""

    paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """

    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

    choices = [rock, paper, scissors]
    choices_names = ["Rock", "Paper", "Scissors"]

    # Get the user's choice
    user_choice = int(input("What do you choose?  0 for Rock, 1 for Paper, 2 for Scissors: "))

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please choose 0, 1, or 2.")
    else:
        # Display the user's choice
        print(f"\nYou chose {choices_names[user_choice]}:")
        print(choices[user_choice])

        # Computer's choice
        computer_choice = random.randint(0, 2)
        print(f"\nComputer chose {choices_names[computer_choice]}:")
        print(choices[computer_choice])

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")
elif program_choice == 4:
    print("   WELCOME   ")
    Enter = float(input("Enter the length : "))
    turki = float(input("Enter the width : "))
    Turki = float(input("How much does it cost per meter? "))
    sum = Enter *turki
    sum1 = sum * Turki
    print(f"Total area : {sum}")
    print(f"Total price : {sum1}")
elif program_choice == 5:
    age = int(input("How old are you : "))
    print(f"Your age will be : {2024 - age}")
elif program_choice == 6:
    number = random.choice(numbers)
    Guess = int(input("Guess the number correctly : "))
    if Guess == number:
        print("You guessed the correct number")
    else :

         while Guess != number:
           if Guess < number :
            Guess = int(input("The number is low : "))
           elif Guess > number :
            Guess = int(input("The number is high : "))
         if Guess == number:
             print("You guessed the correct number")
elif program_choice == 7:
    enter =  int(input("Enter the Total Password : "))
    enter1 = int(input("How many characters do you want in your password? "))
    enter2 = int(input("How many numbers do you want in your password? "))
    enter3 = int(input("How many symbols do you want in your password? "))
    if enter != (enter1 + enter2 +enter3 ):
        print("end")
    else :
        letters = string.ascii_letters
        numbers = string.digits
        sympols = string.punctuation
        d1 = (random.choices(letters,k=enter1)+
            (random.choices(numbers,k=enter2))+
            (random.choices(sympols,k=enter3)))
        random.shuffle(d1)
        paper = "".join(d1)
        print("Generated password",paper)
elif program_choice == 8:
    print("    welcome    ")
    # طلب إدخال الجملة من المستخدم
    sentence = input("Please enter a sentence to reverse: ").split()
    # عكس الجملة
    reversed_sentence = sentence[::-1]
    # عرض النتيجة
    print("The reversed sentence is:")
    print(" ".join(reversed_sentence))
elif program_choice == 9:
    # طلب إدخال الرقم الأول من المستخدم
    num1 = float(input("Please enter the first number: "))
    # طلب العملية الحسابية من المستخدم
    operation = input("Please choose an operation (+, -, *, /): ")
    # طلب إدخال الرقم الثاني من المستخدم
    num2 = float(input("Please enter the second number: "))
    # إجراء العملية الحسابية بناءً على اختيار المستخدم
    if operation == "+":
       result = num1 + num2
    elif operation == "-":
       result = num1 - num2
    elif operation == "*":
       result = num1 * num2
    elif operation == "/":
       if num2 != 0:
        result = num1 / num2
       else:
        result = "Error! Division by zero."
    else:
        result = "Invalid operation selected."
    # عرض النتيجة
    print("The result is:", result)
elif program_choice == 10:
    number = int(input("Enter the multiplication table you want to know : "))
    for i in range(1 , 11) :
      number1 = i*number
      print(f"{i} x {number} = {number1}")
elif program_choice == 11:  
   program = []
   app = []
   number = int(input("How many total products did you buy today? "))
   if number < 0:
    print("You didn't buy anything today : ")
   elif number > 0:
    for i in range(0 , number):
       total = input(f"What is the product {i + 1} : ")
       program.append(total)
       total1 = float(input(f"What is the price of the product {i + 1} : "))
       app.append(total1)
    print(f"Product List : {program}")
    nam = input("Do you want to know the prices? yes or no")
    if  nam == "yes":
       sam = sum(app)
       print(f"Total prices : {sam}")
    else :
       print("Thanks")
else :
   print(f"The number you entered {program_choice} is not in our list")