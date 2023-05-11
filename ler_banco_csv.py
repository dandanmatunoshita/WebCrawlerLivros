import pandas as pd

with open('banco_csv.csv', 'r') as arquivo:
    file = pd.read_csv(arquivo)
    print(file)