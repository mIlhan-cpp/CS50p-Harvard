import pytest
import numpy as np
from project import chunk, search_database

# --- Mock Data for Testing ---
# Simple data samples mimicking what your extract() function outputs
MOCK_EXTRACTED_DATA = [
    {
        "content": "abcdefghij",  # 10 characters long
        "metadata": {"source": "doc1.pdf", "page": 1}
    }
]

# Simple data samples mimicking what your encode() function outputs (with mock 2D embeddings)
MOCK_EMBEDDED_CHUNKS = [
    {
        "content": "This is a fact about apples.",
        "metadata": {"source": "fruit.pdf", "page": 1, "chunk_id": 1},
        "embedding": [1.0, 0.0]  # Pointing straight right
    },
    {
        "content": "This is a fact about airplanes.",
        "metadata": {"source": "planes.pdf", "page": 2, "chunk_id": 1},
        "embedding": [0.0, 1.0]  # Pointing straight up
    }
]

# Dummy model class to bypass loading the actual SentenceTransformer model in tests
class FakeTransformerModel:
    def encode(self, text):
        # If the user searches for apple, give a vector matching the apple chunk
        if "apple" in text.lower():
            return np.array([1.0, 0.0])
        return np.array([0.0, 1.0])


def test_chunk_slicing_logic():
    """
    Tests that chunk character slicing math and overlaps calculate correctly.
    """
    # chunk_size=6, overlap=2 means step = 4
    # "abcdefghij" is 10 characters long
    # First chunk: index 0 to 6 -> "abcdef"
    # Second chunk: index 4 to 10 -> "efghij"
    # Third (trailing) chunk: index 8 onward -> "ij"
    result = chunk(MOCK_EXTRACTED_DATA, chunk_size=6, overlap=2)
    
    assert len(result) == 3
    assert result[0]["content"] == "abcdef"
    assert result[1]["content"] == "efghij"
    assert result[2]["content"] == "ij"


def test_chunk_metadata_pass_through():
    """
    Verifies that page numbers, file sources, and chunk IDs step up correctly.
    """
    result = chunk(MOCK_EXTRACTED_DATA, chunk_size=6, overlap=2)
    
    # Check that metadata attributes from the parent document survived
    assert result[0]["metadata"]["source"] == "doc1.pdf"
    assert result[0]["metadata"]["page"] == 1
    
    # Check that chunk numbers incremented correctly
    assert result[0]["metadata"]["chunk_id"] == 1
    assert result[1]["metadata"]["chunk_id"] == 2


def test_search_database_finds_best_match():
    """
    Tests the cosine similarity vector matching system inside search_database.
    """
    fake_model = FakeTransformerModel()
    
    # Query matching the vector direction of our mock apple entry
    best_match, score = search_database("Tell me about apples", MOCK_EMBEDDED_CHUNKS, fake_model)
    
    # The search engine should pick the first chunk dictionary
    assert best_match["metadata"]["source"] == "fruit.pdf"
    
    # Perfect alignment with the fake vector direction should yield a cosine score close to 1.0
    assert score == pytest.approx(1.0, rel=1e-3)
