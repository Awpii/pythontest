import random
import threading

def nashe(maxnumber):
    #for i in range(2,maxnumber):
        c0 = 3.5
        steps = 0

        while c0 != 1:
            if (c0 % 2) == 0:
                    c0 = c0 // 2
                    #print(c0)
                    steps += 1
            elif (c0 % 2) == 1:
                c0 = 3 * c0 + 1
                #print(c0)
                steps += 1
        if steps == 0:
            print("You deserve a nobel prize, you've disproven Lothar Collatz anasheeeeeee")
            print(f"There are: {steps} steps")
        #print(f"There are: {steps} steps")

nashe(3.5)

#Testing comment for github commit