import sys
import unittest

sys.path.append("..")
import spacy
from ml_utils.ner_extractor import extract_named_entities


class TestNERMethods(unittest.TestCase):
    def test_person(self):
        sentence = "I am Hamza."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"Hamza": "PERSON"})

    def test_organization(self):
        sentence = "He worked at Microsoft"
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"Microsoft": "ORG"})

    def test_money(self):
        sentence = "He earns 500k dollars a year."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"500k dollars": "MONEY"})

    def test_gpe(self):
        sentence = "He lives in India."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"India": "GPE"})

    def test_location(self):
        sentence = "He went to Mount Everest."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"Mount Everest": "LOC"})

    def test_date(self):
        sentence = "He was born in 9th May 1987."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {"9th May 1987": "DATE"})

    def test_combo(self):
        sentence = "In 9th May 1987, he went to Mount Everest and earned 500k dollars."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(
            nes,
            {"9th May 1987": "DATE", "Mount Everest": "LOC", "500k dollars": "MONEY"},
        )

    def test_no_ner(self):
        sentence = "I am me."
        nlp = spacy.load("en_core_web_md")
        nes = extract_named_entities(nlp, sentence)
        self.assertEqual(nes, {})


if __name__ == "__main__":
    unittest.main()
