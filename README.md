# RepIt

RepIt is an experimental AI “class representative” that uses Google Gemini tool-calling to answer questions and trigger helper functions like class scheduling, canceling, polling, and quiz creation. The codebase currently contains a simple CLI loop plus several service stubs for future integrations (MongoDB, PostgreSQL, Excel-based schedules).

## Quick start
- Python 3.11+ recommended.
- Create and activate a virtual environment, then install the deps (rough set):
	```bash
	pip install google-genai google-auth-httplib2 google-api-python-client pymongo psycopg2-binary python-dotenv pandas openpyxl
	```
- Set your Gemini API key (the repo currently contains placeholder keys that should be removed):
	```bash
	set GEMINI_API_KEY=your-key-here   # Windows PowerShell: $env:GEMINI_API_KEY="your-key-here"
	```
- Run the CLI demo (note: `core/ai_client.py` still needs a `GeminiClient` implementation for this to work):
	```bash
	python main.py
	```

## Project layout
- [main.py](main.py) – CLI loop that prompts the user and calls `RepItAgent`.
- [core/agents.py](core/agents.py) – `RepItAgent` orchestrates prompt construction and routes Gemini function calls vs. text.
- [core/tools.py](core/tools.py) – Tool schema definitions (CheckUser, CancelClass, SceduleClass, ShowSchedule, ShowClassForToday, MakeQuiz, MakePoll).
- [core/ai_client.py](core/ai_client.py) – Placeholder Gemini client script; missing the `GeminiClient` class expected by `main.py`.
- [services/scedule_service.py](services/scedule_service.py) – String-format stubs for scheduling/canceling/showing classes.
- [services/poll_service.py](services/poll_service.py) – Empty stub for poll creation.
- [rule.py](rule.py) – Hard-coded role lookup for Admin/Teacher/Student.
- [db.py](db.py) – MongoDB helper stub (hard-coded URI; `read` not yet implemented).
- [supa.py](supa.py) – Example PostgreSQL connection using `.env` variables.
- [scedule.py](scedule.py) – Reads `Book1.xlsx` into a DataFrame; prints schedule data.
- [ai.py](ai.py) and [agent.py](agent.py) – Earlier prototypes of the Gemini interaction loop.

## How it works (intended)
1. `main.py` builds a context with today’s date/day and instantiates `RepItAgent` with an AI client plus the tool schema.
2. User input is sent to Gemini with tool definitions; responses are split into plain text vs. function calls.
3. Function calls are currently just printed; wiring to real services (e.g., `services/` functions or DB calls) is pending.

## Configuration
- `GEMINI_API_KEY` must be set for any Gemini calls. Remove hard-coded keys from the codebase before deploying.
- Database examples:
	- Mongo: replace the connection string in [db.py](db.py) with `MONGO_URI` from env, and implement `read`/queries.
	- Postgres: supply `user`, `password`, `host`, `port`, `dbname` in a `.env` file for [supa.py](supa.py).
- If you rely on Excel schedules, keep `Book1.xlsx` in the project root for [scedule.py](scedule.py).

## Caveats / TODO
- Implement `GeminiClient` in [core/ai_client.py](core/ai_client.py) and replace hard-coded API keys with env-based config.
- Wire tool calls to `services/` implementations and expand them beyond string responses.
- Add error handling, logging, and tests.
- Add a `requirements.txt` or `pyproject.toml` to lock dependencies.
