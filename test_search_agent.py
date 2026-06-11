from agents.search_agent import search_agent

state = {
    "topic":"Agentic AI"
}

state = search_agent(state)

print(len(state["papers"]))

print(state["papers"][1]["display_name"])