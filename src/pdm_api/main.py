
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def _root(): return {'ok': True}
