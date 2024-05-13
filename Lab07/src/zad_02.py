import re
import text2emotion as te
import emoji
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

from nltk import tokenize

sentiPositive = "Great hostel for the paid value. For those who expect to pay hostel price and get ***** HOTEL it will be huge disappointment but for reasonable people who are on budget traveling and they are wise enough to realise that paying value what you pay for this hostel is way lower than any other accommodation in Split, you would be satisfied. Hostel is fictional, beds are comfortable and it has all necessary facilities. Even free laundry and dryer. I like everything. It is good value and that is it. Probably for people who are “paying for bottle of water and expecting to get wine” would be disappointment."

sentiNegative = "They gave a a broken key. I was struggled to lock my door but I managed to do it somehow after 20 minutes. When I came back the same night, I wasn’t able to open it with the key. The other guest got woken up by my attempts to open the door and couldn’t sleep. They tried to help me, but it wouldn’t work. The next day when the maintenance guy came, he confirmed that the key they gave me was broken & he gave me a new one. I had to find another place to stay for a whole night and pay for it although I’ve already paid for a night for that place, which is not acceptable under any circumstances. The key should have been checked before being given to me. Someone didn’t do their job right and I demand compensation. The heater also didn’t work properly but in comparison to the broken key and not being able to sleep in the room I paid for, it was just a minor problem"

lines_list_Pos = tokenize.sent_tokenize(sentiPositive)
lines_list_Neg = tokenize.sent_tokenize(sentiNegative)

print("a) b)")

def calculate_sentiment_average(array):
    sid = SentimentIntensityAnalyzer()
    total_compound = 0
    total_neg = 0
    total_neu = 0
    total_pos = 0
    num_sentences = len(array)

    for sentence in array:
        ss = sid.polarity_scores(sentence)
        total_compound += ss['compound']
        total_neg += ss['neg']
        total_neu += ss['neu']
        total_pos += ss['pos']

    avg_compound = total_compound / num_sentences
    avg_neg = total_neg / num_sentences
    avg_neu = total_neu / num_sentences
    avg_pos = total_pos / num_sentences

    return avg_compound, avg_neg, avg_neu, avg_pos

avg_compound_pos, avg_neg_pos, avg_neu_pos, avg_pos_pos = calculate_sentiment_average(lines_list_Pos)
avg_compound_neg, avg_neg_neg, avg_neu_neg, avg_pos_neg = calculate_sentiment_average(lines_list_Neg)

print(f"Średnia wartość compound (pozytywne): {avg_compound_pos:.2f}")
print(f"Średnia wartość neg (pozytywne): {avg_neg_pos:.2f}")
print(f"Średnia wartość neu (pozytywne): {avg_neu_pos:.2f}")
print(f"Średnia wartość pos (pozytywne): {avg_pos_pos:.2f}")

print(f"Średnia wartość compound (negatywne): {avg_compound_neg:.2f}")
print(f"Średnia wartość neg (negatywne): {avg_neg_neg:.2f}")
print(f"Średnia wartość neu (negatywne): {avg_neu_neg:.2f}")
print(f"Średnia wartość pos (negatywne): {avg_pos_neg:.2f}")

print("c)")


emotion_scores_pos = te.get_emotion(sentiPositive)
print("Positive opinion:")
print(emotion_scores_pos)
emotion_scores_neg = te.get_emotion(sentiNegative)
print("Negative opinion:")
print(emotion_scores_neg)


# d) Wyniki są nie wpełni zgodne z oczekiwaniami, ponieważ w pozytywnej opini było mniej smutku niż w negatywnej.


# def is_pos_is_neg_is_neu(array):
#   counter = 0
#   count_compound = 0
#   count_neu = 0
#   count_pos = 0
#   count_neg = 0
#   for sentence in array:
#     sid = SentimentIntensityAnalyzer()
#     print(sentence)
#     ss = sid.polarity_scores(sentence)
#     counter+=1
#     for k in sorted(ss):
#       print('{0}: {1}, '.format(k, ss[k]), end='')
#     print()
# print("\nPositive sentence : \n")
# is_pos_is_neg_is_neu(lines_list_Pos)
# print("\nNegative sentence : \n")
# is_pos_is_neg_is_neu(lines_list_Neg)

