from fastapi import APIRouter, UploadFile, File
router = APIRouter(prefix="/logs", tags=["logs"])

@router.post("/upload")
async def upload_logs(file: UploadFile = File(...)):
    content = await file.read()
    lines = content.decode("utf-8").splitlines()


    return {
        "filename": file.filename,
        "total_lines": len(lines),
        "preview":lines[:5]
    }