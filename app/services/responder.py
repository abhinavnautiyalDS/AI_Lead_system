from app.services.llm_service import generate_completion

def generate_response(message: str, category: str):

    with open("app/prompts/response_prompt.txt", "r") as file:
        prompt_template = file.read()

    prompt = prompt_template.format(
        category=category,
        message=message
    )

    response = generate_completion(prompt)

    return response