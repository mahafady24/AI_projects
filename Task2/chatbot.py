import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')


faq_data = {
    "What is Artificial Intelligence?": "Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "What is machine learning?": "Machine learning is a subset of AI that involves the development of algorithms that allow computers to learn from and make decisions based on data.",
    "What is deep learning?": "Deep learning is a subset of machine learning that uses neural networks with many layers (deep architectures) to analyze and learn from large amounts of data.",
    "What is natural language processing?": "Natural language processing (NLP) is a field of AI that focuses on the interaction between computers and humans through natural language.",
    "What are neural networks?": "Neural networks are computing systems inspired by the biological neural networks that constitute animal brains.",
    "What is reinforcement learning?": "Reinforcement learning is an area of machine learning where an agent learns to make decisions by performing actions in an environment to maximize cumulative reward.", 
    "What are the different types of AI?": "There are 2 Types. Type 1 involves Narrow AI, General AI, And Super AI. For type 2, it involves Reactive Machine, Limited theory, Theory of mind, Self-Awareness.",
    "How does AI work?": "AI adapts through progressive learning algorithms to let the data do the programming. AI finds structure and regularities in data so that algorithms can acquire skills. Just as an algorithm can teach itself to play chess, it can teach itself what product to recommend next online.",
    "How can I benefit from AI?": "Increased business efficiency, Improved decision-making, Enhanced customer experiences, Optimized marketing strategies, and much more.",
    "What kind of computers are used for AI?": "AI runs on a special kind of enterprise-grade computer called a server. Personal computers and mobile devices can also run AI, but their capabilities are severely limited by the consumer-grade hardware. This is why most AI services require an internet connection, so that your PC or smartphone can connect to the computing resources on the cloud.",
}


def preprocess_text(text): #Defines a function called preprocess_text that will take an input string (text), process it, and return the cleaned version.
    stop_words = set(stopwords.words('english')) # Loads the English stopwords (common words like "the", "is", "and") into a Python set to make them easy to remove later. So We remove stopwords because they don't add much meaning and just add noise to the data.
    lemmatizer = WordNetLemmatizer() #Initializes a lemmatizer, which will convert words to their base forms.  Lemmatization helps normalize words to their root forms, so "run" and "running" are treated as the same word.
    tokens = word_tokenize(text.lower()) #Converts the input text to lowercase (text.lower()) and breaks it into individual words using the word_tokenize() function. Tokenization allows us to work with individual words rather than entire sentences, which is necessary for matching questions.
    processed_text = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return processed_text


def find_best_match(user_question, faq_data): # Getting the question from faq_data that matches the user's question
    processed_user_question = preprocess_text(user_question)
    best_match = None #Initializes best_match to None, which will store the best matching question.
    max_overlap = 0 #Initializes max_overlap to 0, which will store the highest number of overlapping words between the user question and the FAQ questions.

    for question in faq_data.keys():
        processed_faq_question = preprocess_text(question)
        overlap = len(set(processed_user_question) & set(processed_faq_question)) 
    
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = question

    if best_match:
        return best_match, faq_data[best_match]
    else:
        return None, "Sorry, I don't have an answer for that."


# Chatbot interface function (CLI)
def chatbot():
    print("Hello! I can answer questions about AI and its new technologies.")
    print("Type 'exit' or 'quit' to end the chat.\n")
    
    while True:
        user_question = input("You: ")

        # Exit condition
        if user_question.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break

        # Find the best match for the user's question
        question, answer = find_best_match(user_question, faq_data)

        # Print the chatbot's response
        print(f"Chatbot: {answer}\n")



if __name__ == "__main__":
    chatbot()