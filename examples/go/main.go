package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type ChatMessage struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type ChatRequest struct {
	Model    string        `json:"model"`
	Messages []ChatMessage `json:"messages"`
}

func main() {
	body, _ := json.Marshal(ChatRequest{
		Model: "kimi",
		Messages: []ChatMessage{
			{Role: "user", Content: "Explain API failover in one short sentence."},
		},
	})

	req, err := http.NewRequest(http.MethodPost, "http://127.0.0.1:8000/v1/chat/completions", bytes.NewReader(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer anything")
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	payload, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(payload))
}
