"""
Arquivo para scripts de processamento de dados
"""

import numpy as np
import pandas as pd
import nltk
import stanza
nltk.download('all', quiet=True)
stanza.download('pt', verbose=False)

def tokenize_text_and_get_stats(text, nlp_pipeline, stopword_list=None):
    """
    Função para tokenizar um texto. 
    Texto deve etar na coluna 'text'
    Retorna uma tupla com 4 valores:
    - Word_list (tokens de palavras, excluindo stopwords)
    - Lemma_list (tokens de lemmas das palavras, desde que a palavra original não seja stopword)
    - Tamanho médio de frases do texto (em palavras, excluindo stopwords e pontuação)
    - Tamanho médio de palavras no texto (excluindo stopwords e pontuação)
    """
    if stopword_list is None:
        stopword_list = []
    
    processed = nlp_pipeline(text)
    word_list = []
    lemma_list = []

    word_avg_lengths = []

    sentence_lengths = []
    for sent in processed.sentences:
        local_word_list = []
        local_word_lengths = []
        for word in sent.words:
            if word.text.lower() in stopword_list or word.pos == 'PUNCT':
                continue
            local_word_list.append(word.text)
            lemma_list.append(word.lemma)
            local_word_lengths.append(len(word.text))

        sentence_lengths.append(len(local_word_list))

        word_list.extend(local_word_list)
        avg_word_len = np.mean(local_word_lengths)
        word_avg_lengths.append(avg_word_len)
    
    return word_list, lemma_list, np.mean(sentence_lengths), np.mean(word_avg_lengths)


def tokenize_df_row_and_get_stats(df_row, nlp_pipeline, stopword_list=None, n_print=100):
    """
    Função para tokenizar um texto localizado em uma linha de um DataFrame. 
    Texto deve etar na coluna 'text'
    Retorna uma tupla com 4 valores:
    - Word_list (tokens de palavras, excluindo stopwords)
    - Lemma_list (tokens de lemmas das palavras, desde que a palavra original não seja stopword)
    - Tamanho médio de frases do texto (em palavras, excluindo stopwords e pontuação)
    - Tamanho médio de palavras no texto (excluindo stopwords e pontuação)
    """
    
    if n_print is not None and df_row.name % n_print == 0:
        print(f'Processando linhas {df_row.name} a {df_row.name+n_print-1}...')
    text = df_row['text']
    return tokenize_text_and_get_stats(text, nlp_pipeline, stopword_list)


def create_tokenized_df(base_df, remove_nao=True):
    """
    Função para criar colunas no DataFrame referentes à tokenização
    """
    if 'text' not in base_df.columns:
        return base_df
    
    df = base_df.copy()
    nlp = stanza.Pipeline('pt', processors='tokenize,mwt,pos,lemma')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    if remove_nao:
        stopwords.remove('não')
    stopwords.append('r')
    df[['words', 'lemmas', 'avg_sent_len', 'avg_word_len']] = df.apply(tokenize_df_row_and_get_stats, axis=1,
                                                                       result_type='expand',
                                                                       stopword_list=stopwords,
                                                                       nlp_pipeline=nlp)
    return df