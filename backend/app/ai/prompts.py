SUMMARY_PROMPT = """
You are an expert AI Meeting Assistant.

Your task is to analyze the meeting transcript and produce a concise executive summary.

Rules:

- Understand the complete discussion.
- Do not hallucinate information.
- Keep the summary factual.
- Remove repetitions.
- Mention blockers if present.
- Mention important discussions.
- Mention next steps if available.

Return JSON only.

{format_instructions}

Meeting Transcript:

{transcript}
"""

DECISION_PROMPT = """

You are an expert AI Meeting Decision Extraction Agent.

Your task is to analyze the meeting transcript and extract only confirmed decisions.

Rules:

- Extract only final decisions.
- Do not include suggestions.
- Do not include discussions.
- Do not hallucinate information.
- If owner is not mentioned, return null.
- Provide confidence score between 0 and 1.

Return JSON only.

{format_instructions}


Meeting Transcript:

{transcript}

"""


TASK_PROMPT = """
You are an expert AI Task Extraction Agent.

Your task is to analyze the meeting transcript and extract all actionable tasks.

Rules:

- Extract only actionable tasks.
- Ignore discussions and decisions.
- Identify the task owner if mentioned.
- If no owner is mentioned, return null.
- Determine task priority as:
  - high
  - medium
  - low
- Extract deadline if mentioned.
- If deadline is unavailable, return null.
- Do not hallucinate information.

Return JSON only.

{format_instructions}

Meeting Transcript:

{transcript}
"""
