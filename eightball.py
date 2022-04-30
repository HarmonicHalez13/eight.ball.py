import time, random 
randomInt = random.randint (1, 9)
print("Ask the magic 8 ball a question.")
time.sleep(5)
print("Searching for an answer...")
time.sleep(.5)
print("Please be patient")
time.sleep(5)
for dots in range(10):
    print(".")
    time.sleep(.5)
time.sleep(1)

if randomInt == 1:
    print("Answer: It is possible!")
elif randomInt == 2:
    print("Answer: It is decidely so!")
elif randomInt == 3:
    print("Answer: Reply Hazy, try again.")
elif randomInt == 4:
    print("Answer: Ask again later")
elif randomInt == 5:
    print("Answer: Most Definitely")
elif randomInt == 6:
    print("Answer: I think NOT!")
elif randomInt == 7: 
    print("Answer: Yes") 
elif randomInt == 8:
    print("Answer: Cannot be determined")
else:
    print("Answer: Outlook not so good.") 