#!/usr/bin/env python3
"""Test green construction query"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from common.knowledge_base import find_relevant_content

# Test queries
queries = [
    "What is green construction?",
    "What is green building?",
    "Tell me about sustainable construction",
    "green architecture"
]

print("=" * 60)
print("Testing Knowledge Base Synonym Matching")
print("=" * 60)

for query in queries:
    print(f"\nQuery: {query}")
    print("-" * 60)
    content = find_relevant_content(query)
    print(content[:200] + "..." if len(content) > 200 else content)
    print()
