from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def analysis_agent(state: AgentState) -> AgentState:
    """
    Analysis Agent

    Analyzes the retrieved research papers and
    generates a structured literature synthesis.
    """

    papers = state.get("papers", [])

    if not papers:
        state["analysis"] = "No papers available for analysis."
        return state

    paper_text = ""

    for index, paper in enumerate(papers, start=1):

        paper_text += (
            f"{index}.\n"
            f"Title: {paper.get('title', 'N/A')}\n"
            f"Year: {paper.get('year', 'N/A')}\n"
            f"Citations: {paper.get('citations', 0)}\n"
            f"Abstract: {paper.get('abstract', 'Not Available')}\n\n"
        )

    prompt = load_prompt(
        "analysis",
        topic=state["topic"],
        papers=paper_text
    )

    response = generate(prompt)

    state["analysis"] = response

    return state