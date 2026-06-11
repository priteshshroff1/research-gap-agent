from agents.search_agent import search_agent
from agents.analysis_agent import analysis_agent

state = {
    "topic":"Agentic AI"
}

state = search_agent(state)

state = analysis_agent(state)

print(state["analysis"])