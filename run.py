from graph import graph


def main():

    print("=" * 60)
    print("Research Gap Agent")
    print("=" * 60)

    topic = input("\nEnter Research Topic: ").strip()

    initial_state = {
        "topic": topic,
        "search_queries": [],
        "papers": [],
        "analysis": "",
        "confidence": 0.0,
        "next_action": "",
        "gaps": "",
        "innovation": "",
        "critique": "",
        "report": ""
    }

    final_state = graph.invoke(initial_state)

    print("\n")
    print("=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print()

    print(final_state["report"])


if __name__ == "__main__":
    main()