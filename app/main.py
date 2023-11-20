from fastapi import FastAPI
from .routers import posts, users, auth, vote
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {
        "Greetings": "Hello World!",
        "me": "Jeeva",
        "app_name": "Posts-APIs",
        "message": "Welcome to Posts-APIs! This is the home page for our sample API endpoints built with FastAPI.",
        "description": "Our API allows you to create, read, modify, delete, and vote on posts. For detailed documentation, please visit our API documentation page.",
        "urls": {
            "on_heroku": "https://fastapi-posts-endpoints-jeeva-ca5c7ab434e2.herokuapp.com/docs",
            "on_virtualmachine": {
                "root": "https://www.fastapi-blog-jeeva.xyz",
                "docs": "https://www.fastapi-blog-jeeva.xyz/docs/",
            },
        },
    }
