# Necessary Context
During an interview with EarnestRCM, I discussed with Spencer Lorin about how they implement ICT code classification
from doctor's notes. They supposedly achieved better results than a Deloitte research paper, MedCoder GenAI, with a simple
MCP solution using BM25 Similarity score. They never took the time to attempt this with an embedding model however, I'd like to
see how this works and try my own implementation.

# Functional Requirements
- [] Build an AI model capable of taking doctor's notes from a patient visit, and translate it into ICT-10 codes. 
- [] Build a ChromaDB embedding of ICT-10 codes to their respective descriptions
- [] Build an MCP server capable of indexing into ChromaDB

# Stretch Goals
- [] Build a web interface for uploading patient notes
