package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/api/hello", helloHandler)
	http.HandleFunc("/api/monsters", getMonstersHandler) // Placeholder for monster data

	port := ":8080"
	fmt.Printf("Go API server listening on port %s\n", port)
	log.Fatal(http.ListenAndServe(port, nil))
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != "GET" {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	response := map[string]string{"message": "Hello from Go API!"}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func getMonstersHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != "GET" {
        http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
        return
    }
    // In a real application, this would fetch data from PostgreSQL
    // For now, it's a placeholder.
    response := []map[string]string{
        {"id": "1", "name": "Dummy Monster A"},
        {"id": "2", "name": "Dummy Monster B"},
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(response)
}

