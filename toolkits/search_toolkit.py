import duckduckgo_search

def search_duckduckgo(query):
    from duckduckgo_search import DDGS
    with DDGS() as ddgs:
        results = ddgs.text(query, region="wt-wt", safesearch="Moderate", max_results=5)
        return list(results)
