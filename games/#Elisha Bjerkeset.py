#Elisha Bjerkeset
import random
for i in range(2):
    deck = random.randint(1, 10)
dealer = random.randint(1, 10) + random.randint(1, 10)
while dealer < 11:
    dealer += random.randint(1, 10)
print(dealer)

print("You will now play simplified BlackJack. Try to get as close to 21 as possible, but don't go overboard. There are no suits. Aces are only ever worth one")
print("The dealer will never bust")

user = random.randint(1, 10) + random.randint(1, 10)
print("Your hand is:", user)
answer = (input("Do you want to Hit or Pass. Enter H for Hit or P for Pass:"))

while answer == "H" and user < 22:
    user += random.randint(1, 10)
    print("Your hand is:", user)
    
    if user > 21:
        print("You bust. You lose")
    else:
        answer = input("Do you want to Hit or Pass. Enter True for Hit or False for Pass:")

if user > dealer and user <= 21:
    print("You win. The dealer's hand was", + dealer)
elif dealer > user:
    print("The dealer wins. The dealer's hand was", + dealer)
elif user == dealer:
    print("You tied with the dealer")