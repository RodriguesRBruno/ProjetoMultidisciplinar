"""
Arquivo para scripts de plots
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import seaborn as sns
nltk.download('all', quiet=True)

def plot_cloud(words_string):
    """
    Função para plotar nuvem de palavras
    """
    nuvem_palavras = WordCloud(width= 1000, height= 800, max_font_size = 110, collocations=False).generate(words_string)
    plt.figure(figsize=(12,8))
    plt.imshow(nuvem_palavras, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    
def plot_word_counts(tokens, n=10):
    """
    Função para plotar gráfico com contagens das 'n' palavras mais comuns presentes nos 'tokens'
    """
    frequency = nltk.FreqDist(tokens)
    df_frequency = pd.DataFrame({"Word": list(frequency.keys()),
                                 "Frequency": list(frequency.values())})
    plt.figure(figsize=(16,8))
    ax = sns.barplot(data = df_frequency.sort_values(by=['Frequency'], ascending=False).head(n), x = "Word", y = "Frequency")
    ax.set(ylabel = "Count")
    plt.show()