a = 0
testdict = {"apple":2,"sword":1,"berry":5,"dart":3, "book": 2}

#check how many items are being carried
for x in testdict:
    a += testdict[x]
    if a < 11:
        print(a)
    else:
        print("Too much stuff")
        break  #get out of all the loopiness
        
