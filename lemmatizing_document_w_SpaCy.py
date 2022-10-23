
def lemmatizing_document(input_document):
    """


    Parameters
    ----------
    input_document : TYPE
        DESCRIPTION.

    Returns
    -------
    lemmatized_text : TYPE
        DESCRIPTION

    """
    with open(input_document) as f:
        file = f.read()

    import spacy
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(file)

    lemmas = [token.lemma_ for token in doc]

    lemmatized_text = ' '.join(map(str, lemmas))

    return lemmatized_text


if __name__ == '__main__':
    lemmatized_doc = lemmatizing_document("To_shoot_an_Elephant.txt")
