from state import AgentState
from config import TOP_K_PAPERS


def ranking_agent(state: AgentState) -> AgentState:
    """
    Ranking Agent

    Ranks retrieved papers based on citation count
    and retains the top K papers for downstream analysis.
    """

    papers = state.get("papers", [])

    if not papers:
        return state

    # Sort papers by citation count (descending)
    ranked_papers = sorted(
        papers,
        key=lambda paper: paper.get("citations", 0),
        reverse=True
    )

    # Keep only the top K papers
    state["papers"] = ranked_papers[:TOP_K_PAPERS]

    return state