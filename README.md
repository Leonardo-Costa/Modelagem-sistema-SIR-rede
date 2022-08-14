# Modelagem computacional de uma epidemia utilizando o modelo SIR. 

Aqui será apresentado o sistema SIR de modelagem matemática de epidemias e como ele se desenvolve em função do tempo quando os parâmetros de infecção e recuperação mudam. Serão estudados os efeitos na curva de Infectados, como ela abaixa quando os valores de infecção diminuem e quando os de recuperação aumentam. Além disso o sistema será testado em uma Rede circular, tendo seu comportamento analisado na migração de infectados por entre as populações.

A modelagem do problema foi feita em cima de equações diferenciais do modelo SIR e, através do método de Euler, a implementação foi realizada em python. Os gráficos são exibidos por meio da biblioteca matplotlib.pyplot.