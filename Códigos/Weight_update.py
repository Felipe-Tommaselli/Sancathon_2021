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
dw = 0.3*(sqrt(abs(dpdt - Mdpdt))) - 0.1*(sqrt(abs(dpdb - Mdpdb)))

''' aqui a ideia é atualiar o peso de uma certa linha ao longo do HD (horarios do dia),
só precisa ver se realmente a funcao ta fncionando suave pra atualizar os pesos, 
nesse caso é só fazer que o novo peso (nw) = peso atual (w) + dw, naquela hora do dia
Acho que da pra fazer uma tabela cheia de valores aleatorios mesmo e boa, mas é melhor 
fazer em pandas mesmo
'''

''' Caso o peso em alguma hora do dia antinja um valor critico ou se eles esteja perto disso
, guardar ele em um txt ou algo do genero sei la, acho que pra começar é melhor só pegar uns
valor criticos aleatorios normal mesmo e fazer o machine learning. 
No ML a gente tinha escolhido usar rede nerual (NN) pra fazer uma predição através de 
regressão. Pra fazer uma rede de regressão vamo usar poucas camadas escondidas so pro teste,
acho que umas 3 já dá suave com uns 10 neuronios cada? sla
mas de funcao de ativação é a SOFTPLUS a boa, de otimizar ADAM, e tem que pesquisar se a rede
vai ser RNN ou nao. Pra implementar isso só puxar um tensor flow e usar tf.keras pra fazer 
praticamente tdo.
'''