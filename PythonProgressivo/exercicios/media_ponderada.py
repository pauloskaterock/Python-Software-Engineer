# Desafio de Python - Média Ponderada
# A prova do vestibular do IME (Instituto Militar de Engenharia), é composta pelas provas de Matemática, Física, Química, Português e Inglês apenas. Porém, elas tem pesos diferentes. O peso de Matemática é 3, de Física é 2.5, de Química também é 2.5, Português tem peso 1 e Inglês também tem peso

# Crie um programa em Python que peça as 5 notas para o usuário e calcule sua média final.

print("🎓 CÁLCULO DE MÉDIA PONDERADA")


# Pesos das matérias
PESO_MATEMATICA = 3.0
PESO_FISICA = 2.5
PESO_QUIMICA = 2.5
PESO_PORTUGUES = 1.0
PESO_INGLES = 1.0

# Entrada das notas
print("\n📝 Digite as notas (0 a 10):\n")

matematica = float(input("Matemática (peso 3): "))
fisica = float(input("Física (peso 2.5): "))
quimica = float(input("Química (peso 2.5): "))
portugues = float(input("Português (peso 1): "))
ingles = float(input("Inglês (peso 1): "))

# Cálculo da média ponderada
soma_pesos = PESO_MATEMATICA + PESO_FISICA + PESO_QUIMICA + PESO_PORTUGUES + PESO_INGLES
soma_notas_ponderadas = (
    matematica * PESO_MATEMATICA +
    fisica * PESO_FISICA +
    quimica * PESO_QUIMICA +
    portugues * PESO_PORTUGUES +
    ingles * PESO_INGLES
)

media = soma_notas_ponderadas / soma_pesos

# Resultado
print("\n" + "=" * 50)
print("📊 RESULTADO:")
print("=" * 50)
print(f"Matemática: {matematica:.1f} (peso {PESO_MATEMATICA})")
print(f"Física:     {fisica:.1f} (peso {PESO_FISICA})")
print(f"Química:    {quimica:.1f} (peso {PESO_QUIMICA})")
print(f"Português:  {portugues:.1f} (peso {PESO_PORTUGUES})")
print(f"Inglês:     {ingles:.1f} (peso {PESO_INGLES})")
print("-" * 50)
print(f"🎯 Média Final: {media:.2f}")
print("=" * 50)

# Mensagem de aprovação (opcional)
if media >= 7.0:
    print("\n✅ PARABÉNS! Você está APROVADO!")
elif media >= 5.0:
    print("\n⚠️ Você está na LISTA DE ESPERA!")
else:
    print("\n❌ Infelizmente você foi REPROVADO.")
