from fastapi import APIRouter, UploadFile, File
from app.ml.parser import parse_log
from app.services.log_service import LogService

router = APIRouter(tags=["Logs"])

@router.post("/incidents/{incident_id}/logs")
async def upload_logs(
    incident_id: str,
    file: UploadFile = File(...)
):

    content = await file.read()

    lines = content.decode("utf-8").splitlines()

    parsed_logs = []
    failed = []

    for line in lines:

        parsed = parse_log(line)

        if parsed:
            parsed_logs.append(parsed)
        else:
            failed.append(line)

    saved = await LogService.save_logs(
        incident_id,
        parsed_logs
    )

    return {
        "saved": saved,
        "failed": len(failed)
    }