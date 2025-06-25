import random

# Definição dos diferentes caracteres disponíveis.
lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = lowerLetters.upper()
numbers = "0123456789"
symbols = "[]{};/\\~^´`\'\"?:<>,.!@#$%¨&*()-_=+ç"

# Agrupamento de todos os caracteres em uma única variável.
allCaracters = lowerLetters + upperLetters + numbers + symbols

# Definição do tamanho da senha (em caracteres/dígitos).
lengthPass = 10

# Formando a senha: a cada espaço vazio (""), o programa irá iterar um caractere aleatório da String "allCaracters",
# até completar a quantidade de dígitos, informado no parâmetro "lengthPass"
password = "".join(random.sample(allCaracters, lengthPass))

# Saída da senha.
print(password)
