from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from common.knowledge_base import find_relevant_content
from common.prompts import build_rag_prompt

app = FastAPI(title="Cblue AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    conversation_id: str = None

def get_response(message: str) -> str:
    """Generate response using knowledge base"""
    context = find_relevant_content(message)
    
    # Detect language
    is_thai = any(ord(c) >= 0x0E00 and ord(c) <= 0x0E7F for c in message)
    
    if context and "Cblue Thailand provides" not in context:
        # Found specific content - return it
        return context
    else:
        # Fallback response - shorter with only email
        if is_thai:
            return """ขออภัย ไม่พบข้อมูลที่ตรงกับคำถามของคุณ

กรุณาติดต่อเราที่: cblue.thailand@gmail.com"""
        else:
            return """Sorry, I couldn't find information matching your question.

Please contact us at: cblue.thailand@gmail.com"""

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = get_response(req.message)
        return {'message': response}
    except Exception as e:
        print(f"Error: {e}")
        return {'message': 'ขออภัย เกิดข้อผิดพลาด กรุณาติดต่อ: cblue.thailand@gmail.com'}

@app.get("/health")
async def health():
    return {'status': 'ok', 'model_available': False}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8010)
