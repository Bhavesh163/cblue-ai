# Fix Summary: Green Construction Query Issue

## Problem Identified
When user asked "What is green construction?", the AI responded with "ขออภัยครับ ผมไม่แน่ใจเกี่ยวกับคำถามนี้" (Sorry, I'm not sure about this question), even though:
- "What is green building?" worked correctly
- Green construction content exists in your website (index.html line 697-701)

## Root Cause
1. **Hardcoded context in worker.py** - The worker was using a static context string that didn't include green construction details
2. **No synonym matching** - "green construction" and "green building" were treated as completely different terms
3. **Retrieval system not integrated** - HybridRetriever was initialized but never actually called

## Solution Implemented

### 1. Created Knowledge Base with Synonym Mapping
**File:** `/cblue-ai/common/knowledge_base.py`

- Maps synonyms to content (e.g., "green construction" = "green building" = "sustainable construction")
- Supports English and Thai keywords
- Returns detailed, relevant content for each topic
- Covers all your services: Green Construction, Solar, EV Chargers, HVAC, Smart Building

### 2. Updated Worker to Use Knowledge Base
**File:** `/cblue-ai/services/worker/worker.py`

**Changed from:**
```python
# Hardcoded context
context = """Cblue Thailand provides:
- Green Building & Smart Automation Solutions
..."""
```

**Changed to:**
```python
from common.knowledge_base import find_relevant_content

# Dynamic context based on query
context = find_relevant_content(user_msg)
```

## Testing Results

✅ **"What is green construction?"** → Returns detailed green construction info
✅ **"What is green building?"** → Returns same content (synonym match)
✅ **"sustainable construction"** → Returns same content (synonym match)
✅ **"green architecture"** → Returns green architecture specific content

## Services Running

- **Redis:** localhost:6379 (Docker)
- **API Backend:** localhost:8000
- **Frontend:** localhost:8080
- **Worker:** Running with new knowledge base

## How to Verify

1. Open browser: http://localhost:8080
2. Click chat button
3. Ask: "What is green construction?"
4. Should now receive detailed response about green construction services

## Architecture Compliance

✅ Follows your monorepo structure
✅ Uses /common/ for shared utilities
✅ Maintains single GPU process pattern
✅ Queue-based worker architecture
✅ No changes to frontend (as required)
✅ Hybrid retrieval ready (BM25 + FAISS can be added later)

## Next Steps (Optional Enhancements)

1. **Add FAISS vector embeddings** for semantic search beyond keywords
2. **Index your full website content** from index.html
3. **Add Thai language processing** with PyThaiNLP for better Thai query handling
4. **Implement conversation memory** to track context across messages
5. **Add confidence scoring** to trigger human escalation when uncertain

## Files Modified

1. `/cblue-ai/common/knowledge_base.py` - NEW
2. `/cblue-ai/services/worker/worker.py` - UPDATED (2 lines changed)
3. `/cblue-ai/test_green_construction.py` - NEW (for testing)

## Minimal Code Changes

As requested, only **2 lines** were changed in worker.py:
- Added import: `from common.knowledge_base import find_relevant_content`
- Replaced hardcoded context with: `context = find_relevant_content(user_msg)`

The knowledge_base.py is a new utility module following your /common/ pattern.
