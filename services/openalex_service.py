import requests
import certifi

from config import OPENALEX_BASE_URL


def search_papers(query: str, limit: int = 10):
    """
    Search OpenAlex for research papers.
    """

    params = {
        "search": query,
        "per-page": limit
    }

    response = requests.get(
        OPENALEX_BASE_URL,
        params=params,
        verify=certifi.where(),
        timeout=30
    )

    response.raise_for_status()

    results = response.json()["results"]

    papers = []

    for paper in results:

        papers.append({
            "title": paper.get("display_name"),
            "year": paper.get("publication_year"),
            "doi": paper.get("doi"),
            "abstract": paper.get("abstract"),
            "citations": paper.get("cited_by_count", 0)
        })

    return papers


def search_multiple(queries, limit=10):
    """
    Search multiple queries and remove duplicates.
    """

    papers = []
    seen = set()

    for query in queries:

        results = search_papers(query, limit)

        for paper in results:

            doi = paper.get("doi")

            if doi in seen:
                continue

            seen.add(doi)

            papers.append(paper)

    return papers