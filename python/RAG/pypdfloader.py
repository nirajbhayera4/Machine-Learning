from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("python/RAG/rag_guide_20_pages.pdf")
docs=loader.load()
print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
print(len(docs))

