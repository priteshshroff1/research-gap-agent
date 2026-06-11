<<<<<<< HEAD
# Research Gap Agent

## Overview

Research Gap Agent is a multi-agent AI system that analyzes scientific literature and identifies research gaps, innovation opportunities, and future research directions.

The system uses LangGraph to orchestrate multiple AI agents and OpenAlex as the literature retrieval source.

---

## Features

* Multi-Agent Architecture
* Automated Literature Search
* Query Expansion
* Paper Ranking
* Literature Analysis
* Research Gap Discovery
* Innovation Generation
* Critic Agent for Idea Refinement
* Reflection-Based Self-Correction
* AI Novelty Score
* Future Research Roadmap
* PDF Report Generation

---

## Architecture

```
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
      ├───────────────┐
      │               │
SEARCH_MORE       CONTINUE
      │               │
      ▼               ▼
Search Agent      Gap Agent
                      │
                      ▼
              Innovation Agent
                      │
                      ▼
                Critic Agent
                      │
                      ▼
                Report Agent
```

---

## Technology Stack

* Python 3.11
* LangGraph
* LangChain
* Gemini
* OpenAlex API
* Streamlit
* ReportLab

---

## Project Structure

```
research-gap-agent/

agents/
services/
prompts/
utils/
reports/

app.py
graph.py
run.py
config.py
state.py

requirements.txt
README.md
.env
.gitignore
```

---

## Installation

Create a virtual environment:

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variable

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Run the Application

Command Line:

```
python run.py
```

Streamlit UI:

```
streamlit run app.py
```

---

## Workflow

1. Planner Agent creates a search strategy.
2. Query Expansion Agent generates related search queries.
3. Search Agent retrieves papers from OpenAlex.
4. Ranking Agent selects the most relevant papers.
5. Analysis Agent analyzes the literature.
6. Reflection Agent determines whether additional search is required.
7. Gap Agent discovers research opportunities.
8. Innovation Agent generates novel ideas and future directions.
9. Critic Agent refines the generated ideas.
10. Report Agent produces the final report.

---

## Example Topic

```
Agentic AI in Scientific Publishing
```

---

## Generated Output

* Literature Analysis
* Research Gaps
* Innovation Opportunities
* AI Novelty Score
* Future Research Roadmap
* Multi-Agent Execution Log
* Final Report
=======
# research-gap-agent
An AI-powered multi-agent system for literature analysis, research gap discovery, innovation generation, and automated report creation using LangGraph and LLMs.
>>>>>>> 55c627d6fa1e23c2186c2109138585eb505d0429
