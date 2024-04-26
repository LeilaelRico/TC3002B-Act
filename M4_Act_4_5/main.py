import nltk
import os
import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def preprocess_code(code):
    code = '\n'.join(line for line in code.split('\n') if not line.strip().startswith('//'))
    code = ' '.join(code.split())
    return code

def tokenize_code(code):
    tokens = word_tokenize(code)
    return tokens

def calculate_markov_chain(tokens):
    return nltk.FreqDist(nltk.ngrams(tokens, 2))

def calculate_cosine_similarity(code1, code2):
    code1_tokens = tokenize_code(preprocess_code(code1))
    code2_tokens = tokenize_code(preprocess_code(code2))

    markov_chain1 = calculate_markov_chain(code1_tokens)
    markov_chain2 = calculate_markov_chain(code2_tokens)

    # Convertir los modelos de cadenas de Markov en vectores TF-IDF
    vectorizer = TfidfVectorizer(tokenizer=lambda x: x, lowercase=False)
    vectors = vectorizer.fit_transform([markov_chain1, markov_chain2])

    # Calcular la similitud coseno entre los vectores
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return similarity

def main():
    file1_path = '.\\M4_Act_4_5\\f0.c'
    file2_path = '.\\M4_Act_4_5\\f1.c'

    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        code1 = file1.read()
        code2 = file2.read()

    code1_tokens = tokenize_code(preprocess_code(code1))
    code2_tokens = tokenize_code(preprocess_code(code2))

    markov_chain1 = calculate_markov_chain(code1_tokens)
    markov_chain2 = calculate_markov_chain(code2_tokens)

    # Crear DataFrame para la matriz de cadenas de Markov
    df = pd.DataFrame([dict(markov_chain1), dict(markov_chain2)]).fillna(0)

    print("Matriz de cadenas de Markov:")
    print(df)

    # Calcular la similitud coseno
    similarity = calculate_cosine_similarity(code1, code2)

    print(f"\nSimilitud coseno entre los dos códigos: {round(similarity, 4)}")

if __name__ == "__main__":
    main()
