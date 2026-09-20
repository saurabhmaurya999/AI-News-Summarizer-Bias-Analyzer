import re


LOADED_WORDS = {

    "high": [
        "shocking",
        "disastrous",
        "outrageous",
        "evil",
        "terrifying",
        "horrific",
        "absurd",
        "insane"
    ],

    "medium": [
        "dramatic",
        "controversial",
        "massive",
        "extreme",
        "dangerous",
        "radical",
        "major",
        "unprecedented"
    ]
}


def detect_loaded_words(text):

    text_lower = text.lower()

    detected = []

    for level, words in LOADED_WORDS.items():

        for word in words:

            if re.search(
                rf"\b{re.escape(word)}\b",
                text_lower
            ):

                detected.append({
                    "word": word,
                    "level": level
                })

    return detected


def sentiment_score(text):

    positive_words = [
        "success",
        "benefit",
        "improve",
        "progress",
        "positive",
        "growth"
    ]

    negative_words = [
        "failure",
        "problem",
        "crisis",
        "damage",
        "loss",
        "negative"
    ]

    text_lower = text.lower()

    positive = sum(
        text_lower.count(word)
        for word in positive_words
    )

    negative = sum(
        text_lower.count(word)
        for word in negative_words
    )

    total = positive + negative

    if total == 0:
        return {
            "positive": 0,
            "negative": 0,
            "score": 0
        }

    score = (
        (positive - negative)
        / total
    )

    return {
        "positive": positive,
        "negative": negative,
        "score": round(score, 2)
    }


def analyze_bias(text):

    loaded_words = detect_loaded_words(text)

    sentiment = sentiment_score(text)

    score = 0

    score += len(loaded_words) * 10

    if abs(sentiment["score"]) > 0.6:
        score += 20

    score = min(
        score,
        100
    )

    if score < 25:
        level = "Low"

    elif score < 60:
        level = "Medium"

    else:
        level = "High"

    return {
        "indicator_score": score,
        "level": level,
        "loaded_words": loaded_words,
        "sentiment": sentiment
    }