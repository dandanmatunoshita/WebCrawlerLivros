import pandas as pd
import csv

with open('banco_csv.csv', 'r') as arquivo:
    ler = pd.read_csv(arquivo)
    linhas = len(arquivo.readlines())
    print(ler)
    print(linhas)