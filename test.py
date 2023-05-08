from transformers import pipeline
import argparse


def extract_entities(sequence):
    model_name = './restaurant-model'
    nlp = pipeline(task="ner", model=model_name, tokenizer=model_name, framework="pt", grouped_entities=True)
    return nlp(sequence)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Input sequence")
    args = parser.parse_args()
    out_entities = extract_entities(args.input)
    for entity in out_entities:
        print(f"Entity Group : {entity['entity_group']}, Word : {entity['word']}")
