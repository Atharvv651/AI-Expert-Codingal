print("Hello! I am an AI Bot.")

name=input()

print(f"Nice to meet you {name}")
print("How are you feeling today? (bad/good)")
mood=input().lower()

if mood == "good":
    print("I am glad to hear that")
elif mood == "bad":
    print("I am sorry to hear that. Hope things get better soon!")
else:
    print("I see something it is hard to put feelings into words")

print(f"It was nice chatting with you {name}. Goodbye!")