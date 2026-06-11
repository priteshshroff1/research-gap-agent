
from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def analysis_agent(state: AgentState) -> AgentState:
    """
    Analysis Agent

    Performs literature analysis on the
    highest ranked research papers.
    """

    papers = state.get("papers", [])

    literature = ""

    # Only analyze top 5 papers
    papers = papers[:5]

    for i, paper in enumerate(papers, start=1):

        # Limit abstract size to reduce token usage
        abstract = paper.get("abstract", "") or ""

        if len(abstract) > 300:
            abstract = abstract[:300] + "..."

        literature += f"""

Paper {i}

Title:
{paper.get("title", "")}

Authors:
{", ".join(paper.get("authors", []))}

Year:
{paper.get("year", "")}

Venue:
{paper.get("venue", "")}

Citation Count:
{paper.get("citations", 0)}

Impact Score:
{round(paper.get("impact_score", 0), 3)}

Abstract:
{abstract}

----------------------------------------

"""

    prompt = load_prompt(
        "analysis",
        topic=state["topic"],
        literature=literature
    )

    response = generate(prompt)

    state["analysis"] = response

    return state

