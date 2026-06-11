from services.openalex_service import search_papers

papers = search_papers("Agentic AI")

print(f"Found {len(papers)} papers\n")

for paper in papers:
    print(paper["display_name"])