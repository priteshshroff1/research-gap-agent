from pathlib import Path


# Path to the prompts directory
PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

def load_prompt(prompt_name: str, **kwargs) -> str:
    """
    Load a prompt template and replace placeholders
    like {topic}, {analysis}, {papers}, etc.
    """
    prompt_path = PROMPTS_DIR / f"{prompt_name}.txt"

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_path}"
        )

    template = prompt_path.read_text(
        encoding="utf-8"
    )

    # Replace only known placeholders
    for key, value in kwargs.items():
        template = template.replace(
            f"{{{key}}}",
            str(value)
        )

    return template

