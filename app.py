import os

import streamlit as st

from graph import graph
from utils.pdf_generator import generate_pdf

st.set_page_config(
page_title="Research Gap Agent",
page_icon="🔬",
layout="wide"
)

st.title("🔬 Research Gap Agent")

st.markdown(
"AI-powered Literature Analysis and Research Gap Discovery"
)

# ----------------------------------------------------

# Session State Initialization

# ----------------------------------------------------

if "final_state" not in st.session_state:
    st.session_state.final_state = None

if "workflow_steps" not in st.session_state:
    st.session_state.workflow_steps = []

topic = st.text_input(
"Enter Research Topic"
)

if st.button("Generate Report"):

    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:

        # Reset previous execution
        st.session_state.final_state = None
        st.session_state.workflow_steps = []

        state = {
        "topic": topic,
        "search_queries": [],
        "papers": [],
        "analysis": "",
        "confidence": 0.0,
        "next_action": "",
        "retry_count": 0,
        "gaps": "",
        "innovation": "",
        "critique": "",
        "report": ""
    }

    st.subheader("Workflow Progress")

    progress_bar = st.progress(0)

    steps_container = st.container()

    steps = {
        "planner": (10, "Planner Agent completed"),
        "query_expansion": (20, "Query Expansion Agent completed"),
        "search": (35, "Search Agent completed"),
        "ranking": (50, "Ranking Agent completed"),
        "analysis": (65, "Analysis Agent completed"),
        "reflection": (75, "Reflection Agent completed"),
        "gap": (85, "Gap Agent completed"),
        "innovation": (90, "Innovation Agent completed"),
        "critic": (95, "Critic Agent completed"),
        "report": (100, "Report Agent completed")
    }

    final_state = None

    for event in graph.stream(state):
        for node_name, node_state in event.items():
            if node_name in steps:
                percent, message = steps[node_name]
                progress_bar.progress(percent)
                st.session_state.workflow_steps.append(message)
                with steps_container:
                    html = ""
                    for step in st.session_state.workflow_steps:
                        html += (
                            "<div style=\""
                            "font-size:12px;"
                            "color:#2E8B57;"
                            "margin-bottom:2px;"
                            "\">"
                            f"✓ {step}"
                            "</div>"
                        )
                    st.markdown(html, unsafe_allow_html=True)
            final_state = node_state

    progress_bar.progress(100)

    st.success(
        "Workflow completed successfully!"
    )

    st.session_state.final_state = final_state


# Display Report

if st.session_state.final_state is not None:
    st.markdown("---")

    st.subheader("Research Gap Report")

    st.markdown(st.session_state.final_state["report"])

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join("reports", "research_gap_report.pdf")

    generate_pdf(st.session_state.final_state["report"], pdf_path)

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name="research_gap_report.pdf",
            mime="application/pdf",
        )
