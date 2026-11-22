# Ai-learning
# Create virtual environment
python -m venv venv

# Activate on Windows PowerShell
.\venv\Scripts\Activate.ps1

# install dependencies
python -m pip install -r requirements.txt


api_key = os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",

     model="openai/gpt-oss-120b",