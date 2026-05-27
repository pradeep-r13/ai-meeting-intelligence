import ollama

SYSTEM_PROMPT = """
You are an expert meeting analyst.

Extract all decisions.

Return valid JSON.

Example:

{
  "decisions":[
    {
      "decision":"Use Qdrant",
      "owner":"Pradeep",
      "status":"approved"
    }
  ]
}
"""

def extract_decisions(transcript):

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":transcript
            }
        ]
    )

    return response["message"]["content"]