import json
from socket  import socket, AF_INET, SOCK_STREAM
from constCS import HOST, PORT

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

print('''
Operações disponíveis:
1. "sum a b": soma "a" e "b"
2. "sub a b": subtrai "a" de "b"
3. "mul a b": multiplica "a" e "b"
4. "div a b": divide "b" por "a"
5. "exit": encerra a conexão
''')

while True:
    command = input("> ")

    if command.startswith("exit"):
        break
    else:
        # Codificando os dados em um formato enviável
        encoded_data = json.dumps(command).encode('utf-8')
        
        # Enviando os dados
        s.send(encoded_data)

        # Recebendo a resposta e especificando a leitura de até 1024 bytes
        response = s.recv(1024)
        if not response:
            break

        # Exibindo a resposta
        print(response.decode("utf-8"))

s.close() # Encerrando a conexão
