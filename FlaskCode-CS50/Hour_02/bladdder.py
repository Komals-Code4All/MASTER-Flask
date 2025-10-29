

def bladderFull(status):

    if status:
        breakTime = input("Is it time for break? (y/n)")
 
        if breakTime=='y':
            print("go to toilet")
        else:
            print("I'm holding on")
    else:
        print("Carry on!")



bladderFull(True)

bladderFull(False)
