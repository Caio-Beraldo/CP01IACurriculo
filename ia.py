from openai import OpenAI
from calcularTokens import calcular_tokens
client = OpenAI()
def analisar_curriculo_com_llm(texto_curriculo):
    modelo = "gpt-5.6-luna"
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

    resposta = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    
    tokens_saida = calcular_tokens(resposta, modelo)
    total_tokens = tokens_entrada + tokens_saida

    relatorio = {
        "modelo": modelo,
        "tokens_entrada": tokens_entrada,
        "tokens_saida": tokens_saida,
        "tokens_totais": total_tokens
    }
    
    return resposta.output_text, relatorio


