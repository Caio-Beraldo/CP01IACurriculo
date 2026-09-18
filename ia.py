from openai import OpenAI

client = OpenAI()
def analisar_curriculo_com_llm(texto_curriculo):

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

    resposta = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return resposta.output_text