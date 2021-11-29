# code by Alpha
# @david_dhavyd

import time
def game():
    import random
    questions = [
        "\n What is the name of the toy cowboy in Toy Story? ",  # 0
        "\n How many legs does a spider have? ",  # 1
        "\n What is something you hit with a hammer? ",  # 2
        "\n What is the color of an emerald? ",  # 3
        "\n What’s the name of a place you go to see lots of animals? ",  # 4
        "\n Whose nose grew longer every time he lied? ",  # 5
        "\n What is the name of the fairy in Peter Pan? ",  # 6
        "\n If you freeze water, what do you get? ",  # 7
        "\n What colors are the stars on the American flag? ",  # 8
        "\n In the nursery rhyme, Jack and Jill, what do Jack and Jill go up the hill to fetch? ",  # 9
        "\n Where does the President of the United States live while in office? ",  # 10
        "\n How many planets are in our solar system? ",  # 11
        "\n Which ocean is off the California coast? ",  # 12
        "\n What fruit do kids traditionally give to teachers? ",  # 13
        "\n What’s the response to “see you later, alligator” ? ",  # 14
        "\n Which Disney movie is Elsa in? ",  # 15
        "\n Who is Mickey Mouse’s girlfriend? ",  # 16
        "\n Where does Santa Claus live? ",  # 17
        "\n According to the Dr. Seuss book, who stole Christmas? ",  # 18
        "\n Which state is famous for Hollywood? ",  # 19
        "\n What type of fish is Nemo? ",  # 20
        "\n What do caterpillars turn into? ",  # 21
        "\n What is the color of a school bus? ",  # 22
        "\n What do you use to write on a blackboard? ",  # 23
        "\n On which holiday do you go trick-or-treating? ",  # 24
        "\n How many pairs of wings do bees have? ",  # 25
        "\n Where is the Great Pyramid of Giza? ",  # 26
        "\n What is a doe? ",  # 27
        "\n What do bees make? ",  # 28
        "\n When do leaves die? "  # 29
    ]
    quest = []
    score = 0

    # question conditions
    for y in range(len(questions * 23)):
        rand = random.choice(questions)
        if rand not in quest:
            quest.append(rand)

    for x in range(len(quest)):
        if quest[x] == questions[0]:
            print(quest[x])
            print("A. Woody")
            print("B. Lucas")
            print("C. John")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[1]:
            print(quest[x])
            print("A. Two")
            print("B. Four")
            print("C. Eight")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[2]:
            print(quest[x])
            print("A. Nail")
            print("B. Head")
            print("C. Book")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[3]:
            print(quest[x])
            print("A. Red")
            print("B. Green")
            print("C. Blue")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[4]:
            print(quest[x])
            print("A. Supermarket")
            print("B. Zoo")
            print("C. Cinema")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[5]:
            print(quest[x])
            print("A. Shrek")
            print("B. Snow White")
            print("C. Pinocchio")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[6]:
            print(quest[x])
            print("A. Tinkerbell")
            print("B. Cinderella")
            print("C. Snow White")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[7]:
            print(quest[x])
            print("A. Stone")
            print("B. Block")
            print("C. Ice")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[8]:
            print(quest[x])
            print("A. Red")
            print("B. Blue")
            print("C. White")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[9]:
            print(quest[x])
            print("A. Log of woods")
            print("B. A pail of water")
            print("C. Basket of groceries")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[10]:
            print(quest[x])
            print("A. The White House")
            print("B. Presidential Village")
            print("C. House of America")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[11]:
            print(quest[x])
            print("A. Eight")
            print("B. Nine")
            print("C. Seven")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[12]:
            print(quest[x])
            print("A. The Pacific")
            print("B. The River")
            print("C. The Atlantic")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[13]:
            print(quest[x])
            print("A. An orange")
            print("B. An apple")
            print("C. A mango")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[14]:
            print(quest[x])
            print("A. In a while, crocodile.")
            print("B. In a while, hippopotamus.")
            print("C. In a while, tortoise.")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[15]:
            print(quest[x])
            print("A. Beauty and the Beast")
            print("B. Frozen")
            print("C. Shrek")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[16]:
            print(quest[x])
            print("A. Sarah")
            print("B. SpongeBob")
            print("C. Minnie Mouse")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[17]:
            print(quest[x])
            print("A. The North Pole")
            print("B. The East Pole")
            print("C. The South Pole")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[18]:
            print(quest[x])
            print("A. The Gringos")
            print("B. The Grinch")
            print("C. The Goats")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[19]:
            print(quest[x])
            print("A. California")
            print("B. Paris")
            print("C. London")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[20]:
            print(quest[x])
            print("A. Shark")
            print("B. Tilapia")
            print("C. A clownfish")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[21]:
            print(quest[x])
            print("A. Snail")
            print("B. Maggot")
            print("C. Butterflies")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[22]:
            print(quest[x])
            print("A. Black")
            print("B. Yellow")
            print("C. Violet")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[23]:
            print(quest[x])
            print("A. Chalk")
            print("B. Paint")
            print("C. Crayon")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[24]:
            print(quest[x])
            print("A. Christmas")
            print("B. Halloween")
            print("C. Summer holidays")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[25]:
            print(quest[x])
            print("A. One")
            print("B. Two")
            print("C. Three")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[26]:
            print(quest[x])
            print("A. Egypt")
            print("B. Syria")
            print("C. France")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[27]:
            print(quest[x])
            print("A. A female deer")
            print("B. A male deer")
            print("C. A baby deer")
            ans = str(input(">>> ")).upper()
            if ans == "A":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[28]:
            print(quest[x])
            print("A. Oil")
            print("B. Honey")
            print("C. Noise")
            ans = str(input(">>> ")).upper()
            if ans == "B":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)

        elif quest[x] == questions[29]:
            print(quest[x])
            print("A. In the night")
            print("B. In day time")
            print("C. In the fall")
            ans = str(input(">>> ")).upper()
            if ans == "C":
                print("Correct ✅ ")
                score += 1
            else:
                print("Wrong ❌")
            time.sleep(1)
    # end of the question & calculating results
    time.sleep(3)
    print("\nPlease be patient while we calculate your score...")
    time.sleep(1)
    print("Results loading... %25")
    time.sleep(0.5)
    print("        loading... %50")
    time.sleep(0.5)
    print("        loading... %75")
    time.sleep(1.5)
    print("        loading... %100")
    time.sleep(1)
    print("\n Your performance has been successfully analyzed...")
    wscore = 30 - score
    time.sleep(1)
    print(f"You scored {score} out of {30} Questions")
    print(f"Total correct answer = {score} \nTotal wrong answers = {wscore}")
    if score < 10:
        print(f"{name} your performance is very poor 👎")
        print(f"Thanks for playing my game {name} ❤")
    elif score <= 20:
        print(f"{name} you made a good performance 👍")
        print(f"Thanks for playing my game {name} ❤")
    else:
        print(f"{name} your performance is amazing ✔✔✔🙌")
        print(f"Thanks for playing my game {name} ❤")


print("Hi, I'm Alpha 🐺 ")
time.sleep(1)
name = str(input("What is your name?  \n>>> "))
name = name.capitalize()
time.sleep(1)
print("Hello", name, "\nWelcome to my game...", "Will you like to play?")

# wants to play conditions
wtp = input("Yes or No? >>> ").capitalize()
if wtp == "Yes":
    time.sleep(1)
    print("Okay...")
    time.sleep(1)
elif wtp == "Y":
    time.sleep(1)
    print("Okay...")
    time.sleep(1)
else:
    print(f"Okay {name} Bye! 👋")
    input("\nStrike 'Enter' to exit this game")
    while wtp:
        print("$$$$$")

    # age conditions
age = int(input("How old are you? >>> "))
# time.sleep(1)
if age < 18:
    while age < 18:
        print(f"OH! {age} years old... \nSorry {name} you are too young to play this game 😏 \n{name} you should try again when you are up to {18} or above")
        input("\nStrike 'Enter' to enter another age ")
        age = int(input("How old are you now? >>> "))
        if age >= 18:
            print(f"{name} {age}yrs old. \nOkay  you are old enough to play 👍")
            print("\n     !!!!!Game On!!!!!")


else:
    print(f"{name} {age}yrs old. \nOkay  you are old enough to play 👍")
    print("\n     !!!!!Game On!!!!!")
time.sleep(1)
game()

input("\n\n\n\n\nStrike 'Enter' to exit ")
