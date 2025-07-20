from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract

app = FastAPI()

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        text = pytesseract.image_to_string(image)

        # Expecting format like: 12345678 * 87654321
        numbers = text.split("*")
        if len(numbers) != 2:
            return JSONResponse(status_code=400, content={"error": "Invalid format"})

        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
        result = num1 * num2

        return {
            "answer": result,
            "email": "23f3001760@ds.study.iitm.ac.in"
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
