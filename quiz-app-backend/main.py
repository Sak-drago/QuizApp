from fastapi import FastAPI
from routes import user_routes, admin_routes

app = FastAPI()

app.include_router(user_routes.router, prefix="/users")
app.include_router(admin_routes.router, prefix="/admin")
