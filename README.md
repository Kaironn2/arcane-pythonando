# 🤖 RAG-Pipeline – Context Builder + Chat + WhatsApp

## English

### 📟 Short Description

System for building a full RAG (Retrieval-Augmented Generation) pipeline using web scraping, PDF/text ingestion, and FAISS vector storage. Includes a real-time chat with source display and optional WhatsApp integration via EvolutionAPI.

### 📄 Long Description

RAG-Pipeline is a tool to ingest and process contextual data from various sources and serve it in a context-aware chat interface using a Retrieval-Augmented Generation (RAG) approach.

The system works with different types of inputs:

- Performs **web scraping** using BeautifulSoup to extract content from websites.
- Processes **PDFs or raw text** provided by the user.
- Generates **embeddings** for all content and stores them using **FAISS**.
- Supports **RAG-based Q&A**, where a language model answers based on retrieved context.
- Answers are shown in a **chat interface with source links**.
- Optional integration with **WhatsApp** via **EvolutionAPI**, allowing users to ask questions directly from WhatsApp.

### 🔄 Process Flow

1. User inputs:
   - A target website URL for scraping.
   - A PDF or text.
2. The system extracts and cleans the text.
3. Embeddings are generated using OpenAI or another LLM provider.
4. All embeddings are stored in a FAISS vector store.
5. When the user asks a question:
   - The system searches the most relevant chunks in FAISS.
   - Constructs a prompt and calls the LLM to generate an answer.
   - Displays the streamed answer with source references.
6. If WhatsApp integration is active:
   - Messages received via EvolutionAPI are processed the same way.
   - Replies are sent back to the user on WhatsApp with optional links.

### 🧰 Tech Stack

- Python
- BeautifulSoup4
- Langchain
- FAISS
- OpenAI (embeddings & LLM)
- Django (chat backend)
- EvolutionAPI (for WhatsApp)
- DjangoQ

---

## Português

### 📟 Descrição Curta

Sistema para montar uma pipeline completa de RAG (Retrieval-Augmented Generation) com scraping, ingestão de PDFs/texto e armazenamento em vetor FAISS. Inclui chat em tempo real com exibição de fontes e integração opcional com WhatsApp via EvolutionAPI.

### 📄 Descrição Longa

O RAG-Pipeline permite construir uma base de conhecimento contextual com dados extraídos de diferentes fontes e utilizá-la em uma interface de chat inteligente usando o conceito de RAG (Geração Aumentada por Recuperação).

Este sistema suporta múltiplas formas de entrada:

- Faz **web scraping** com BeautifulSoup para extrair conteúdo de sites.
- Processa **PDFs ou textos brutos** fornecidos pelo usuário.
- Gera **embeddings** de todos os conteúdos e armazena com **FAISS**.
- Utiliza **RAG** para responder perguntas com base no conteúdo extraído.
- As respostas são exibidas em um **chat com links para as fontes utilizadas**.
- Integração opcional com **WhatsApp** via **EvolutionAPI**, permitindo perguntas diretamente pelo app.

### 🔄 Fluxo do Processo

1. O usuário fornece:
   - Um link de site para scraping.
   - Um PDF ou texto.
2. O sistema extrai e limpa os textos.
3. Gera embeddings com OpenAI ou outro provedor de LLM.
4. Armazena tudo no banco vetorial FAISS.
5. Ao fazer uma pergunta:
   - Busca os trechos mais relevantes no FAISS.
   - Monta o prompt e chama o modelo de linguagem para gerar a resposta.
   - Exibe a resposta em streaming com referências das fontes.
6. Se a integração com WhatsApp estiver ativa:
   - As mensagens recebidas via EvolutionAPI são processadas da mesma forma.
   - As respostas são enviadas de volta com ou sem links de referência.

### 🧰 Tech Stack

- Python
- BeautifulSoup4
- PyMuPDF / PDFPlumber
- FAISS
- OpenAI (embeddings e LLM)
- Django (backend do chat)
- EvolutionAPI (para WhatsApp)
- DjangoQ
