async function analyzeNews() {

    const query =
        document.getElementById(
            "query"
        ).value.trim();


    if (!query) {

        alert(
            "Please enter a topic."
        );

        return;
    }


    const loading =
        document.getElementById(
            "loading"
        );


    const results =
        document.getElementById(
            "results"
        );


    loading.style.display =
        "block";


    results.innerHTML = "";


    try {

        const response =
            await fetch(
                `/api/analyze?q=${encodeURIComponent(query)}`
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.error ||
                "Something went wrong"
            );
        }


        if (
            !data.articles ||
            data.articles.length === 0
        ) {

            results.innerHTML =
                "<p>No articles found.</p>";

            return;
        }


        data.articles.forEach(
            article => {

                const bias =
                    article.bias;


                const words =
                    bias.loaded_words
                    .map(
                        item =>
                            `<span class="word">
                                ${item.word}
                             </span>`
                    )
                    .join("");


                const biasClass =
                    `bias-${bias.level.toLowerCase()}`;


                const card =
                    document.createElement(
                        "div"
                    );


                card.className =
                    "news-card";


                card.innerHTML = `

                    <h2>
                        ${article.title}
                    </h2>

                    <div class="source">

                        ${article.source}
                        |
                        ${article.published_at}

                    </div>


                    <h3>
                        AI Summary
                    </h3>

                    <p class="summary">
                        ${article.summary}
                    </p>


                    <div
                        class="bias-box
                        ${biasClass}"
                    >

                        <h3>
                            Potential Framing Indicators
                        </h3>

                        <p>

                            Level:
                            <strong>
                                ${bias.level}
                            </strong>

                        </p>

                        <p>

                            Indicator score:
                            <strong>
                                ${bias.indicator_score}/100
                            </strong>

                        </p>


                        <p>
                            Detected loaded words:
                        </p>

                        <div>
                            ${words || "None detected"}
                        </div>


                        <p>

                            Positive signals:
                            ${bias.sentiment.positive}

                            <br>

                            Negative signals:
                            ${bias.sentiment.negative}

                        </p>

                    </div>


                    <a
                        class="read-more"
                        href="${article.url}"
                        target="_blank"
                    >
                        Read Original Article →
                    </a>

                `;


                results.appendChild(
                    card
                );

            }
        );


    } catch (error) {

        results.innerHTML = `

            <div class="news-card">

                <h3>
                    Error
                </h3>

                <p>
                    ${error.message}
                </p>

            </div>

        `;

    } finally {

        loading.style.display =
            "none";

    }

}