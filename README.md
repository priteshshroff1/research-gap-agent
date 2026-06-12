# 🔬 Research Gap Agent

An **AI-powered Multi-Agent Research Intelligence Platform** that automates literature analysis, discovers research gaps, identifies innovation opportunities, and generates comprehensive research reports using **LangGraph**, **Groq LLM**, and **OpenAlex**.

The platform leverages a team of specialized AI agents to search scientific literature, rank research papers using citation-aware intelligence, analyze trends, identify research gaps, and propose future research directions.

---

# 🚀 Features

* 🤖 Multi-Agent AI Workflow using LangGraph
* 🔍 Intelligent Query Expansion
* 📚 Automated Literature Search using OpenAlex
* 📊 Citation-aware Research Ranking
* 📈 Publication Trend Analysis
* ⭐ Research Impact Scoring
* 🏆 Top Influential Papers Identification
* 🔬 Automated Research Gap Discovery
* 💡 Innovation Opportunity Generation
* 🛡️ AI Critic Validation
* 📑 Comprehensive Research Intelligence Report
* 📄 PDF Report Download
* ⚡ Interactive Streamlit Dashboard

---

# 🏗️ Multi-Agent Architecture

```text
                         User Topic
                              │
                              ▼
                     Planner Agent
                              │
                              ▼
                Query Expansion Agent
                              │
                              ▼
                      Search Agent
                              │
                              ▼
                     Ranking Agent
                              │
                              ▼
                     Analysis Agent
                              │
                              ▼
                    Reflection Agent
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
        SEARCH_MORE                    CONTINUE
               │                             │
               ▼                             ▼
         Search Agent                  Gap Agent
                                             │
                                             ▼
                                    Innovation Agent
                                             │
                                             ▼
                                      Critic Agent
                                             │
                                             ▼
                                      Report Agent
                                             │
                                             ▼
                        📄 Final Research Intelligence Report
```

---

# 🔄 Workflow

1. **Planner Agent** understands the user's research topic and creates an execution plan.
2. **Query Expansion Agent** generates semantic search queries.
3. **Search Agent** retrieves research papers from OpenAlex.
4. **Ranking Agent** prioritizes papers using:

   * Semantic Relevance
   * Citation Count
   * Publication Recency
   * Research Impact Score
5. **Analysis Agent** analyzes the highest-quality literature.
6. **Reflection Agent** evaluates whether sufficient evidence exists.
7. If needed, the workflow loops back to the **Search Agent** for additional retrieval.
8. **Gap Agent** identifies research gaps.
9. **Innovation Agent** proposes novel research opportunities.
10. **Critic Agent** validates and strengthens the findings.
11. **Report Agent** generates the final AI-powered research intelligence report.

---

# 📊 Research Intelligence Dashboard

The dashboard automatically generates:

* 📄 Papers Retrieved
* ⭐ Average Citation Count
* 🏆 Highest Citation Count
* 📈 Publication Trend
* 🔥 Research Momentum
* 🥇 Top Influential Papers
* 📊 Research Impact Score

These insights help researchers quickly understand the maturity and influence of a research domain before diving into detailed literature analysis.

---

# 📑 Final Report Includes

* Executive Summary
* Research Landscape
* Literature Analysis
* Citation Intelligence
* Publication Trends
* Research Gaps
* Innovation Opportunities
* Novelty Assessment
* Future Research Directions
* Critic Review
* Final Recommendations

---

# 🛠️ Technology Stack

* Python
* LangGraph
* LangChain
* Groq LLM
* OpenAlex API
* Streamlit
* ReportLab

---

# 📂 Project Structure

```text
research-gap-agent/

│── agents/
│      planner_agent.py
│      query_expansion_agent.py
│      search_agent.py
│      ranking_agent.py
│      analysis_agent.py
│      reflection_agent.py
│      gap_agent.py
│      innovation_agent.py
│      critic_agent.py
│      report_agent.py

│── prompts/

│── services/
│      llm_service.py
│      openalex_service.py
│      prompt_manager.py

│── utils/
│      pdf_generator.py

│── reports/

│── graph.py

│── app.py

│── config.py

│── state.py
```

---

# ⚡ Installation

```bash
git clone https://github.com/<your-username>/research-gap-agent.git

cd research-gap-agent

pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

*(OpenAlex is open and does not require an API key for basic usage.)*

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🎯 Typical User Journey

* Enter a research topic.
* AI expands search queries.
* OpenAlex retrieves relevant literature.
* Papers are ranked using citation-aware research intelligence.
* Literature is analyzed.
* Publication trends and citation statistics are generated.
* Research gaps are identified.
* Innovation opportunities are proposed.
* Findings are validated by the Critic Agent.
* A comprehensive research intelligence report is generated.
* Report can be downloaded as a PDF.

---

# ⚡ Performance Optimizations

To optimize Groq token usage and improve response time:

* Only the **Top 5 ranked papers** are analyzed.
* Abstracts are truncated to **300 characters**.
* Only the **first 3 authors** are retained.
* Intermediate agent outputs are compressed before report generation.
* Citation statistics and publication trends are computed programmatically instead of consuming LLM tokens.

These optimizations significantly reduce token consumption while preserving report quality.

---

# 🚀 Future Enhancements

* Citation Network Visualization
* Author Collaboration Graphs
* Topic Evolution Timeline
* Knowledge Graph Generation
* Patent Intelligence Integration
* Funding Opportunity Discovery
* AI-powered Research Roadmap Generator
* Multi-source Literature Search (OpenAlex + CrossRef + Semantic Scholar)

---

# 📜 License

MIT License

---

# 🌟 Vision

Traditional literature reviews summarize published work.

**Research Gap Agent goes one step further—transforming scientific publications into actionable research intelligence by combining citation analytics, AI-driven gap discovery, and innovation opportunity generation.**

**From literature review to research intelligence—accelerating scientific discovery through AI.**
