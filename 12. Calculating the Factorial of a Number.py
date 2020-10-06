                                                      # Code made by Frank Lochtenberg
print("Hello user!")                                  # Hello

print("I'm going to calculate n!.")                   # Introduction sentence
n = int(input("Can I get a value of n from you?: "))  # Asks the user for a integer

f = 1                                                 # f stands for factorial  

for i in range(1,n):                                  # i stands for integer
    f = f*(i+1)                                       # Calculates the factorial of the integer the user gave

print("The factorial of your n is: ",f)               # Prints the factorial of the integer the user gave

print("Goodbye user!")                                # Goodbye


    


