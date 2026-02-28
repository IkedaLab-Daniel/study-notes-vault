from langchain.tools import tool


### -- Exercise 1 -- ###
""""
Instructions:

1. Create a tool called calculator_tool using the @tool decorator.
2. The tool should accept a mathematical expression as a string.
3. Use Python's eval() function carefully (or better yet, use the ast module for safety).
4. Test your tool with various mathematical expressions.
5. Add your tool to the tools list and test it with the ReAct agent.
"""
import math

@tool
def calculator_tool(expression: str) -> str:
    """
    Evaluate mathematical expressions.
    
    Supports math functions like sqrt, sin, cos, etc.
    
    Example:
        0.15 * 250 + sqrt(144)
    """

    allowed_names = {
        # math functions
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "log10": math.log10,
        "exp": math.exp,
        # constants
        "pi": math.pi,
        "e": math.e,
    }

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    
### -- Exercise 2 -- ###
"""
Instructions:
1. Create a `news_summarizer_tool` that takes news content and creates summaries.
2. The tool should extract key information: headline, date, main points.
3. Format the output in a readable way.
4. Test it by asking the agent to "search for recent AI news and summarize the top 3 articles".
"""
import json

@tool
def news_summarizer_tool(news_content: str) -> str:
    """
    Summarize news articles from search results.

    :param news_content: Raw news content (JSON string or list of dicts)
    :return: A formatted summary of the news
    """

    try:
        # If passed as JSON string, convert to Python object
        if isinstance(news_content, str):
            news_content = json.loads(news_content)

        if not isinstance(news_content, list):
            return "No valid news articles found."

        summaries = []

        for article in news_content:
            if not isinstance(article, dict):
                continue

            title = article.get("title", "No Title")
            url = article.get("url", "")
            content = article.get("content", "")
            date = article.get("published_date", "Unknown date")

            # Extract first 2–3 sentences as quick summary
            sentences = content.split(". ")
            short_summary = ". ".join(sentences[:2]).strip()

            summaries.append(
                f"**{title}**\n"
                f"{date}\n"
                f"{short_summary}.\n"
                f"{url}\n"
            )

        if not summaries:
            return "No readable articles found."

        return "\n---\n".join(summaries)

    except Exception as e:
        return f"Error summarizing news: {str(e)}"