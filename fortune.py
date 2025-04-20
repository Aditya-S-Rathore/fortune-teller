# fortune.py

def main():
    name = "Aditya Singh Rathore"
    admission_number = "20JE0062"

    print(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    print("\n✨ Your fortune:", end=" ")

    if mood == "happy":
        print(f"Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("Better days are coming. Hang in there. ✨")
    elif mood == "neutral":
        print("Sometimes the middle path leads to the best destination. ✨")
    elif mood == "stressed":
        print("Don't worry about the future focus on present, Great things are ahead!✨")
    else:
        print("Hmm... I can't read that mood. Try happy, sad, or neutral. ✨")

if __name__ == "__main__":
    main()
