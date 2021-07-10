from dbConnectionManager.database_resolver import get_db_name
from fastapi import FastAPI, Request, APIRouter, status
from fastapi.params import Path
from fastapi.responses import JSONResponse

router = APIRouter()

# read files


@router.get("/{file_path:path}")
async def read_files(request: Request, file_path: str):
    await get_db_name(request)
    try:
        return {"file_path": file_path}
    except:
        return JSONResponse(content="This route has not been setup yet, check back later", status_code=status.HTTP_306_RESERVED)
