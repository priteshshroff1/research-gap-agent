from agents.search_agent import search_agent
from agents.analysis_agent import analysis_agent
from agents.gap_agent import gap_agent

state = {
    "topic":"Agentic AI"
}

state = search_agent(state)

state = analysis_agent(state)

state = gap_agent(state)

print(state["gaps"])