# NLP Chatbot

This project is a simple NLP-based chatbot using the Blenderbot model from the Hugging Face Transformers library.

## Project Structure

- `NLPChatbot.py`: Main script to run the chatbot.

## Requirements

- Python 3.6+
- pip

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/amitwadhwa83/NLPChatbot.git
    cd NLPChatbot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the chatbot:
```sh
python NLPChatbot.py
```

##  How It Works
The script loads the Blenderbot model and tokenizer from the Hugging Face Transformers library.
It starts a conversation loop where the user can input text.
The input is tokenized and passed to the model to generate a response.
The response is decoded and printed to the console.