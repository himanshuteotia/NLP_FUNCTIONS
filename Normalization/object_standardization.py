
#lookup_dict = {"rt":"Retweet","dm":"direct message","awsm" : "awesome","luv" :"love", "..."}

lookup_dict = {"rt":"Retweet","dm":"direct message","awsm":"awesome","luv":"love"}

def _lookup_words(input_text):
    words = input_text.split()
    new_words = []
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word)
    new_text = " ".join(new_words)
    return new_text

print(_lookup_words("I would luv to DM you"))