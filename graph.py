from langgraph.graph import StateGraph, END

from state import AgentState

from agents.planner_agent import planner_agent
from agents.query_expansion_agent import query_expansion_agent
from agents.search_agent import search_agent
from agents.ranking_agent import ranking_agent
from agents.analysis_agent import analysis_agent
from agents.reflection_agent import reflection_agent
from agents.gap_agent import gap_agent
from agents.innovation_agent import innovation_agent
from agents.critic_agent import critic_agent
from agents.report_agent import report_agent


def reflection_router(state: AgentState):
   """
Allow at most one additional search
before continuing the workflow.
"""

   if (
       state["next_action"] == "SEARCH_MORE"
       and state["retry_count"] < 1
   ):
       state["retry_count"] += 1
       return "search"

   return "gap"

workflow = StateGraph(AgentState)

# ------------------------
# Add Nodes
# ------------------------

workflow.add_node("planner", planner_agent)

workflow.add_node(
    "query_expansion",
    query_expansion_agent
)

workflow.add_node(
    "search",
    search_agent
)

workflow.add_node(
    "ranking",
    ranking_agent
)

workflow.add_node(
    "analysis",
    analysis_agent
)

workflow.add_node(
    "reflection",
    reflection_agent
)

workflow.add_node(
    "gap",
    gap_agent
)

workflow.add_node(
    "innovation",
    innovation_agent
)

workflow.add_node(
    "critic",
    critic_agent
)

workflow.add_node(
    "report",
    report_agent
)

# ------------------------
# Entry Point
# ------------------------

workflow.set_entry_point("planner")

# ------------------------
# Edges
# ------------------------

workflow.add_edge(
    "planner",
    "query_expansion"
)

workflow.add_edge(
    "query_expansion",
    "search"
)

workflow.add_edge(
    "search",
    "ranking"
)

workflow.add_edge(
    "ranking",
    "analysis"
)

workflow.add_edge(
    "analysis",
    "reflection"
)

workflow.add_conditional_edges(
    "reflection",
    reflection_router,
    {
        "search": "search",
        "gap": "gap"
    }
)

workflow.add_edge(
    "gap",
    "innovation"
)

workflow.add_edge(
    "innovation",
    "critic"
)

workflow.add_edge(
    "critic",
    "report"
)

workflow.add_edge(
    "report",
    END
)

graph = workflow.compile()