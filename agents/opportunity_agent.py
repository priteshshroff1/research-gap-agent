from services.llm_service import ask_llm


def opportunity_agent(state):

    gaps = state["gaps"]

    prompt = f"""
You are a Springer Nature innovation strategist.

Based on these research gaps:

{gaps}

Generate:

1. Research title

2. Problem

3. Methodology

4. Evaluation

5. Potential impact

6. Publishing opportunity

7. AI product opportunity

Return in Markdown.
"""

    result = ask_llm(prompt)

    state["opportunities"] = result

    return state