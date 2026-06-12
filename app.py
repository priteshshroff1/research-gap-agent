
import os
import streamlit as st

from graph import graph
from utils.pdf_generator import generate_pdf

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

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

# ----------------------------------------------------
# User Input
# ----------------------------------------------------

topic = st.text_input(
    "Enter Research Topic"
)

# ----------------------------------------------------
# Workflow Execution
# ----------------------------------------------------

if st.button("Generate Report"):

    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

    else:

        # Reset session state

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

            "report": "",

            "research_landscape": {}

        }

        st.subheader(
            "Workflow Progress"
        )

        progress_bar = st.progress(0)

        progress_placeholder = st.empty()

        steps = {

            "planner":
                (
                    10,
                    "Planner Agent"
                ),

            "query_expansion":
                (
                    20,
                    "Query Expansion Agent"
                ),

            "search":
                (
                    35,
                    "Search Agent"
                ),

            "ranking":
                (
                    50,
                    "Research Intelligence Agent"
                ),

            "analysis":
                (
                    65,
                    "Analysis Agent"
                ),

            "reflection":
                (
                    75,
                    "Reflection Agent"
                ),

            "gap":
                (
                    85,
                    "Gap Agent"
                ),

            "innovation":
                (
                    90,
                    "Innovation Agent"
                ),

            "critic":
                (
                    95,
                    "Critic Agent"
                ),

            "report":
                (
                    100,
                    "Report Agent"
                )

        }

        final_state = None

        for event in graph.stream(state):

            for node_name, node_state in event.items():

                if node_name in steps:

                    percent, agent = steps[node_name]

                    progress_bar.progress(
                        percent
                    )

                    st.session_state.workflow_steps.append(
                        agent
                    )

                    progress_text = " ➜ ".join(
                        st.session_state.workflow_steps
                    )

                    progress_placeholder.markdown(

                        f"""
<div style="
background-color:#F8F9FA;
padding:12px;
border-radius:8px;
border-left:5px solid #2E8B57;
font-size:13px;
">

<b>Workflow Execution</b><br><br>

{progress_text}

</div>
""",

                        unsafe_allow_html=True,

                    )

                final_state = node_state

        progress_bar.progress(100)

        st.success(
            "Research Gap Analysis Completed Successfully!"
        )

        st.session_state.final_state = final_state

# ----------------------------------------------------
# Display Report
# ----------------------------------------------------

if st.session_state.final_state is not None:

    st.markdown("---")

    landscape = st.session_state.final_state.get(
        "research_landscape",
        {}
    )

    # ----------------------------------------
    # Research Intelligence Dashboard
    # ----------------------------------------

    st.subheader(
        "🔬 Research Intelligence Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📄 Papers",
            landscape.get(
                "total_papers",
                0
            )
        )

    with col2:

        st.metric(
            "⭐ Avg Citations",
            round(
                landscape.get(
                    "average_citations",
                    0
                ),
                2
            )
        )

    with col3:

        st.metric(
            "🏆 Highest Citations",
            landscape.get(
                "highest_citations",
                0
            )
        )

    trend = landscape.get(
        "publication_trend",
        {}
    )

    momentum = "Unknown"

    if len(trend) >= 2:

        years = sorted(trend.keys())

        if trend[years[-1]] > trend[years[0]]:

            momentum = "Growing 📈"

        else:

            momentum = "Stable"

    with col4:

        st.metric(
            "🔥 Momentum",
            momentum
        )

    # ----------------------------------------
    # Publication Trend
    # ----------------------------------------

    if trend:

        st.markdown("---")

        st.subheader(
            "📈 Publication Trend"
        )

        st.bar_chart(trend)

    # ----------------------------------------
    # Top Influential Papers
    # ----------------------------------------

    top_papers = landscape.get(
        "top_papers",
        []
    )

    if top_papers:

        st.markdown("---")

        st.subheader(
            "🏆 Top Influential Papers"
        )

        for idx, paper in enumerate(
            top_papers,
            start=1
        ):

            st.markdown(
                f"""
### {idx}. {paper.get('title','Unknown')}

- **Year:** {paper.get('year','')}
- **Citations:** {paper.get('citations',0)}
- **Impact Score:** {round(paper.get('impact_score',0),3)}

---
"""
            )

    # ----------------------------------------
    # AI Report
    # ----------------------------------------

    st.markdown("---")

    st.subheader(
        "📑 Research Gap Report"
    )

    report = st.session_state.final_state.get(
        "report",
        ""
    )

    st.markdown(
        report
    )

    # ----------------------------------------
    # Generate PDF
    # ----------------------------------------

    os.makedirs(
        "reports",
        exist_ok=True
    )

    pdf_path = os.path.join(
        "reports",
        "research_gap_report.pdf"
    )

    generate_pdf(
        report_text=report,
        landscape=landscape,
        output_path=pdf_path
    )

    # ----------------------------------------
    # Download Button
    # ----------------------------------------

    with open(
        pdf_path,
        "rb"
    ) as pdf_file:

        st.download_button(

            label="📄 Download PDF Report",

            data=pdf_file,

            file_name="research_gap_report.pdf",

            mime="application/pdf",

        )


