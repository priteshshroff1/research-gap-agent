from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def report_agent(state: AgentState) -> AgentState:
    """
    Report Agent

    Combines the outputs of all previous agents
    into a final research report.
    """

    prompt = load_prompt(
        "report",
        topic=state["topic"],
        analysis=state["analysis"],
        gaps=state["gaps"],
        innovation=state["innovation"],
        critique=state["critique"]
    )

    response = generate(prompt)

    state["report"] = response

    return state