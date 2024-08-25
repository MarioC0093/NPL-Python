import pandas as pd
from IPython.display import Markdown, display
import re
from collections import Counter
# Import text from url
import requests
# Colores
from termcolor import colored # Solo funciona dentro del notebook
from rich.console import Console # Este paquete logra reflejarlo en el HTML
console = Console(record=True)
# NPL en general
import spacy
# Tokenizacion
import nltk
from nltk.tokenize import word_tokenize
# Stop Words
from nltk.corpus import stopwords
# Steamming and Lemmatization
import nltk
from nltk.stem.snowball import SnowballStemmer
# ENT
from spacy import displacy