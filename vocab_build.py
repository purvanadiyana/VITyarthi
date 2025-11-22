import json
import os

# Define the file name for persistent storage
DATA_FILE = "vocabulary.json"

def load_vocabulary():
    """Loads the vocabulary from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_vocabulary(vocab):
    """Saves the current vocabulary to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(vocab, f, indent=4)

def add_word(vocab):
    """Adds a new word and its definition to the tracker."""
    word = input("\nEnter the **word** to add: ").strip().lower()
    if not word:
        print("Word cannot be empty.")
        return

    if word in vocab:
        print(f"'{word}' is already in your vocabulary.")
        return

    definition = input(f"Enter the **definition** for '{word}': ").strip()
    if not definition:
        print("Definition cannot be empty. Word not added.")
        return

    vocab[word] = definition
    save_vocabulary(vocab)
    print(f"✅ Word '{word}' added successfully!")

def view_vocabulary(vocab):
    """Displays all words and their definitions, sorted alphabetically."""
    if not vocab:
        print("\nYour vocabulary list is **empty**.")
        return

    print("\n📚 **Your Vocabulary List** 📚")
    print("-----------------------------------")
    
    # Sort the words alphabetically
    sorted_words = sorted(vocab.keys())
    
    for i, word in enumerate(sorted_words, 1):
        print(f"**{i}. {word.capitalize()}**: {vocab[word]}")

    print("-----------------------------------")

def find_word(vocab):
    """Searches for a specific word."""
    search_term = input("\nEnter the word to **search** for: ").strip().lower()
    if search_term in vocab:
        print(f"\n🔍 **Found**: {search_term.capitalize()}")
        print(f"Definition: {vocab[search_term]}")
    else:
        print(f"\n❌ Word '{search_term}' **not found** in your vocabulary.")

def remove_word(vocab):
    """Removes a word from the tracker."""
    word_to_remove = input("\nEnter the word to **remove**: ").strip().lower()

    if word_to_remove in vocab:
        del vocab[word_to_remove]
        save_vocabulary(vocab)
        print(f"🗑️ Word '{word_to_remove}' **removed** successfully.")
    else:
        print(f"❌ Word '{word_to_remove}' **not found**.")

def main_menu():
    """Displays the main menu and handles user input."""
    vocabulary = load_vocabulary()

    while True:
        print("\n--- **Vocabulary Tracker** ---")
        print("1. Add a new word")
        print("2. View all words")
        print("3. Search for a word")
        print("4. Remove a word")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_word(vocabulary)
        elif choice == '2':
            view_vocabulary(vocabulary)
        elif choice == '3':
            find_word(vocabulary)
        elif choice == '4':
            remove_word(vocabulary)
        elif choice == '5':
            print("\n👋 Saving vocabulary and exiting. Goodbye!")
            save_vocabulary(vocabulary) # Save one last time before exiting
            break
        else:
            print("❗ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()