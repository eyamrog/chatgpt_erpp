#!/bin/bash
clear
read -p "Enter your OpenAI API key: " openai_api_key
echo "Thank you! End the programme with Ctrl+Z when you are done."
count=1
while true
do
    echo "response_"$count".txt"
    read -p "Enter your ChatGPT prompt: " prompt
    echo $prompt > response_"$count".txt
    curl -X POST "https://api.openai.com/v1/chat/completions" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ${openai_api_key}" \
     -d '{
         "model": "gpt-3.5-turbo",
         "messages": [
             {"role": "user", "content": "'"$prompt"'"}
         ]
     }' >> response_"$count".txt
    more response_"$count".txt
    count=$((count+1))
done
