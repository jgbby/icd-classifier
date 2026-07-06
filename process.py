import chromadb
import pandas as pd
import logging
import time

'''
chroma_client = chromadb.Client()
# chroma_client.get_or_create_collection(...)
# icdc = chroma_client.create_collection(name="icts")
#icdc.upsert(...)
print(results)
'''

chroma_client = chromadb.PersistentClient(path="./icdc")
icdc = chroma_client.get_or_create_collection(name="icdc")

ids = []
documents = []
metadatas = []

def addRow(row):
    '''
    '''
    global ids, documents, metadatas
    ids.append(row.CODE)
    documents.append(f"""
<code>{row.CODE}</code> 
<short_desc>{row._2}</short_desc>
<long_desc>{row._3}</long_desc>
"""
    )
    metadatas.append({
        "Code": row.CODE,
        "NF": True if row._4 == "Y" else False 
    })
    
def batch(size):
    global ids, documents, metadatas
    for i in range(0, len(ids), size):
        yield ids[i:i+size], documents[i:i+size], metadatas[i:i+size] 


def process(filename):
    global icdc, ids, documents, metadatas
    df = pd.read_excel(filename, sheet_name="Valid ICD10 FY2026 & NF Exclude")
    '''
    DataFrame.itertuples() is a built-in Pandas method used to iterate over DataFrame rows as named tuples. 
    It is widely preferred over iterrows() because it is significantly faster and more memory-efficient
    '''
    desired_rows = df.shape[0]
    batch_size = 5000

    rows = df.head(desired_rows)
    tuples = rows.itertuples(index=True)
    count = 1
    num_rows = rows.shape[0]
    print(f"Processing {num_rows}) rows to ids, documents, and metadata")
    for row in tuples:
        print(f"{count}/{num_rows}")
        addRow(row)
        count += 1

    if len(ids) == 0:
        print("No ids found")
        return

    print(f"Adding {num_rows} rows to ChromaDB")

    num_batches = 1
    for gids, gdocuments, gmetadatas in batch(batch_size):
        print(f"[*] Batch {num_batches * batch_size}/{num_rows}")
        start = time.time()
        icdc.add(ids=gids, documents=gdocuments, metadatas=gmetadatas)
        num_batches += 1
        end = time.time()
        print(f"Took {end - start:.2f} seconds")

    print(f"Finished adding {num_rows} rows")

def test():
    global icdc

    results = icdc.query(
        query_texts=["aching fever, potentially meningitis?"],
        n_results=1
    )
    print(results)


def main():
    filename = "./icd10-oct25.xlsx"
    print(f"Processing {filename}")
    process(filename)

if __name__ == "__main__":
    main()
