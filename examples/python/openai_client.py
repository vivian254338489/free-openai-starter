from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key="anything",
        base_url="http://127.0.0.1:8000/v1",
    )

    response = client.chat.completions.create(
        model="kimi",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user", "content": "Explain what account rotation means in one sentence."},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
