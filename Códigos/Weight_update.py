# Imports
import pandas as pd
import numpy as np

# Criando tabela
hd1 = pd.Series({'weight': 0.4, 'people flow/bus': 40, 'people flow/time': 10})
hd2 = pd.Series({'weight': 0.5, 'people flow/bus': 35, 'people flow/time': 36})
hd3 = pd.Series({'weight': 0.6, 'people flow/bus': 10, 'people flow/time': 9})
hd4 = pd.Series({'weight': 0.55, 'people flow/bus': 30, 'people flow/time': 7})

df = pd.DataFrame([hd1, hd2, hd3, hd4])

# A, B: Constantes a serem otimizadas pelo algoritmo
dw = A*(sqrt(abs(dpdt - Mdpdt))) - B*(sqrt(abs(dpdb - Mdpdb)))
