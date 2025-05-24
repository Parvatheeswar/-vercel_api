from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Sample marks data
marks = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40
}

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks.get(n, 0) for n in name]
    return {"marks": result}
