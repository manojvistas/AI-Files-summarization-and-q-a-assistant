#!/bin/sh
set -e

# Start Ollama server in the background
ollama serve &

# Wait for the server to be ready
sleep 5

# Pull the llama3 model
ollama pull llama3

# Pull the nomic-embed-text model
ollama pull nomic-embed-text

# Keep the container running
tail -f /dev/null
