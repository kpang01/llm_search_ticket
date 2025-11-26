from fastapi import APIRouter, HTTPException, Query
from src.ETL.ticket_repo import TicketRepository, Ticket
from src.db.db_config import DATABASE_CONFIG
from src.utils.embedding_utils import get_embedding
from typing import List, Optional

router = APIRouter()
repo = TicketRepository(DATABASE_CONFIG)

@router.get("/tickets/", response_model=List[dict])
def get_tickets():
    tickets = repo.get_all_()
    return [{"metadata": t.metadata, "description": t.description} for t in tickets]

@router.get("/tickets/filter/", response_model=List[dict])
def filter_tickets(priority: Optional[str] = None, ticket_type: Optional[str] = None, channel: Optional[str] = None):
    filters = {}
    if priority:
        filters["priority"] = priority
    if ticket_type:
        filters["ticket_type"] = ticket_type
    if channel:
        filters["channel"] = channel
    tickets = repo.filter_by(**filters)
    return [{"metadata": t.metadata, "description": t.description} for t in tickets]

@router.get("/tickets/custom/", response_model=List[dict])
def custom_tickets(fields: List[str] = Query(...), priority: Optional[str] = None, ticket_type: Optional[str] = None):
    filters = {}
    if priority:
        filters["priority"] = priority
    if ticket_type:
        filters["ticket_type"] = ticket_type
    tickets = repo.fetch_custom(fields, filters)
    return [{"metadata": t.metadata, "description": t.description} for t in tickets]

@router.post("/tickets/semantic_search/", response_model=List[dict])
def semantic_search(query: str, top_k: int = 5):
    tickets = repo.get_all_()
    query_embedding = get_embedding(query)
    # Compute similarity and rank tickets
    def cosine_similarity(a, b):
        from numpy import dot
        from numpy.linalg import norm
        return dot(a, b) / (norm(a) * norm(b))
    results = []
    for t in tickets:
        emb = get_embedding(t.description)
        sim = cosine_similarity(query_embedding, emb)
        results.append((sim, t))
    results.sort(key=lambda x: x[0], reverse=True)
    top5 = [r[1] for r in results[:top_k]]
    return [{"metadata": t.metadata, "description": t.description} for t in top5]