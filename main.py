from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Marks dictionary
marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 15
}

@app.get("/api")
async def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}
