def extract_named_entities(nlp, query):
    doc = nlp(query)
    return dict([(item.text, item.label_) for item in doc.ents])