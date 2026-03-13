import json
from pathlib import Path

def create_sample_json_file(tmp_path):
    """
    Create a temporary JSONL file for testing pipelines.
    """

    file_path = tmp_path / "sample.jsonl"

    data = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

    with open(file_path, "w") as f:
        for row in data:
            f.write(json.dumps(row) + "\n")

    return file_path
