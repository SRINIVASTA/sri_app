from duckduckgo_search import DDGS

def run_web_search(query):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=5))
