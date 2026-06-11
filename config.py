import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# Gemini Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_MODEL = "gemini-3.5-flash"

TEMPERATURE = 0.2

# ==========================
# Groq Configuration
# ==========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"

TEMPERATURE = 0

MAX_TOKENS = None

MAX_RETRIES = 2

REQUEST_TIMEOUT = 60

# ==========================
# OpenAlex Configuration
# ==========================

OPENALEX_BASE_URL = "https://api.openalex.org/works"

DEFAULT_PAPER_LIMIT = 10

MAX_SEARCH_QUERIES = 10

# ==========================
# Ranking Configuration
# ==========================

TOP_K_PAPERS = 3

# ==========================
# Reflection Agent
# ==========================

CONFIDENCE_THRESHOLD = 0.75

# ==========================
# Report Configuration
# ==========================

REPORTS_DIR = "reports"

REPORT_FILE_NAME = "research_gap_report.pdf"