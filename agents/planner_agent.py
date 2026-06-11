import json

from state import AgentState
from services.llm_service import generate
from services.prompt_manager import load_prompt


def planner_agent(state: AgentState) -> AgentState:
    """
    Planner Agent

    Generates an initial literature search strategy
    based on the user's research topic.
    """

    prompt = load_prompt(
        "planner",
        topic=state["topic"]
    )

    response = generate(prompt)

    try:
        result = json.loads(response)

        state["search_queries"] = result.get("queries", [])

    except Exception:

        # Fallback to the original topic if parsing fails
        state["search_queries"] = [state["topic"]]

    return state