import tiktoken
def calcular_tokens(texto, modelo="ollama3:1b"):
    
    try:
        codificador = tiktoken.get_encoding("cl100k_base")
        tokens_lista = codificador.encode(texto)

        return len(tokens_lista)
        
    except Exception as e:
        print(f"Aviso: Erro ao calcular tokens ({e}). Usando aproximação.")
        return len(texto) // 4

