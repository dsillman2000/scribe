from io import BytesIO
from pathlib import Path
from random import randint, seed
from typing import Literal

from exercises import rhythm_exercise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


ROOT_DIR = Path(__file__).parent
FILES_DIR = ROOT_DIR / "files"
EXERCISES = {"rhythm"}


@app.get("/api/beep")
async def get_beep_audio(format: Literal["mp3", "wav"] = "wav"):

    if format not in ["mp3", "wav"]:
        return JSONResponse(status_code=400, content={"error": "Invalid format"})

    base_name: str = f"beep-07a.{format}"
    file_path: Path = Path(FILES_DIR / base_name)

    if not file_path.exists():
        return JSONResponse(status_code=404, content={"error": "File not found"})

    return FileResponse(file_path, media_type=f"audio/{format}")


@app.get("/exercises/{exercise_id}/{exercise_seed}")
async def get_exercise_audio(exercise_id: str, exercise_seed: str, bpm: int = 120, count_in: int = 4):

    if exercise_id not in EXERCISES:
        return JSONResponse(status_code=404, content={"error": "Exercise not found"})

    int_exercise_seed: int = int(exercise_seed)
    if exercise_id == "rhythm":
        return StreamingResponse(BytesIO(rhythm_exercise(int_exercise_seed, bpm, count_in)), media_type="audio/wav")


# app.mount("/", StaticFiles(directory=ROOT_DIR / "frontend" / "public", html=True), name="static")
app.mount("/", StaticFiles(directory=FILES_DIR, html=False), name="static")
