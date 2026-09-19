import ollama
from calcularTokens import calcular_tokens

def analisar_curriculo_com_llm(texto_curriculo):
   
    modelo = "ollama3:1b"
    prompt = f"""

Você é um especialista em recrutamento de desenvolvedores.

Analise o currículo abaixo.

Produza:

1. Senioridade provável do candidato.
2. Principais soft skills identificadas.
3. Parecer qualitativo.
4. Resumo executivo para o recrutador.

Não invente informações que não estejam presentes no currículo.

CURRÍCULO:
{texto_curriculo}
"""
    tokens_entrada = calcular_tokens(prompt, modelo)

    resposta = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    
    tokens_saida = calcular_tokens(resposta["message"]["content"], modelo)
    total_tokens = tokens_entrada + tokens_saida

    relatorio = {
        "modelo": modelo,
        "tokens_entrada": tokens_entrada,
        "tokens_saida": tokens_saida,
        "tokens_totais": total_tokens
    }
    
    return resposta["message"]["content"], relatorio


