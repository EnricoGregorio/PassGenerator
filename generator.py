import random

# Definição dos diferentes caracteres disponíveis.
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
numbers = '0123456789'
symbols = '[]{};/\\~^´`\'\"?:<>,.!@#$%¨&*()-_=+ç'

# Agrupamento de todos os caracteres em uma única variável.
all = lower + upper + numbers + symbols

# Definição do tamanho da senha (em caracteres).
length = 10

# Formando a senha.
password = ''.join(random.sample(all, length))

# Retorno da senha.
print(password)
