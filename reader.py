from pypdf import PdfReader

def extrair_pdf(arquivo):
    try:
        leitor = PdfReader(arquivo)
        texto_acumulado = ""
        for pagina in leitor.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_acumulado += texto_pagina + "\n"
        return texto_acumulado
        
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF {arquivo}: {e}")
        return ""