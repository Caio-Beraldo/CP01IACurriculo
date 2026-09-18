import re

def aplicar_filtros_deterministicos(texto_pdf, tempo_mininimo, orcamento):
    texto_lower = texto_pdf.lower()
    aprovado = True
    motivos_reprovacao = []
    padrao_experiencia = r'(\d+)\s*(?:anos?|ano)\s*(?:de\s*)?(?:experiência|experiencia)'
    experiencias = re.findall(padrao_experiencia, texto_lower)
    anos_experiencia = 0
    if experiencias:
        for ano in experiencias:
            anos_experiencia = max(int(ano))
    if anos_experiencia < tempo_mininimo:
        aprovado = False
        motivos_reprovacao.append("Experiência Insuficiente!")

            
    padrao_salario = (
        r'(?:pretensão salarial|pretensao salarial|'
        r'pretensão|pretensao|salário desejado|salario desejado)'
        r'.{0,30}?'
        r'(?:r\$\s*)?'
        r'(\d{1,3}(?:\.\d{3})*|\d+)'
    )
    correspondencias = re.findall(padrao_salario, texto_lower)
    valores_encontrados = []
    for val in correspondencias:
        val_limpo = val.replace('.', '')
        if val_limpo.isdigit():
            valores_encontrados.append(int(val_limpo))  
    if valores_encontrados:
        faixa_salarial = max(valores_encontrados)
        if faixa_salarial > orcamento:
            aprovado = False
            motivos_reprovacao.append(f"Nosso orçamento nao atende a faixa salarial proposta.")
    return aprovado, motivos_reprovacao