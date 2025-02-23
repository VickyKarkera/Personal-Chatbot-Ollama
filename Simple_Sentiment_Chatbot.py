from textblob import TextBlob

# pre-defined responses
intents = {
    "hours":{
        "keywords": ["hour", "open","close"],
        "response": "We are open from 9 AM to 5 PM, from Monday to Friday."
    },
    "return": {
        "keywords":["refund", "money back", "return"],
        "response": "I'd be happy to help you process your return. Let me transfer you to a live agent."
    }
}

def get_response(message):
    message.lower()
    # Check if message has any keywords with pre-defined intents
    for key in intents.keys():
        if any(word in message for word in intents[key]["keywords"]):
            return intents[key]["response"]    
    # Analyze the sentiment of the message 
    sentiment = TextBlob(message).sentiment.polarity
    return ("That's great to hear!" if sentiment > 0 else
            "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
            "I see. Could you tell me more about that?") 

def chat():
    print("Chatbot: Hi, How can I help you today?")
    # Loop until user decides to end chat
    while (user_message := input("You: ").strip().lower()) not in ['quit','exit','bye']:
        print(f"\nChatbot: {get_response(user_message)}")
    print("Chatbot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    chat()