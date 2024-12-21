Deliverable Report

Code:

The provided code effectively incorporates the following functionalities:

1.	Task Selection: Allows users to choose between five tasks:
o	Text Generation.
o	Text Summarization.
o	Sentiment Analysis.
o	Creative Prompt Engineering.
o	Zero-shot Classification.
2.	Flexible Inputs:
o	Prompts and paragraphs are dynamically accepted from the user.
o	Parameters like max_length, temperature, top_p, and top_k are configured to experiment with output quality.
3.	Models:
o	GPT-2 for text generation and creative prompt engineering.
o	Facebook/BART for summarization and zero-shot classification.
o	DistilBERT for sentiment analysis.
________________________________________
Advanced Experimentation with Parameters
1.	Impact of Parameters:
o	Temperature: Higher values (e.g., 0.9) yield more creative but less coherent results, while lower values (e.g., 0.7) provide more deterministic responses.
o	Max_length: Controls the verbosity of the output; excessively high values often result in repetitive content.
o	Top_p: Lower values limit randomness; higher values encourage diversity at the cost of relevance.
o	Top_k: Restricts token selection; smaller values enforce strict control but can sacrifice creative diversity.
o	Truncation: Controls whether or not the input text should be truncated if it exceeds the model’s maximum input length.
o	pad_token_id: Refers to the ID of a special padding token used to make all inputs or outputs the same length during training or inference.
	In most GPT-like models, the padding token ID is 50256. [USED]
	In BERT-based models, it might correspond to [PAD].
2.	Findings:
o	Creative and coherent outputs require fine-tuning these parameters together, based on the specific task.
________________________________________
