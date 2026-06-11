from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def innovation_agent(state: AgentState) -> AgentState:
    """
    Innovation Agent

    Generates innovative research ideas and
    future opportunities from the identified
    research gaps.
    """

    prompt = load_prompt(
        "innovation",
        topic=state["topic"],
        gaps=state["gaps"]
    )

    response = generate(prompt)

    state["innovation"] = response

    return state