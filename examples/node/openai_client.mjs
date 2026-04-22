import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "anything",
  baseURL: "http://127.0.0.1:8000/v1",
});

const response = await client.chat.completions.create({
  model: "kimi",
  messages: [
    { role: "system", content: "You are concise." },
    { role: "user", content: "Explain proxy rotation in one sentence." },
  ],
});

console.log(response.choices[0].message.content);
