# AI-Finance-Assistant (Full Production)

Features:
- SMS parsing, transaction extraction
- ML-based transaction categorization (NLP)
- Expense forecasting (time-series)
- FastAPI backend with modular structure
- SQLite (default) + SQLAlchemy ORM
- Docker-ready

Quickstart:
1. cd backend
2. python -m venv venv
3. activate venv and `pip install -r requirements.txt`
4. Train models:
   - python app/ml/categorizer/train_categorizer.py
   - python app/ml/predictor/train_predictor.py
5. Run server:
   - uvicorn app.main:app --reload --port 8000

See `deployment/` for Docker config.

## Swagger Docs
![]("assets/AIscreenshot-1.png")
![]("assets/AIscreenshot-2.png")
![]("assets/AIscreenshot-3.png")




