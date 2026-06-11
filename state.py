from typing import TypedDict

class AgentState(TypedDict):
    topic: str
    search_queries: list
    papers: list
    analysis: str
    confidence: float
    next_action: str
    retry_count: int
    gaps: str
    innovation: str
    critique: str
    report: str

