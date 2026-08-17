#!/usr/bin/env python3
"""Minimal Gemini text-generation demo using the Google Gen AI SDK."""

import os
from google import genai

PROMPT = """
اكتب فقرة عربية من 60 إلى 80 كلمة عن أثر الذكاء الاصطناعي في تعلّم البرمجة.
استخدم أسلوبًا واضحًا ومهنيًا، وتجنب المبالغة، ثم أضف عنوانًا قصيرًا في سطر منفصل.
""".strip()


def main() -> None:
    if not os.environ.get("GEMINI_API_KEY"):
        raise RuntimeError("لم يُضبط المتغير GEMINI_API_KEY.")

    client = genai.Client()
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        system_instruction="أنت محرر تقني عربي. التزم باللغة العربية الفصحى والدقة.",
        input=PROMPT,
        generation_config={
            "temperature": 0.6,
            "max_output_tokens": 220,
            "thinking_level": "low",
        },
    )

    print(interaction.output_text)


if __name__ == "__main__":
    main()
