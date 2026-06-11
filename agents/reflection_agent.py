import json

from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def reflection_agent(state: AgentState) -> AgentState:
    """
    Reflection Agent

    Evaluates whether the current literature
    is sufficient for research gap discovery.
    """

    prompt = load_prompt(
        "reflection",
        topic=state["topic"],
        analysis=state["analysis"]
    )

    response = generate(prompt)

    try:
        result = json.loads(response)

        state["confidence"] = result.get("confidence", 0.0)
        state["next_action"] = result.get("decision", "CONTINUE")

    except Exception:

        # Fallback values
        state["confidence"] = 0.5
        state["next_action"] = "CONTINUE"

    return state