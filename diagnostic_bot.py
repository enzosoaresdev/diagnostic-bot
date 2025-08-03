perguntas = [
    {
        "pergunta": "O problema é relacionado à internet?",
        "solucao": "Reinicie o roteador e verifique os cabos.",
    }
]

for pergunta in perguntas:
    comando = input(f'{pergunta["pergunta"]} (s/n): ')
    if comando.lower() == "s":
        print(f'{pergunta["solucao"]}')
