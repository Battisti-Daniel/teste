faturamento = {'SP': 67836.34, 'RJ': 36678.66,
               'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total = sum(faturamento.values())

for key, value in faturamento.items():
    percent = (value / total) * 100
    print(f"O estao de {key} teve um total de {percent:.2f}% de representação")
