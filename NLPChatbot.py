from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Start a conversation loop
print("Chatbot: Hi! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Tokenize input and generate response
    inputs = tokenizer(user_input, return_tensors="pt")
    response_ids = model.generate(**inputs)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)

    print("Chatbot:", response)
