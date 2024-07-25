from textblob import TextBlob


def grammer_check(text):
    text_to_be_blobed = TextBlob(text)
    correct_text = str(text_to_be_blobed.correct())
    return correct_text
    
sentence = input()
print(grammer_check(sentence))