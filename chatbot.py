"""
chatbot.py
----------
MSCS-633-A01 Hands-On Assignment 3: Simple Q&A Chatbot
Author : Bala Krishna Konakanchi
Purpose: Terminal-based chatbot using ChatterBot's corpus trainer.
         Trains on built-in English conversation data and accepts
         free-form user input until the user types 'quit' or 'exit'.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def create_bot() -> ChatBot:
    """
    Instantiate and return a trained ChatBot.

    The bot uses SQLite storage (default) so it remembers
    prior conversations between runs.  Set read_only=True
    after initial training to freeze the model.

    Returns:
        ChatBot: A trained ChatterBot instance ready to respond.
    """
    bot = ChatBot(
        "AssistantBot",
        # Disable read-only so the bot can learn during the session
        read_only=False,
        # Default SQLite storage adapter
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
            # Best-match adapter scores candidate responses by similarity
            {
                "import_path": "chatterbot.logic.BestMatch",
                # Confidence threshold: below this the fallback reply is used
                "default_response": "I'm sorry, I don't quite understand. "
                                    "Could you rephrase that?",
                "maximum_similarity_threshold": 0.90,
            }
        ],
    )
    return bot


def train_bot(bot: ChatBot) -> None:
    """
    Train the bot on ChatterBot's bundled English corpus.

    The corpus covers general conversation, greetings, and trivia.
    Training only needs to happen once; subsequent runs load the
    persisted SQLite database automatically.

    Args:
        bot (ChatBot): The bot instance to train.
    """
    trainer = ChatterBotCorpusTrainer(bot)
    print("[INFO] Training on English corpus (this may take a moment)...")
    trainer.train("chatterbot.corpus.english")
    print("[INFO] Training complete.\n")


def chat_loop(bot: ChatBot) -> None:
    """
    Run the interactive terminal chat loop.

    Reads user input from stdin, passes it to the bot,
    prints the bot's response, and repeats until the user
    types 'quit' or 'exit' (case-insensitive).

    Args:
        bot (ChatBot): A trained ChatBot ready to generate responses.
    """
    print("=" * 50)
    print("  Welcome to AssistantBot!")
    print("  Type 'quit' or 'exit' to end the session.")
    print("=" * 50)

    while True:
        try:
            # Read user input; strip whitespace
            user_input: str = input("\nuser: ").strip()

            # Allow graceful exit
            if user_input.lower() in ("quit", "exit", "bye"):
                print("bot: Goodbye! Have a great day!")
                break

            # Skip empty lines
            if not user_input:
                continue

            # Generate and print the bot's response
            response = bot.get_response(user_input)
            print(f"bot: {response}")

        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or piped-input termination cleanly
            print("\nbot: Session interrupted. Goodbye!")
            break


def main() -> None:
    """Entry point: create, train, and run the chatbot."""
    bot = create_bot()
    train_bot(bot)
    chat_loop(bot)


if __name__ == "__main__":
    main()