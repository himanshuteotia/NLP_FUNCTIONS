import spacy 

def load_model(type):
    try:
        if type == 'lg':
            nlp = spacy.load("en_core_web_lg")
        elif type == 'md':
            nlp = spacy.load("en_core_web_md")
        else:
            nlp = spacy.load("en_core_web_sm")
        return nlp
    except Exception as e:
        print("An exception occurred in model loading : ",e)
        return "please install the module " + type

model = load_model('md')



