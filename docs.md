**Natural Language Processing**

NLP is a branch of data science that consists of systematic ( व्यवस्थित ) processes for analyzing, understanding, and deriving information from the text data in a smart and efficient manner.


By utilizing NLP and its components, one can organize the massive chunks of text data, perform numerous automated tasks and solve a wide range of problems such as – automatic summarization, machine translation, named entity recognition, relationship extraction, sentiment analysis, speech recognition, and topic segmentation etc.


Tokenization – process of converting a text into tokens

Tokens – words or entities present in the text

Text object – a sentence or a phrase or a word or an article



**1. Text Preprocessing**

Since, text is the most unstructured form of all the available data, various types of noise are present in it and the data is not readily ( आसानी से ) analyzable without any pre-processing. The entire process of cleaning and standardization of text, making it noise-free and ready for analysis is known as text preprocessing.


It is predominantly (मुख्य रूप से) comprised (शामिल) of three steps:

Noise Removal

Lexicon Normalization

Object Standardization


Raw Text ----> Noisy Entities Removal (stopwords,URL's, punctations,mentions etc ) ---> Word Normalization ( Tokenization, Lemmatization, Stemming ) ----> Word Standardization ( Regular Expression, Lookup Tables ) ---> Clened Text 


Noide Removal :


An peice of text which is not relevant to the context of the data and the end-output can be specified as the noise.

> language stopwords
> URL, LINKS , social media entities( mentions , hashtags)
> Punctuations
> Industry specific words

