import fitz
from pathlib import Path
import sys
from sentence_transformers import SentenceTransformer
import numpy as np

folder=Path("./pdfs/")


def extract(pdf_file):
    documents=[]
    for pdf in pdf_file:
        docs=fitz.open(pdf)
        print(f"\nProcessing: {pdf.name}")
        for page_num,page in enumerate(docs):
            text=page.get_text()
            if not text.strip():
                continue
            documents.append({
            "content": text,
            "metadata": {
                "source": pdf.name,
                "page": page_num + 1
            }
        })

        docs.close()
    if documents:
        print("\n200 letters", documents[0]["content"][:200])
        print("\nTotal extracted pages:", {len(documents)})
    else:
        sys.exit("\nWarning: No text extracted. check PDF")
        
    return documents

def chunk(data,chunk_size=300,overlap=50):
    step=chunk_size-overlap
    chunks=[]
    for docs in data:
        text = docs["content"]
        metadata = docs["metadata"]
        chunk_number=0
        for i in range(0,len(text),step):
            chunk=text[i:i+chunk_size].strip()
            chunk_number+=1

            chunk_metadata={
                **metadata,
                'chunk_id':chunk_number
            }
            chunks.append({
                'content':chunk,
                'metadata':chunk_metadata
            })
    return chunks

def encode(chunk):
    if not chunk:
        sys.exit('No chunks found')
        
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embed=[item['content'] for item in chunk] #lambda function
    embedded=model.encode(embed,show_progress_bar=True)
    for index, embedding in enumerate(embedded):
        chunk[index]['embedding'] = embedding.tolist()

    return chunk

def search_database(query: str, chunks_with_vectors: list, model: SentenceTransformer):
    query_encode=model.encode(query)
    best_chunk=[]
    max_similarity=-1
    for chunk in chunks_with_vectors:
        a = np.array(chunk['embedding'])
        b = np.array(query_encode)

        similarity=np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))
        if similarity>max_similarity:
            max_similarity=similarity
            best_chunk=chunk

    return best_chunk, max_similarity



def main():
    pdf_file=list(folder.glob('*.pdf'))
    if not pdf_file:
        print('No file exists')
        return
    raw_docs = extract(pdf_file)
    chunked=chunk(raw_docs)
    embedded=encode(chunked)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    if embedded:
        sample=embedded[0]['embedding']
        print(sample)
        print("Pipeline execution finished successfully.")

    print("\nPDF Knowledge Base Completed")
    while True:
        user_query = input("\nAsk a question about your PDFs (or type 'exit'): ").strip()
        if user_query.lower() == 'exit':
            break
        match,score=search_database(user_query,embedded,model)
        print(f"\n[Match Score: {score:.2f}] Found in {match['metadata']['source']} (Page {match['metadata']['page']}):")
        print(f"Content: \"{match['content']}\"")

if __name__ == "__main__":
    main()