from __future__ import annotations

import json
from typing import Any

from openai import OpenAI


def create_structured_response(
    *,
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_payload: str,
    schema_name: str,
    schema: dict[str, Any],
) -> dict[str, Any]:
    """Run one clean structured-output request.

    The call intentionally avoids previous response state and sets store=False so
    each case/condition can be treated as an independent clean-instance probe.
    """
    response = client.responses.create(
        model=model,
        store=False,
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_payload},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": schema_name,
                "strict": True,
                "schema": schema,
            }
        },
    )
    return json.loads(response.output_text)
