#RAG pipeline
PDF Knowledge Base – Semantic Search over Local PDFs

#### Video Demo: https://youtu.be/PPedsEpLPlk

#### Description:

PDF Knowledge Base is my CS50P final project. It is a question-answering application built with Python that allows users to search through multiple PDF documents by asking questions in human language without paid AI models.

I came up with this idea because searching through large PDF documents manually can be time-consuming, especially when the information is spread across multiple files and paying for APIs isn't always feasible.

The project uses semantic search, which means it compares the meaning of the user’s question with the content extracted from PDF documents. It uses sentence embeddings and cosine similarity to identify the most relevant passage and displays the matching text along with the PDF filename and page number.

The application is organized into four main functions in project.py.

1. Extract (extract)
This function reads all PDF files from the ./pdfs/ directory using PyMuPDF (fitz). It extracts text from each page and skips pages that contain no readable text.
For every extracted page, the program stores the text along with its source filename and page number. This makes it possible to identify where the search results originally came from.

2. Chunk (chunk)
After extracting the text, the program divides it into smaller sections called chunks.
The default chunk size is 300 characters, with an overlap of 50 characters. I used overlapping chunks to avoid losing context when information falls near the boundary between two sections.
Each chunk also retains its original PDF filename and page number and is assigned a unique chunk_id.

3. Encode (encode)
This function converts each text chunk into a numerical representation called an embedding.
For this, I used the all-MiniLM-L6-v2 model from Sentence Transformers. The model generates 384-dimensional vectors that represent the meaning of the text.
These embeddings allow the application to find relevant passages even when the words used in a question are different from those in the original document.

4. Search (search_database)
When the user enters a question, the application converts it into an embedding using the same model.
It then calculates cosine similarity between the question embedding and the stored embeddings of all document chunks. The chunk with the highest similarity score is returned as the best match.
The result includes:
- The matching text.
- Similarity score.
- Original PDF filename.
- Page number.

The main() function brings everything together. It loads the PDF documents, runs the extraction, chunks the extracted text, and encodes chunks of texts, and starts an interactive command-line interface for question-answering.

Users can continue asking questions until they type exit.

Files

- project.py: Contains the main application and implements PDF extraction, text chunking, embedding generation, and semantic search.
- test_project.py: Contains unit tests for the chunking and search functionality.
- pdfs/: Directory where users place their PDF documents.

How to Run

First, install the required libraries:

pip install pymupdf sentence-transformers numpy pytest

Place your PDF files inside the pdfs directory.

Run the application:
python project.py

The application will process the available PDFs and display the following prompt:
Ask a question about your PDFs (or type 'exit'):
Enter a question related to the documents. The application will return the most relevant passage and its source information.
