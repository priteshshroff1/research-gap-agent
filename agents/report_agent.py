
from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def truncate(text, limit):

    if text is None:
        return ""

    text = str(text)

    if len(text) <= limit:
        return text

    return text[:limit] + "..."


def report_agent(state: AgentState) -> AgentState:

    landscape = state.get(
        "research_landscape",
        {}
    )

    summary = f"""
Research Landscape

Total Papers:
{landscape.get('total_papers',0)}

Average Citations:
{landscape.get('average_citations',0)}

Highest Citations:
{landscape.get('highest_citations',0)}

Publication Trend:
"""

    trend = landscape.get(
        "publication_trend",
        {}
    )

    for year, count in sorted(
        trend.items()
    ):

        summary += f"\n{year}: {count}"

    summary += "\n\nTop Papers:\n"

    top_papers = landscape.get(
        "top_papers",
        []
    )

    for paper in top_papers:

        summary += (
            f"\n• "
            f"{paper.get('title','Unknown')} "
            f"({paper.get('year','')}) "
            f"- Citations: "
            f"{paper.get('citations',0)}"
        )

    # -----------------------------
    # Reduce Prompt Size
    # -----------------------------

    analysis = truncate(
        state.get("analysis"),
        1000
    )

    gaps = truncate(
        state.get("gaps"),
        700
    )

    innovation = truncate(
        state.get("innovation"),
        700
    )

    critique = truncate(
        state.get("critique"),
        500
    )

    research_landscape = truncate(
        summary,
        400
    )

    prompt = load_prompt(

        "report",

        topic=state["topic"],

        research_landscape=research_landscape,

        analysis=analysis,

        gaps=gaps,

        innovation=innovation,

        critique=critique

    )

    response = generate(prompt)

    state["report"] = response

    return state

