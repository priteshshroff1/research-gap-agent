
import requests
import certifi

from config import OPENALEX_BASE_URL


def reconstruct_abstract(inverted_index):
    """
    Reconstruct abstract from OpenAlex abstract_inverted_index.
    """

    if not inverted_index:
        return ""

    words = []

    for word, positions in inverted_index.items():
        for pos in positions:
            words.append((pos, word))

    words.sort(key=lambda x: x[0])

    abstract = " ".join(
        word for _, word in words
    )

    # Limit abstract size for LLM token optimization
    return abstract[:300]


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

    results = response.json().get(
        "results",
        []
    )

    papers = []

    for paper in results:

        # -----------------------
        # Abstract
        # -----------------------

        abstract = reconstruct_abstract(
            paper.get(
                "abstract_inverted_index"
            ) or {}
        )

        # -----------------------
        # Authors
        # -----------------------

        authors = []

        for author_info in (
            paper.get("authorships") or []
        )[:3]:

            author = author_info.get(
                "author"
            ) or {}

            name = author.get(
                "display_name"
            )

            if name:
                authors.append(name)

        # -----------------------
        # Venue
        # -----------------------

        venue = ""

        primary_location = (
            paper.get(
                "primary_location"
            ) or {}
        )

        source = (
            primary_location.get(
                "source"
            ) or {}
        )

        venue = source.get(
            "display_name",
            ""
        )

        # -----------------------
        # Citations
        # -----------------------

        citations = paper.get(
            "cited_by_count",
            0
        )

        # -----------------------
        # Relevance Score
        # -----------------------

        score = paper.get(
            "relevance_score",
            0.5
        )

        papers.append({

            "title":
                paper.get(
                    "display_name",
                    ""
                ),

            "year":
                paper.get(
                    "publication_year",
                    0
                ),

            "doi":
                paper.get(
                    "doi",
                    ""
                ),

            "abstract":
                abstract,

            "authors":
                authors,

            "venue":
                venue,

            "citations":
                citations,

            "score":
                score

        })

    return papers


def search_multiple(
    queries,
    limit=10
):
    """
    Search multiple queries and remove duplicates.
    """

    papers = []

    seen = set()

    for query in queries:

        results = search_papers(
            query=query,
            limit=limit
        )

        for paper in results:

            key = (
                paper.get("doi")
                or paper.get("title")
            )

            if key in seen:
                continue

            seen.add(key)

            papers.append(paper)

    return papers
