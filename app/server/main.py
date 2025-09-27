from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schemas.models import AskRequest
from app.chains.rag_chain import ask
from app.policies.policy_store import POLICY_PACK_VERSION

app = FastAPI(title="Audit-Ready RAG")

@app.get("/healthz")
def health():
    return {"status": "ok", "policy_pack_version": POLICY_PACK_VERSION}

@app.post("/ask")
def ask_route(req: AskRequest):
    return JSONResponse(ask(question=req.question, jurisdiction=req.jurisdiction))

if __name__ == "__main__":
    # <-- Debug-friendly: same process as PyCharm
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
