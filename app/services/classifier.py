from app.services.llm_service import generate_completion

def classify_lead(message: str):

    with open("app/prompts/classify_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.format(message=message)

    category = generate_completion(prompt)

    valid_categories = [
        "sales",
        "support",
        "spam",
        "partnership",
        "general"
    ]

    category = category.lower().strip()

    if category not in valid_categories:
        return "general"

    return category