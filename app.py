from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from services.news_service import search_news
from services.article_service import (
    extract_article_text,
    clean_text
)
from services.summarizer import summarize_text
from services.bias_detector import analyze_bias


app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/api/analyze")
def analyze():

    query = request.args.get(
        "q",
        ""
    ).strip()

    if not query:

        return jsonify({
            "error": "Please enter a topic."
        }), 400

    try:

        articles = search_news(query)

        results = []

        for article in articles:

            url = article["url"]

            article_text = (
                extract_article_text(url)
            )

            article_text = clean_text(
                article_text
            )

            if not article_text:

                article_text = (
                    article["description"]
                    or article["title"]
                    or ""
                )

            summary = summarize_text(
                article_text
            )

            bias = analyze_bias(
                article_text
            )

            results.append({

                "title": article["title"],

                "source": article["source"],

                "published_at":
                    article["published_at"],

                "url": article["url"],

                "image":
                    article["image"],

                "summary":
                    summary,

                "bias":
                    bias

            })

        return jsonify({

            "query": query,

            "count": len(results),

            "articles": results

        })

    except Exception as e:

        print(e)

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True
    )