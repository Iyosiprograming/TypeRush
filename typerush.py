import time
import random

def get_random_text():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Typing fast takes practice and focus.",
        "Python is a great programming language.",
        "AI is changing the future of everything.",
        "Code every day to become a better developer.",
        "Debugging is like being a detective in a crime movie.",
        "Functions make code reusable and clean.",
        "The keyboard is mightier than the sword.",
        "Errors help you learn faster.",
        "Speed comes from accuracy and consistency."
    ]
    return random.choice(sentences).split()

def calculate_wpm(start_time, end_time, word_count):
    elapsed_time = end_time - start_time
    if elapsed_time == 0:
        return 0
    wpm = (word_count / elapsed_time) * 60
    return round(wpm, 2)

def start_game():
    text = get_random_text()
    
    print("📜 Type this:\n", " ".join(text))
    
    start_time = time.time() 
    user_input = input("⌨️ Start typing: ").split()
    end_time = time.time()    
    
    correct_words = 0
    for i in range(len(text)):
        if i < len(user_input) and user_input[i] == text[i]:
            correct_words += 1
        else:
            print(f"❌ Wrong word: expected '{text[i]}', but got '{user_input[i] if i < len(user_input) else 'nothing'}'")
    
    print(f"✅ You typed {correct_words} out of {len(text)} words correctly.")
    print(f"⏱️ Time taken: {round(end_time - start_time, 2)} seconds.")
    wpm = calculate_wpm(start_time, end_time, correct_words)
    print(f"⚡ Your WPM: {wpm} ", end="")

    if wpm < 20:
        print("🐢 Very slow")
    elif wpm < 40:
        print("🐌 Slow")
    elif wpm < 60:
        print("🚶 Average")
    elif wpm < 80:
        print("🏃 Good")
    elif wpm < 100:
        print("🚴 Fast")
    else:
        print("🚀 Pro-Level")

while True:
    print("\n🎮 ************ Typerush ************")
    print("1️⃣  Start Game")
    print("2️⃣  Exit")
    try:
        choice = input("👉 Enter your choice (1 or 2): ")
        if choice == '1':
            print("🎯 Starting the game...")
            start_game()
        elif choice == '2':
            print("👋 Exiting the game. Goodbye!")
            break
    except ValueError:
        print("⚠️ Invalid choice. Please enter 1 or 2.")

""" developerd by Iyosi """