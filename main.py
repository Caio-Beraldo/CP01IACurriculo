from reader import extrair_pdf
from filter import aplicar_filtros_deterministicos
from ia import analisar_curriculo_com_llm


def executar():
    print("----------------------------------")
    print(" SISTEMA DE TRIAGEM DE CURRÍCULOS")
    print("-----------------------------------")
    caminho_pdf = "curriculo.pdf"
    texto_curriculo = extrair_pdf(caminho_pdf)
    if not texto_curriculo:
        print("Erro: não foi possível extrair o currículo.")
        return
    print("\nCurrículo carregado com sucesso.")

    experiencia_minima = 3
    orcamento_maximo = 20000

    aprovado, motivos = aplicar_filtros_deterministicos(
        texto_curriculo,
        experiencia_minima,
        orcamento_maximo
    )

    if not aprovado:
        print("\n---------------------------------")
        print("CANDIDATO REPROVADO")
        print("------------------------------------")
        for motivo in motivos:
            print(f"- {motivo}")
        return

    print("\nCandidato aprovado nos filtros determinísticos.")
    resultado, relatorio = analisar_curriculo_com_llm(texto_curriculo)
    print("ANÁLISE DO LLM")
    print(
    resultado
    + "\n\n-------------------------------\n"
    + "RELATÓRIO DE USO DE TOKENS\n"
    + "-----------------------------------------\n"
    + f"Modelo: {relatorio['modelo']}\n"
    + f"Tokens de entrada: {relatorio['tokens_entrada']}\n"
    + f"Tokens de saída: {relatorio['tokens_saida']}\n"
    + f"Tokens totais: {relatorio['tokens_totais']}\n"
    + "Custo: R$ 0,00\n"
    + "------------------------------------------"
)
    
if __name__ == "__main__":
    executar()