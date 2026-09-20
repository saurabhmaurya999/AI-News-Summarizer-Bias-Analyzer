from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


model = SentenceTransformer(
    MODEL_NAME
)


def create_embedding(text):

    return model.encode(
        text,
        convert_to_numpy=True
    )


def similarity(text1, text2):

    embedding1 = create_embedding(text1)
    embedding2 = create_embedding(text2)

    score = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return float(score)