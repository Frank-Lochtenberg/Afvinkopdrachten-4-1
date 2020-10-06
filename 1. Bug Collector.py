                                                                                          # Code made by Frank Lochtenberg
print("Hello user!")                                                                      # Hello

d = 1                                                                                     # d stands for days
b = 0                                                                                     # b stands for bugs

while d <= 5:                                                                             # Asks the user during 5 days
    b = b + int(input(("How many bugs have you collected on day ") + (str(d)) + ("?")))   # how many bugs it collected each day
    d += 1                                                                                

print("Total of bugs collected:",b)                                                       # Prints the total of bugs collected

print("Goodbye user!")                                                                    # Goodbye
                  
