import math
def hello_World():
    print("Hello World!")

hello_World()

msg = "Hello World!"
print(msg)

def printName(name):
    print(name)

printName("Lukas")

def greeting(name):
    print('Hello, ' + name + '!')

greeting("Joseph")

def add(num1,num2):
    print(num1 + num2)

add(20,46)

def nameCheck(name):
    if name == "Steven":
        print("What's up, Steven?")
    elif name == "Bryan":
        print("Hey, Bryan!")
    else: print("Cool name, {}".format(name))

nameCheck("Magdaline")

def faveColorFinder(color):
    if color == "Red":
        print("Red is a great color!")
    elif color == "Green":
        print("Green is a solid favorite color.")
    elif color == "Black":
        print("So trendy!")
    else: print("You need to evaluate your choices in colors")

colorRating = faveColorFinder("Red")

def printAllNames(arr):
    for x in arr:
        print(x)
printAllNames(["Jenny","Margaret","Lucy","John"])

def thatsOdd(num):
    if num % 2 == 0:
        print("That's not odd!")
    else: print("That's odd, indeed!")

thatsOdd(20)

def bigOrSmall(nums):
    answers = []
    for x in nums:
        if x > 100:
            answers.append("big")
        elif x <= 100:
            answers.append("small")
    print(answers)
bigOrSmall([50,2000,512,3,5643,4,10])

def theElminator(contestants,loser):
    contestants.remove(loser)
    print(contestants)
theElminator(["Katniss", "Peeta", "Fox-face", "Glimmer", "Cato", "Rue", "Thresh", "Clove", "Marvel"],"Glimmer")

def scream(str):
    screamStr = str.upper() + "!!!"
    print(screamStr)
scream("my head hurts")

def whisper(str):
    whisperStr = str.lower() + "..."
    print(whisperStr)
whisper("Be quiet")

def emailCheck(email):
    if '@' in email:
        print("Email successfully verified")
    else: print("Not a valid email address.")
emailCheck("lukasthis.com")

def frogMerchant(coins):
    if coins > 3:
        maxAmt = math.floor(coins / 3)
        print("You can buy {} chocolate frogs!".format(maxAmt))
    else: print("You don't have enough coin!")
frogMerchant(20)

sampleArray = [0,1,2,30,4,5,6,8,9]
def ascendingArr(arr):     
    ascending = [arr[index] <= arr[index + 1] for index in range(len(arr) -1)]
    if False in ascending:
        print(False)
    else: print(True)
ascendingArr(sampleArray)
    