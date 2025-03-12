from fastapi import FastAPI
from src.organization.routes import organization
from src.platform.routes import platform
from src.location.routes import location_router
from src.assets.routes import assets_router
from src.classification.routes import classification_router
from src.specialization.routes import specialization_router


app = FastAPI()


app.include_router(organization)
app.include_router(platform)
app.include_router(location_router)
app.include_router(assets_router)
app.include_router(classification_router)
app.include_router(specialization_router)