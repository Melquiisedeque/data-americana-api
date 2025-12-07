from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_current_date():
    """
    Retorna a data atual no formato americano YYYY-MM-DD
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    return {"date": current_date}
