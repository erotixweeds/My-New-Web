from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from auth import router as auth_router
from generator import router as gen_router
from admin import router as admin_router
from referral import router as referral_router
from analytics import router as analytics_router

app = FastAPI()

# CORS (safe for test)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
app.include_router(auth_router)
app.include_router(gen_router)
app.include_router(admin_router)
app.include_router(referral_router)
app.include_router(analytics_router)

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.get("/{page}")
def pages(page: str):
    return FileResponse(f"frontend/{page}.html")
