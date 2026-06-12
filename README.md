# 🔬 Research Gap Agent

An AI-powered **Multi-Agent Research Intelligence Platform** that automates literature analysis, discovers research gaps, identifies innovation opportunities, and generates comprehensive research reports using **LangGraph**, **Groq LLM**, and openAlex.

---

# 🚀 Features

* 🤖 Multi-Agent AI Workflow using LangGraph
* 🔍 Intelligent Query Expansion
* 📚 Automated Literature Search
* 📊 Citation & Impact-aware Paper Ranking
* 📈 Publication Trend Analysis
* 🏆 Research Intelligence Dashboard
* 🔬 Research Gap Discovery
* 💡 Innovation Opportunity Generation
* 🛡️ Critic Agent Validation
* 📑 AI-generated Research Report
* 📄 PDF Export
* ⚡ Interactive Streamlit UI

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

1. **Planner Agent** understands the research topic and creates an execution plan.
2. **Query Expansion Agent** generates multiple openalex search queries.
3. **Search Agent** retrieves relevant literature from OpenAlex 
4. **Ranking Agent** prioritizes papers using relevance, citation count, publication recency, and impact score.
5. **Analysis Agent** performs literature analysis on the highest-ranked papers.
6. **Reflection Agent** evaluates whether additional literature is required.
7. If confidence is low, the workflow loops back to the **Search Agent** for additional retrieval.
8. Otherwise, the **Gap Agent** identifies research gaps.
9. The **Innovation Agent** proposes novel research ideas and opportunities.
10. The **Critic Agent** validates and refines the findings.
11. The **Report Agent** generates a comprehensive AI-powered research intelligence report.

---

# 📊 Research Intelligence

The Ranking Agent enriches the research pipeline by generating:

* 📄 Total Papers Analyzed
* ⭐ Average Citation Count
* 🏆 Highest Citation Count
* 📈 Publication Trends
* 🔥 Research Momentum
* 🥇 Top Influential Papers
* 📊 Research Impact Score

This enables downstream agents to focus on the most impactful and relevant research.

---

# 📑 Generated Report Includes

* Executive Summary
* Research Landscape
* Literature Analysis
* Research Gaps
* Innovation Opportunities
* Novelty Assessment
* Future Research Roadmap
* Critic Review
* Final Recommendation

---

# 🛠️ Technology Stack

* Python
* LangGraph
* LangChain
* Groq LLM
* openalex 
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

│── utils/

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

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🎯 Typical User Journey

* Enter a research topic.
* AI expands search queries.
* Relevant papers are retrieved.
* Papers are ranked using Research Intelligence scoring.
* Literature is analyzed.
* Research gaps are identified.
* Innovation opportunities are generated.
* Results are validated by the Critic Agent.
* A comprehensive research intelligence report is produced.
* The report can be downloaded as a PDF.

---

# 🚀 Future Enhancements

* Citation Network Visualization
* Author Collaboration Graphs
* Topic Evolution Timeline
* Knowledge Graph Generation
* Patent Intelligence Integration
* Funding Opportunity Discovery
* Multi-source Literature Search
* AI-powered Research Roadmap Generator

---

# 📜 License

MIT License

---

## 🌟 Vision

Move beyond traditional literature reviews and transform scientific publications into actionable research intelligence.

**From publishing knowledge to powering scientific discovery through AI.**
