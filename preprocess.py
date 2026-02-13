import json
import os
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

def process_posts(raw_file_path, processed_file_path):
    if not os.path.exists(raw_file_path):
        print("Raw file not found!")
        return

    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        enriched_posts = []
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        post['tags'] = list({unified_tags.get(tag, tag) for tag in post['tags']})

    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)
    print("Processing Complete!")

def extract_metadata(post):
    template = '''Extract: line_count, language, tags (max 2). JSON only. No preamble.
    Post: {post}'''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm | JsonOutputParser()
    return chain.invoke(input={"post": post})

def get_unified_tags(posts):
    unique_tags = set()
    for post in posts: unique_tags.update(post['tags'])
    
    template = '''Unify these tags into a mapping JSON. {tags}'''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm | JsonOutputParser()
    return chain.invoke(input={"tags": str(list(unique_tags))})

if __name__ == "__main__":
    # Ensure data folder exists
    if not os.path.exists("data"): os.makedirs("data")
    process_posts("data/raw_posts.json", "data/processed_posts.json")