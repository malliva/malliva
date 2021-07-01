from fastapi import APIRouter

router = APIRouter()


@router.get("/robot.txt")
async def read_robottxt():
    return {"message", "The robot.txt file will be displayed here"}


@router.get("/sitemap.xml.gz")
async def read_robottxt():
    return {"message", "The sitemap file for each marketplace will be displayed here"}
