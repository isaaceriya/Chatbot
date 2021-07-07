def results(maxResults):
    value = False
    options = ["1: View event","2: Add event", "3: Delete event"]
    choice = int(input(options))
    while value == False:
        if choice in range(0,4):
            if choice == 1:
                maxResults = int(input("Enter value: "))
                while maxResults <= 0:
                    print("please enter a value greater than 0")
                    maxResults = int(input("Enter value that is greater than 0: "))
                maxResults2 = ("maxResults = "+str(maxResults))
                file= open("changes2.py","w")
                file.write(str(maxResults2))
                file.close()
                value = True
        else:
            print("Please keep the input in the range 1-3")
            value = True
            results(6)
results(6)