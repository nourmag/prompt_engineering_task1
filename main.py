from transformers import pipeline

def main():
    print("Select the task you want to perform:")
    print("1: Text Generation")
    print("2: Text Summarization")
    print("3: Sentiment Analysis")
    print("4: Creative Prompt Engineering")
    print("5: Zero-shot Classification")

    # Get user choice
    choice = input("Enter the number corresponding to your task: ").strip()

    # Initialize variables
    task = None
    model_name = None
    model1 = "gpt2"
    model2 = "facebook/bart-large-cnn"
    model3 = "distilbert-base-uncased-finetuned-sst-2-english"

    # Determine the pipeline and task based on the choice
    if choice == "1" or choice == "4":  # Both use text generation
        task = "text-generation"
        model_name = model1
    elif choice == "2":
        task = "summarization"
        model_name = model2
    elif choice == "3":
        task = "sentiment-analysis"
        model_name = model3
    elif choice == "5":
        task = "zero-shot-classification"
        model_name = model2
    else:
        print("Invalid choice. Please run the program again.")
        return

    # Initialize pipeline
    print("Initializing pipeline...")
    pipeline_instance = pipeline(task, model=model_name)

    # Get user input based on task
    if choice in ["1", "4"]:  # Text Generation or Creative Prompt Engineering
        prompt = input("Enter your prompt: ").strip()

        output = pipeline_instance(prompt, max_length= 200, temperature= 0.8, top_p=0.9, top_k = 5, pad_token_id = 50256)[0]['generated_text']
        print("\nGenerated Text:")
        print(output)

    elif choice == "2":  # Summarization
        paragraph = input("Paste the paragraph to summarize: ").strip()

        summary = pipeline_instance(paragraph, max_length= 200, min_length= 50, truncation=True)[0]['summary_text']
        print("\nSummary:")
        print(summary)

    elif choice == "3":  # Sentiment Analysis
        text = input("Enter the text for sentiment analysis: ").strip()

        sentiment = pipeline_instance(text)
        print("\nSentiment Analysis Result:")
        print(sentiment)

    elif choice == "5":  # Zero-shot Classification
        text = input("Enter the text to classify: ").strip()
        candidate_labels = input("Enter candidate labels separated by commas: ").strip().split(',')

        classification = pipeline_instance(text, candidate_labels)
        print("\nClassification Result:")
        print(classification)

if __name__ == "__main__":
    main()
