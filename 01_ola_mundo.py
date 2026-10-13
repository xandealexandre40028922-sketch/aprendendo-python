nome = input("Qual Seu Nome? ")
idade = int(input("Quantos Anos Você tem? "))

print("Olá " + nome + "!")

# Se a pessoa tiver menos de 18 anos
if idade < 18:
    anos_para_18 = 18 - idade
    print("Faltam " + str(anos_para_18) + " anos para você completar 18 anos.")

# Se a pessoa tiver exatamente 18 anos
elif idade == 18:
    print("Você acabou de completar 18 anos!")

# Se a pessoa já for maior de 18 anos
else:
    anos_passados = idade - 18
    print("Você já é maior de idade há " + str(anos_passados) + " anos.")
