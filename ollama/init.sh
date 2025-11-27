#!/bin/bash

MODEL_FILE="/ollama/models.txt"

is_ollama_server_ready() {
  ollama list > /dev/null 2>&1
  return $?
}

echo "Waiting for Ollama server to become available..."
while ! is_ollama_server_ready; do
  echo "Ollama server not ready yet. Retrying in 5 seconds..."
  sleep 5
done
echo "Ollama server is ready!"

if [[ ! -f "$MODEL_FILE" ]]; then
  echo "Error: $MODEL_FILE not found!"
  exit 1
fi

is_model_pulled() {
  local MODEL_NAME=$1
  ollama list | grep -qw "$MODEL_NAME"
  return $?
}

while IFS= read -r MODEL_NAME; do
  # Trim whitespace and skip empty lines
  MODEL_NAME=$(echo "$MODEL_NAME" | xargs)
  if [[ -z "$MODEL_NAME" ]]; then
    continue
  fi

  if is_model_pulled "$MODEL_NAME"; then
    echo "Model '$MODEL_NAME' is already pulled. Skipping..."
    continue
  fi

  echo "Pulling model: $MODEL_NAME..."
  ollama pull "$MODEL_NAME"

  # Check if the command was successful
  if [[ $? -eq 0 ]]; then
    echo "Successfully pulled model: $MODEL_NAME"
  else
    echo "Failed to pull model: $MODEL_NAME"
  fi

done < "$MODEL_FILE"

echo "All models processed."
