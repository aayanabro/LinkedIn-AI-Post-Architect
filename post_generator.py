from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    mapping = {"Short": "1 to 5 lines", "Medium": "6 to 15 lines", "Long": "15 to 30 lines"}
    return mapping.get(length, "6 to 10 lines")

def generate_post(length, language, tag, tone):
    length_str = get_length_str(length)
    
    # Improved Prompt for Recruiters to see high quality
    prompt = f"""
    You are an expert LinkedIn Content Strategist.
    Generate a post about: {tag}
    Length: {length_str}
    Language: {language}
    Tone: {tone}
    
    Rules:
    - Use a strong "hook" in the first line.
    - Use bullet points if the length is Medium or Long.
    - End with a question to drive comments.
    - Keep sentences concise.
    """
    
    examples = few_shot.get_filtered_posts(length, language, tag)
    if examples:
        prompt += "\n\nFollow this writing style:\n"
        for ex in examples[:2]:
            prompt += f"\n---\n{ex['text']}\n"

    response = llm.invoke(prompt)
    return response.content