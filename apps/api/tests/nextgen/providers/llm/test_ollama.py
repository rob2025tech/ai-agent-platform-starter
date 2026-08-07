# apps/api/tests/nextgen/providers/llm/test_ollama.py

import pytest

# from unittest.mock import AsyncMock, patch, MagicMock

from apps.api.providers.llm.ollama import OllamaLLM


@pytest.mark.anyio
async def test_ollama_generate():

    provider = OllamaLLM()

    # mock_response = MagicMock()
    # mock_response.json.return_value = {"response": "Hello from mock ollama!"}


    response = await provider.generate(
        prompt="Say hello in one word",
        memories=[],
    )


    assert isinstance(
        response,
        str,
    )

    assert len(response) > 0