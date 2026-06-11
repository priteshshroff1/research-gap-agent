from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def gap_agent(state: AgentState) -> AgentState:
    """
    Gap Agent

    Identifies research gaps from the literature analysis.
    """

    prompt = load_prompt(
        "gap",
        topic=state["topic"],
        analysis=state["analysis"]
    )

    response = generate(prompt)

    state["gaps"] = response

    return state