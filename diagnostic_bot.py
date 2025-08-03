import os

knowledge_base = [
    {
        "question": "O problema é relacionado à internet?",
        "solution": "Verifique os cabos.",
    }
]

while True:
    os.system("cls" if os.name == "nt" else "clear")
    answer = False
    for question in knowledge_base:
        while True:
            command = input(f"{question['question']} (s/n): ").lower().strip()
            if command in ["s", "n"]:
                break
            else:
                print("Digite apenas 's' para sim ou 'n' para não.")

    if command == "s":
        print(f"Sugestão: {question['solution']}")
        answer = True
        break

    if not answer:
        new_solution = input("Desisto! Qual era a solução para seu problema? ")
        new_question = input("Qual dúvida 'sim/não' para solucionar o caso? ")
        knowledge_base.append({"question": new_question, "solution": new_solution})
        print(">>> Nova regra aprendida. Obrigado.")

        try_again = input("Iniciar um novo diagnóstico? (s/n): ").lower().strip()
        if try_again != "s":
            print("Sistema encerrando. Até a próxima!")
            break
