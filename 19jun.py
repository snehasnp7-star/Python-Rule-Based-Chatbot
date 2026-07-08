responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I am fine, thank you.",
    "what is your name": "My name is ChatBot.",
    "who created you": "I was created using Python.",
    "what is python": "Python is a popular programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine learning enables computers to learn from data.",
    "what is cse": "CSE stands for Computer Science and Engineering.",
    "what is your favorite language": "Python is my favorite language.",
    "tell me a joke": "Why do programmers hate nature? It has too many bugs!",
    "what is your purpose": "I am here to answer your questions.",
    "thank you": "You are welcome!",
    "good morning": "Good morning! Have a great day.",
    "bye": "Goodbye! See you later."
}
print("Welcome to our chatbot")
for i in  responses:
    chat = input("Chat with the bot: ").lower()
    if chat in responses:
        print(responses[chat])
    else:
        print("invalid")