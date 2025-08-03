perguntas = [
    {
        "pergunta": "O problema é relacionado à internet?",
        "solucao": "Reinicie o roteador e verifique os cabos.",
    }
]


while True:
    resposta = False
    for pergunta in perguntas:
        comando = input(f'{pergunta["pergunta"]} (s/n): ')
        if comando.lower().strip() == "s":
            print(f'{pergunta["solucao"]}')
            resposta = True
            break

    if not resposta:
        nova_solucao = input("Desisto. Qual era a solução para seu problema? ")
        nova_pergunta = input("Qual dúvida de 'sim/não' levaria a essa solução? ")
        perguntas.append({"pergunta": nova_pergunta, "solucao": nova_solucao})

    resposta = input("Gostaria de tentar novamente? (s/n): ")
    if resposta.lower().strip() != "s":
        break
