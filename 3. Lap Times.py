                                                                                        # Code made by Frank Lochtenberg
print("Hello user!")                                                                    # Hello

lo = int(input("How many laps do you have to run? "))                                   # Asks the user how many laps the user has to run | lo stands for loops  
la = 0                                                                                  # la stands for laps
s = 0                                                                                   # s stands for slowest
tt = 0                                                                                  # tt stands for total time

while la <= lo:                                                                         # Collects the time of each lap the user makes
    if la == 0:                                                                         # Also calculates which time is the:
        la += 1                                                                         # - fastest
    if la == 1:                                                                         # - slowest
        t = float(input(("What is the time for lap ") + str(la) + (" in minutes? ")))   # And calcultes the average time
        tt = t + tt                                                                     
        a = tt/lo                                                                       # a stands for average
        f = t                                                                           # f stands for fastest
        if t < f:
            f = t
        if t > s:
            s = t
        la += 1
    if la > 1:
        t = float(input(("What is the time for lap ") + str(la) + (" in minutes? ")))
        tt = t + tt
        a = tt/lo
        if t < f:
            f = t
        if t > s:
            s = t
        la += 1

print("This was the time of your fastest lap in minutes: ",f)                           # Prints the fastest and slowest lap time
print("This was the time of your slowest lap in minutes: ",s)                           # Also prints the average lap time
print("This was your average lap time in minutes: ",round(a,2))

print("Goodbye user!")                                                                  # Goodbye
