import random

secret = random.randint(1,100)
chances = 3

for attempt in range(1,chances+1):
    guess=int(input(f"\nAttempt {attempt}/{chances} - Enter a number between 1-100: "))
    if guess == secret:
        print("🎉 Woww! You Guessed correct!")
        break
    else:
        print("❌ You Guessed Wrong!")
    
        if attempt < chances:
             if guess > secret:
                 print("💡 CLUE: Try a Smaller Number.")
             else:
                 print("💡 CLUE: Try a Larger Number.")
                
else:
    print("\n😐 All chances ended!")
    print(f"\n🔍The Number was: {secret}")
