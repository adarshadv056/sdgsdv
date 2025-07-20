from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    try:
        # Load the uploaded image
        image = Image.open(file.file)

        # Use OCR to extract text
        text = pytesseract.image_to_string(image)

        # Expecting format like: "12345678 * 87654321"
        parts = [int(s.strip()) for s in text.split('*')]
        if len(parts) == 2:
            result = parts[0] * parts[1]
        else:
            return JSONResponse(status_code=400, content={"error": "Could not detect proper multiplication format."})

        return {
            "answer": result,
            "email": "23f3001760@ds.study.iitm.ac.in"
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
