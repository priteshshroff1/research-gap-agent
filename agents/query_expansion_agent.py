import json

from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def query_expansion_agent(state: AgentState) -> AgentState:
    """
    Query Expansion Agent

    Expands the user's research topic into
    multiple semantically related search queries.
    """

    prompt = load_prompt(
        "query_expansion",
        topic=state["topic"]
    )

    response = generate(prompt)

    try:
        result = json.loads(response)

        expanded_queries = result.get("queries", [])

        # Remove duplicates while preserving order
        unique_queries = []

        seen = set()

        for query in expanded_queries:

            query = query.strip()

            if query and query not in seen:

                seen.add(query)

                unique_queries.append(query)

        # Always include the original topic
        if state["topic"] not in seen:
            unique_queries.insert(0, state["topic"])

        state["search_queries"] = unique_queries

    except Exception:

        # Fallback
        state["search_queries"] = [
            state["topic"]
        ]

    return state