from fastapi import APIRouter

router = APIRouter()


@router.get("/robots.txt")
async def read_robots():
    return {"message", "The robot.txt file will be displayed here"}


@router.get("/sitemap.xml.gz")
async def read_sitemap():
    return {"message", "The sitemap file for each marketplace will be displayed here"}
