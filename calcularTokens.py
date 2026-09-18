import tiktoken
def calcular_tokens(texto, modelo="gpt-4o-mini"):
    
    try:
        codificador = tiktoken.encoding_for_model(modelo)
        tokens_lista = codificador.encode(texto)

        return len(tokens_lista)
        
    except Exception as e:
        print(f"Aviso: Erro ao calcular tokens ({e}). Usando aproximação.")
        return len(texto) // 4

