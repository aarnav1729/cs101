#Make your own cake game
import random

def make_cake():

    flavor = ["Chocolate", "Vanilla", "Red Velvet", "Carrot", "Lemon", "Strawberry", "Coconut", "Marble", "Black Forest", "Coffee"]
    frosting = ["Cream Cheese", "Butter Cream", "Fondant", "Chocolate Ganache", "Whipped Cream"]
    size = ["Tiny", "Small", "Medium", "Large", "Extra Large"]

    understanding = 0
    while understanding == 0:
        understanding = int(input("All of your inputs should be an integer, do you understand? \n(type 1 if yes, type 0 if no):"))
        if understanding != 0 and understanding != 1:
            print("You clearly don't understand")
            understanding = 0

    print("\nThere are 10 flavors of cake, Chose one of them:")
    for i in range (len(flavor)):
        print(f"{1+i}:", flavor[i])
    userFlavor = int(input("Type your choice in here:"))
    if userFlavor > 10 or userFlavor < 1:
        print("THAT IS NOT AN OPTION!!!!! YOUR FLAVOR HAS NOW RANDOMLY BEEN CHOSEN")
        userFlavor = random.randint(1, 10)

    print("\nThere are 5 flavors of frosting, Chose one of them:")
    for i in range (len(frosting)):
        print(f"{1+i}:", frosting[i])
    userFrosting = int(input("Type your choice in here:"))
    if userFrosting > 5 or userFrosting < 1:
        print("THAT IS NOT AN OPTION!!!!! YOUR FROSTING HAS NOW RANDOMLY BEEN CHOSEN")
        userFrosting = random.randint(1, 5)

    print("\nThere are 5 sizes of cake, Chose one of them:")
    for i in range (len(size)):
        print(f"{1+i}:", size[i])
    userSize = int(input("Type your choice in here:"))
    if userSize > 5 or userSize < 1:
        print("THAT IS NOT AN OPTION!!!!! YOUR SIZE HAS NOW RANDOMLY BEEN CHOSEN")
        userSize = random.randint(1, 5)

    userLayers = int(input("\nYou can have from 1 layer to 5 layers on your cake, type how many you want:"))
    if userLayers > 5:
        print("TOO MANY LAYERS!!!!!!! YOUR LAYERS HAVE NOW RANDOMLY BEEN CHOSEN")
        userLayers = random.randint(1, 5)
    elif userLayers < 1:
        print("NOT ENOUGH LAYERS!!!!!! YOUR LAYERS HAVE NOW RANDOMLY BEEN CHOSEN")
        userLayers = random.randint(1, 5)
        
    if 1 <= userFlavor <= 3 or userFrosting == 3 or userSize >= 4 or userLayers == 5:
        if userSize == 5 and userLayers > 1:
            print("\nYou made an", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layers tall")
        elif userSize == 5:
            print("\nYou made an", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layer tall")
        elif userLayers > 1:
            print("\nYou made a", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layers tall")
        else:
            print("\nYou made a", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layer tall")
        print("That sounds like a delicious cake! You win!")
    else:
        if userSize == 5 and userLayers > 1:
            print("\nYou made an", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layers tall")
        elif userSize == 5:
            print("\nYou made an", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layer tall")
        elif userLayers > 1:
            print("\nYou made a", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layers tall")
        else:
            print("\nYou made a", size[userSize - 1], flavor[userFlavor - 1], "cake with", frosting[userFrosting - 1], "frosting, and it is", userLayers, "layer tall")
        print("That sounds like a gross cake! You lose!")