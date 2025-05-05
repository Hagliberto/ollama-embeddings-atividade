# create_embeddings.py
import ollama

def main():
    model_name = 'llama3.2'
    text = 'Gerando embeddings com Ollama.'

    # Gera a resposta (EmbedResponse)
    response: ollama.EmbedResponse = ollama.embed(model=model_name, input=text)

    # Extrai o vetor: response.embeddings é uma lista de listas [[...]]
    vector = response.embeddings[0]

    print(f'Vetor de embeddings (tamanho: {len(vector)}):')
    print('Primeiros 5 valores:', vector[:5])

if __name__ == '__main__':
    main()
