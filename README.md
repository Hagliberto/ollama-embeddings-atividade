# Ollama Embeddings Atividade

Este repositório contém um exemplo completo de como instalar e configurar o Ollama localmente, gerar vetores de embeddings a partir de um texto simples usando Python e organizar tudo em um ambiente de desenvolvimento (VS Code) versionado no GitHub.

---

## 📝 Conteúdo

* [Descrição](#descrição)
* [Pré-requisitos](#pré-requisitos)
* [Instalação](#instalação)
* [Configuração do Ollama](#configuração-do-ollama)
* [Uso](#uso)

  * [Executar o servidor Ollama](#executar-o-servidor-ollama)
  * [Gerar Embeddings via Script Python](#gerar-embeddings-via-script-python)
  * [Exemplo de Saída](#exemplo-de-saída)
* [Notebook Jupyter (Opcional)](#notebook-jupyter-opcional)
* [Estrutura do Repositório](#estrutura-do-repositório)
* [Vídeo de Demonstração](#vídeo-de-demonstração)
* [Solução de Problemas](#solução-de-problemas)
* [Contato](#contato)

---

## Descrição

Esta atividade tem como objetivo demonstrar:

1. Instalação e configuração do Ollama localmente.
2. Geração de vetores de embeddings a partir de um texto simples com Python.
3. Organização do projeto em VS Code e controle de versão via Git/GitHub.
4. Registro de uma breve demonstração em vídeo (até 3 minutos) comprovando que tudo funciona.

---

## Pré-requisitos

* **Sistema Operacional**: Windows, macOS ou Linux
* **Python**: versão 3.8 ou superior
* **Git**: para controle de versão
* **VS Code**: editor de código (recomendado)
* **Ollama**: instalado localmente (veja [Configuração do Ollama](#configuração-do-ollama))

---

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Hagliberto/ollama-embeddings-atividade.git
   cd ollama-embeddings-atividade
   ```

2. Crie e ative um ambiente virtual:

   * **Windows (PowerShell)**:

     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD)**:

     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   * **macOS/Linux**:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuração do Ollama

1. **Instalar o Ollama**:

   * **Linux/macOS**:

     ```bash
     curl -fsSL https://ollama.com/install.sh | sh
     ```
   * **Windows**:

     * Baixe o instalador em [https://ollama.com/download](https://ollama.com/download) e siga as instruções.

2. **Verificar a instalação**:

   ```bash
   ollama list
   ```

3. **Baixar o modelo de embeddings**:

   ```bash
   ollama pull llama3.2
   ```

---

## Uso

### Executar o servidor Ollama

Em um terminal (com o ambiente virtual ativo):

```bash
ollama serve
```

Deixe esta janela aberta para atender as requisições de embeddings.

### Gerar Embeddings via Script Python

Abra outro terminal (ou use o mesmo com `Ctrl+Shift+'`) e execute:

```bash
python create_embeddings.py
```

Isso irá conectar ao Ollama local e gerar o vetor de embeddings para o texto de exemplo.

### Exemplo de Saída

```
Vetor de embeddings (tamanho: 1536):
Primeiros 5 valores: [-0.0234, 0.1123, ...]
```

---

## Notebook Jupyter (Opcional)

Caso prefira, abra o arquivo `create_embeddings.ipynb` no VS Code ou Jupyter:

1. Inicie o Jupyter:

   ```bash
   jupyter notebook
   ```
2. Navegue até `create_embeddings.ipynb` e execute a célula com o mesmo código do script.

---

## Estrutura do Repositório

```plaintext
ollama-embeddings-atividade/
├── create_embeddings.py       # Script principal em Python
├── create_embeddings.ipynb    # Notebook com código equivalente
├── requirements.txt           # Dependências Python
├── .gitignore                 # Arquivos e pastas ignorados pelo Git
└── README.md                  # Este arquivo de documentação
```

---

## Vídeo de Demonstração

Grave um vídeo de até 3 minutos mostrando:

1. Inicialização do servidor Ollama (`ollama serve`).
2. Pull do modelo (`ollama pull llama3.2`).
3. Execução do script/notebook e visualização dos embeddings.

> **Link do vídeo:** [Vídeo de apresentação](https://www.loom.com/share/ffaf4d2d3c51470bb8003060253150d1?sid=f27d8b0a-b150-4413-9f8e-230ef7585087)

---

## Solução de Problemas

* **Erro: `ollama: command not found`**

  * Verifique se o Ollama está instalado e se o PATH inclui o binário.

* **Ambiente virtual não ativa**

  * Confira se você está no diretório correto e se o `.venv` foi criado com sucesso.

* **Problemas ao gerar embeddings**

  * Assegure-se de que o servidor Ollama está rodando (`ollama serve`).
  * Confirme o nome do modelo baixado (`ollama list`).

---

