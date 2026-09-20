import requests

import re

from bs4 import BeautifulSoup


def extract_article_text(url):

    try:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        for element in soup(
            ["script", "style", "nav", "footer", "header"]
        ):
            element.decompose()

        paragraphs = soup.find_all("p")

        text = " ".join(
            paragraph.get_text(" ", strip=True)
            for paragraph in paragraphs
        )

        return text

    except Exception as e:

        print("Article extraction error:", e)

        return ""



def clean_text(text):

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = re.sub(
        r"http\S+",
        "",
        text
    )

    return text.strip()