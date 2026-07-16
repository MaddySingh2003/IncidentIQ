from fastapi import APIRouter, UploadFile, File
from app.ml.parser import parse_log

router = APIRouter(prefix="/logs", tags=["logs"])


@router.post("/upload")
async def upload_logs(file: UploadFile = File(...)):


    content=await file.read()

    lines = content.decode("utf-8").splitlines()

    parsed_logs = []

    failed=[]
    for line in lines:
        print(repr(line))

        result = parse_log(line)
        if result:
            parsed_logs.append(result)
        else:
            failed.append(line)
        
    return {
        "parsed":len(parsed_logs),
        "failed":len(failed),
        "preview":parsed_logs[:5],

    }

