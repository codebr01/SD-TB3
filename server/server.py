import os
import uvicorn
import sqlite3
from datetime import datetime
from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from libs.processing import apply_denoise_filter
import uuid
from fastapi.responses import FileResponse

db_path = "../db/images.db"
images_dir = Path("./images/original").resolve()
save_processed_dir = Path("./images/processed").resolve()
os.makedirs(images_dir, exist_ok=True)
os.makedirs(save_processed_dir, exist_ok=True)

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    timestamp = datetime.now()
    date = timestamp.strftime("%Y-%m-%d")
    time = timestamp.strftime("%H-%M-%S")
    original_path = str(images_dir / file.filename)
    
    with open(original_path, "wb") as f:
        f.write(file.file.read())
    
    processed_path = apply_denoise_filter(original_path, save_processed_dir)
    image_id = str(uuid.uuid1())
    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO images (id, date, time, original_path, processed_path) VALUES (?, ?, ?, ?, ?)",
              (image_id, date, time, original_path, processed_path))
    conn.commit()
    conn.close()
    
    return {"id": image_id, "date": date, "time": time, "original": original_path, "processed": processed_path}

@app.get("/image/{image_id}")
async def get_image(image_id: str):
    # Query the database to get the image paths
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT original_path, processed_path FROM images WHERE id = ?", (image_id,))
    result = c.fetchone()
    conn.close()
    
    if result:
        original_path, processed_path = result
        # Resolver o caminho absoluto para garantir que as imagens sejam localizadas corretamente
        original_path = Path(original_path).resolve()
        processed_path = Path(processed_path).resolve()

        # Verificar se os arquivos existem antes de retornar
        if original_path.exists() and processed_path.exists():
            return {
                "original": str(original_path),
                "processed": str(processed_path)
            }
        else:
            return {"error": "Image files not found"}
    else:
        return {"error": "Image not found"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
