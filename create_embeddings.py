import ollama

def main():
    model_name = 'llama3.2'
    text = 'Exemplo de texto para gerar embeddings com Ollama.'

    embeddings = ollama.embed(model=model_name, input=text)
    vector = embeddings['embedding']

    print(f'Vetor de embeddings (tamanho: {len(vector)}):')
    print('Primeiros 5 valores:', vector[:5])

if __name__ == '__main__':
    main()
