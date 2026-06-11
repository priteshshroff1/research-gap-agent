from state import AgentState
from services.openalex_service import search_multiple


def search_agent(state: AgentState) -> AgentState:
    """
    Search Agent

    Retrieves research papers from OpenAlex
    using the expanded search queries.
    """

    queries = state.get("search_queries", [])

    if not queries:
        queries = [state["topic"]]

    papers = search_multiple(
        queries=queries,
        limit=5
    )

    state["papers"] = papers

    return state