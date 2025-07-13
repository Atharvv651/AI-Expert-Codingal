import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to sentiment spy! {Fore.RESET}")
user_name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()

if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"{Fore.CYAN} Hello Agent {user_name}")
print(f"Type a sentence and i will analyze your sentence with textblob and show you the sentiment")
print(f"{Fore.YELLOW} reset {Fore.CYAN} {Fore.YELLOW} history {Fore.CYAN} {Fore.YELLOW} exit")
print(f"{Fore.CYAN} to quit. {Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()
    
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command. {Style.RESET_ALL}")
        continue

    if user_input.lower() == 'exit':
        print(f"\n{Fore.BLUE} Exiting Sentiment spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input.lower() == 'reset':
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation history cleared! {Style.RESET_ALL}")
        continue

    elif user_input.lower() == 'history':
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet. {Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Conversation History yet. {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😭"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                
                print(f"{idx}. {color}{emoji}{text}"
                      f"(polarity: {polarity:.2f}, {sentiment_type})"
                      )
        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😭"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected!")
    print(f"(Polarity: {polarity:.2f}) {Style.RESET_ALL}")
