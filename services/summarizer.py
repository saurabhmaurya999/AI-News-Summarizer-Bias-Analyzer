from transformers import pipeline


MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


summarizer = pipeline(
    "summarization",
    model=MODEL_NAME
)


def split_text(text, max_words=450):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        max_words
    ):

        chunks.append(
            " ".join(
                words[i:i + max_words]
            )
        )

    return chunks


def summarize_text(text):

    if not text:
        return "No article text available."

    chunks = split_text(text)

    summaries = []

    for chunk in chunks[:5]:

        if len(chunk.split()) < 50:
            continue

        try:

            result = summarizer(
                chunk,
                max_length=120,
                min_length=30,
                do_sample=False
            )

            summaries.append(
                result[0]["summary_text"]
            )

        except Exception as e:

            print(
                "Summarization error:",
                e
            )

    if not summaries:

        return text[:500]

    return " ".join(summaries)