from mcp.server.fastmcp import FastMCP
from typing import Any
import mcp
import logging
import httpx
import chromadb

# Initialize FastMCP server
mcp = FastMCP("icd-classifier")

chroma_client = chromadb.PersistentClient('./icdc')
icdc = chroma_client.get_or_create_collection(name="icdc")

NUM_RESULTS=5

def formatResult(document: str) -> str:
    """Returns a formatted result for the agent regarding a medical ICD classification
    """
    return f"""
<li>
{document}
</li>
"""

@mcp.tool()
def getCodes(description: str) -> str:
    """Get ICD-10 codes and descriptions pertaining to a medical description

    Args:
        description: medical notes regarding a patient's condition
    """
    global icdc, NUM_RESULTS

    results = icdc.query(
        # Should test with splitting the notes up too
        query_texts=[description],
        n_results=NUM_RESULTS
    )
    res = ''
    # logging.info(f"Found {len(results['ids'])} result(s): {results}")
    for i in range(len(results['ids'][0])):
        # Why is the 'ids', 'documents', etc, an array of arrays? Because the query(...) can take in multiple queries
        code, document = results['ids'][0][i], results['documents'][0][i]
        # res += formatResult(code, document)
        res += formatResult(document)
    return res

def test():
    print(getCodes("feeling sick, maybe meningitus"))

def main():
    logging.info("Hello from icd-classifier!")
    mcp.run(transport="stdio")
    #test()
    logging.info("Goodbye from icd-classifier!")


if __name__ == "__main__":
    main()
