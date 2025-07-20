import re, random
from colorama import Fore, init

init(autoreset = True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? too many bugs",
    "Why did the computer go to the doctor? Because it had a virus",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches , mountains or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome Enjoy {suggestion}")
        elif answer == "no":
            print(Fore.CYAN + "TravelBot: I will suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry I dont't have that type of desination")

    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days? ")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}")
    print(Fore.GREEN + "- Pack Versatile Clothes")
    print(Fore.GREEN + "- Bring chargers/adapers")
    print(Fore.GREEN + "- Check the weather forecast")

def tell_joke():
    print(Fore.YELLOW + f"Travel: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "I can:-")
    print(Fore.GREEN + "- Suggest Travel Spots (say: 'recommendation')")
    print(Fore.GREEN + "- Offer Packing Tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.")

def chat():
    print(Fore.CYAN + "Hello! I am a TravelBot: ")
    name = input(Fore.YELLOW + "Your Name: ")
    print(Fore.GREEN + f"Nice to Meet you, {name}")
    show_help

    while True:
        user_input = input(Fore.YELLOW + f"{name}")
        user_input = normalize_input(user_input)

        match user_input:

            case "recommend"|"suggest":
                recommend()
            case "pack"|"packing":
                packing_tips()
            case "joke"|"funny":
                tell_joke()
            case "help":
                show_help()
            case "exit"|"bye":
                print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
                break
            case _:
                print(Fore.RED + "Could you rephrase?")
            
chat()