from datetime import datetime

from state import AgentState
from config import TOP_K_PAPERS


def recency_score(year):

    current = datetime.now().year

    age = current - year

    if age <= 1:
        return 1

    elif age <= 2:
        return 0.9

    elif age <= 3:
        return 0.8

    elif age <= 5:
        return 0.7

    return 0.5


def ranking_agent(state: AgentState):

    papers = state.get("papers", [])

    if not papers:
        return state

    max_citation = max(
        p.get("citations", 0)
        for p in papers
    )

    trend = {}

    total_citations = 0

    for paper in papers:

        citations = paper.get(
            "citations",
            0
        )

        year = paper.get(
            "year",
            datetime.now().year
        )

        relevance = paper.get(
            "score",
            1
        )

        citation_score = citations / max(
            max_citation,
            1
        )

        recent_score = recency_score(year)

        impact_score = (
            0.6 * relevance
            + 0.25 * citation_score
            + 0.15 * recent_score
        )

        paper["impact_score"] = impact_score

        total_citations += citations

        trend[year] = trend.get(year, 0) + 1

    papers = sorted(
        papers,
        key=lambda x: x["impact_score"],
        reverse=True
    )

    state["papers"] = papers[:TOP_K_PAPERS]

    state["research_landscape"] = {

        "total_papers": len(papers),

        "total_citations": total_citations,

        "average_citations": round(
            total_citations / len(papers),
            2
        ),

        "highest_citations": max_citation,

        "publication_trend": trend,

        "top_papers": papers[:5]

    }

    return state