from uuid import UUID
from typing import List
from models import User, Gender, Roles, UpdateUser
from json_beautify import PrettyJSONResponse
from fastapi import FastAPI, HTTPException
app = FastAPI()

db: List[User] = [
    User(id=UUID("b8764374-828c-460e-8405-2903f8e1df5f"), first_name="Manish", last_name="Raina", gender=Gender.male, roles=[Roles.user]),
    User(id=UUID("552565fd-bd72-4ad3-bc86-0fd5e3537ee9"), first_name="Kalyani", last_name="Bodhankar", gender=Gender.female, roles=[Roles.admin])
]


@app.get("/", response_class=PrettyJSONResponse)
async def root():
    return {"Hello": "World"}


@app.get("/show_users", response_class=PrettyJSONResponse)
async def show_user():
    return db


@app.post("/show_users", response_class=PrettyJSONResponse, tags=["Register_User"])
async def register_user(user: User):
    db.append(user)
    response = {"id": user.id}
    return response


@app.delete("/delete_user/{delete_user_id}", response_class=PrettyJSONResponse, tags=["Delete_User"])
async def delete_user(delete_user_id: UUID):
    for user in db:
        if user.id == delete_user_id:
            db.remove(user)
            return {"Status": "User deleted successfully"}

        raise HTTPException(
            status_code=404,
            detail=f"User with user id: {delete_user_id} does not exist"
        )


@app.put("/show_users/{user_id}", tags=["Update_User"])
async def update_users(user_id: UUID, update_user: UpdateUser):
    for user in db:
        if user.id == user_id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if update_user.roles is not None:
                user.roles = update_user.roles
            return {"Status": f"User with user id {user_id} updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=F"User with user id {user_id} does not exist"
    )
