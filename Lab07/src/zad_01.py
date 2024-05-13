import nltk
import spacy
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')
from collections import Counter
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize 

with open("TraumaSurgeon.txt", "r") as file:
    text = file.read()

text_tokenize = word_tokenize(text)
print("a) b)")
print("Before tokenize ", len(sent_tokenize(text)))
print("After tokenize ", len(word_tokenize(text)))

english_stopwords = set(stopwords.words('english'))
filtered_sentence = [w for w in text_tokenize if w.lower() not in english_stopwords]
print("c)")
print(len(filtered_sentence))

# Add any additional stopwords here
english_stopwords.update([':', ',', '.', "'", '``', "''", '-', '_'])
filtered_sentence = [w for w in text_tokenize if w.lower() not in english_stopwords]
print("d)")
print(len(filtered_sentence))

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_sentence]

# print(filtered_sentence)
print("e)")
print(len(lemmatized_tokens))


# Create a word count vector
word_counts = Counter(lemmatized_tokens)
# Get the top 10 most frequent words
top_10_words = word_counts.most_common(10)
# Create a bar chart
plt.bar(range(len(top_10_words)), [word[1] for word in top_10_words], align='edge')
plt.xticks(range(len(top_10_words)), [word[0] for word in top_10_words], rotation=90)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.show()

print("g)")

# Zmień rozmiar chmury tagów
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(' '.join(lemmatized_tokens))

# Wyświetl chmurę tagów
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()

# Join the lemmatized tokens into a sentence
# lemmatized_text = ' '.join(lemmatized_tokens)