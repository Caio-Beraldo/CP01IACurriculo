from pypdf import PdfReader

def extrair_texto_pdf(caminho_arquivo):
    try:
        leitor = PdfReader(caminho_arquivo)
        texto_acumulado = ""
        for pagina in leitor.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_acumulado += texto_pagina + "\n"
        return texto_acumulado
        
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF {caminho_arquivo}: {e}")
        return ""