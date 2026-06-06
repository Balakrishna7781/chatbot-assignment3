Simple Q&A Chatbot
MSCS-633-A01: Advanced Artificial Intelligence
University of the Cumberlands | First Bi-term, Summer 2026
A terminal-based conversational chatbot built with Python, Django, and ChatterBot. The bot trains on ChatterBot's built-in English corpus and responds to free-form natural language input.

Project Structure
chatbot-assignment3/
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
├── .gitignore          # Excludes venv and db files
└── README.md

Requirements

Python 3.10+
pip


Setup & Installation
1. Clone the repository
bashgit clone https://github.com/Balakrishna7781/chatbot-assignment3.git
cd chatbot-assignment3
2. Create and activate a virtual environment
bashpython -m venv chatbot_env
source chatbot_env/bin/activate        # macOS/Linux
chatbot_env\Scripts\activate           # Windows
3. Install dependencies
bashpip install -r requirements.txt
4. Download the spaCy English model (required by ChatterBot)
bashpython -m spacy download en_core_web_sm
5. Run the chatbot
bashpython chatbot.py

Sample Interaction
==================================================
  Welcome to AssistantBot!
  Type 'quit' or 'exit' to end the session.
==================================================

user: Good morning! How are you doing?
bot:  I am doing very well, thank you for asking.
user: You're welcome.
bot:  Do you like hats?
user: What is artificial intelligence?
bot:  Artificial intelligence is the simulation of human intelligence processes by machines.
user: quit
bot:  Goodbye! Have a great day!

How It Works
ComponentRoleChatBotCore dialog engine from ChatterBotChatterBotCorpusTrainerTrains the bot on built-in English conversation dataBestMatch logic adapterScores candidate responses by similarity (threshold: 0.90)SQLite (db.sqlite3)Persists learned conversations between sessions (auto-generated, not committed)

Dependencies
PackagePurposeDjangoWeb framework integration for ChatterBotChatterBotML-based conversational dialog enginechatterbot-corpusEnglish conversation training datasetsSQLAlchemyDatabase ORM for conversation storagespaCy + en_core_web_smNLP tokenization and taggingNLTKNatural language processing utilities

Author
Bala Krishna Konakanchi
University of the Cumberlands
