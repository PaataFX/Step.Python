while True:
    parrot = input("User Said Whaaat!? ")
    print ("user said whaaat!?", f"User Said {parrot}", sep='\n')
    if parrot.lower() == "quit":
        break
    else:
        continue