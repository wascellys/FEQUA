from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/v1/books",
    tags=["v1"]
)


# @router.get("/tools")
# def get_tools(title: str = None):
#     books = request.get_books(title=title)
#     if books:
#         return Response(json.dumps(books))
#     else:
#         raise HTTPException(status_code=404, detail="Book not found")