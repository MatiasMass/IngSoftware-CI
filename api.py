

from fastapi import HTTPException, status, APIRouter

router = APIRouter()

list_of_products = [
    {
        "id": 1,
        "name": "Product 1",
        "description": "This is the description for product 1",
        "price": 100,
        "image": "https://picsum.photos/200/300"
    },
    {
        "id": 2,
        "name": "Product 2",
        "description": "This is the description for product 2",
        "price": 200,
        "image": "https://picsum.photos/200/300"
    },
]

@router.get("/", status_code=status.HTTP_200_OK)
def get_products():
   
    return {"Status": "Success", "Results": len(list_of_products), "Products": list_of_products}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_product(id: str):
    product = None
    if id.isalpha():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No Product with this id: `{id}` found",
        )
    else:
        id = int(id.strip())
        for item in list_of_products:
            if item["id"] == id:
                product = item
                break
        if product == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No Product with this id: `{id}` found",
            )
    
        return {"Status": "Success", "Product": product}
   
