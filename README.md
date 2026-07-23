Start your API:
This project uses relative imports, so to start uvicorn:

1. Make sure you are in the root directory (i.e. ai-agent-platform-starter)

2. From the root ai-agent-platform-starter directory, run:

source .venv/bin/activate
uvicorn apps.api.main:app --reload

3. From a different terminal, verify the API with this curl command:

curl http://localhost:8000/health

You should see:

{"status":"ok"}% 

4. If that status said "ok", test the execute endpoint:

curl -X POST http://localhost:8000/execute \
-H "Content-Type: application/json" \
-d '{
  "backend":"mock",
  "prompt":"Hello"
}'

You should see this:

{"detail":[{"type":"missing","loc":["body","input"],"msg":"Field required","input":{"backend":"mock","prompt":"Hello"}}]}% 

5. To run both test in one command, you can run:

pytest

6. Before every commit, run:

ruff check .
black .
pytest




