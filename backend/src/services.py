import os
import openai

from src.config import settings
from src.schemas import BrainDumpResponse

MODEL_URL = "https://api.groq.com/openai/v1"
SYSTEM_PROMPT = """
You are an expert technical Product Manager and Agile Lead. Your job is to analyze chaotic, unstructured braindump text, meeting notes, or voice transcripts and convert them into clear, actionable, and well-scoped technical tasks.

Follow these strict output guidelines:
1. Deconstruct the Input: Identify every distinct bug, feature, task, or technical debt item mentioned in the text.
2. Group & Isolate: Do not merge distinct pieces of work into a single vague item. Keep tasks modular and self-contained.
3. Write Clear Titles: Formulate concise, action-oriented headlines (e.g., "Implement JWT user authentication endpoint" rather than "Fix auth").
4. Provide Contextual Descriptions: Summarize relevant background details, assumptions, or edge cases from the input text into the task description.
5. Categorize & Prioritize accurately: Assign an appropriate Category (Feature, Bug, Task, Refactor) and Priority level (High, Medium, Low) based on urgency implied in the text.
"""

def parse_text_to_item(raw_text: str) -> BrainDumpResponse | None:
    client = openai.OpenAI(api_key=settings.GROQ_API_KEY, base_url=MODEL_URL)

    completion = client.chat.completions.parse(
        model=settings.LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": raw_text}
        ],
        response_format=BrainDumpResponse
    )

    return completion.choices[0].message.parsed
