"Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:• O menor valor de faturamento ocorrido em um dia do mês;• O maior valor de faturamento ocorrido em um dia do mês;• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.IMPORTANTE:a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"

import json

def calculo_faturamento(file_path):
    try:
        with open(file_path, 'r') as file:
            dados = json.load(file)
    except FileNotFoundError:
        return "Arquivo não encontrado."
    except json.JSONDecodeError:
        return "Erro ao decodificar o arquivo JSON."

    
    if not isinstance(dados, list) or not all(isinstance(item, dict) and 'valor' in item for item in dados):
        return "Formato de dados inválido."

    faturamento_diario = [registro['valor'] for registro in dados if registro['valor'] > 0]

    if not faturamento_diario:
        return "Não há dados de faturamento para processar."

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

file_path = 'dados.json'

resultados = calculo_faturamento(file_path)

if isinstance(resultados, dict):
    print(f"Menor valor de faturamento: {resultados['menor_faturamento']}")
    print(f"Maior valor de faturamento: {resultados['maior_faturamento']}")
    print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_media']}")
else:
    print(resultados)
