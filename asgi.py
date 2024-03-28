import uvicorn
from main import create_app

import settings

api = create_app(settings)

if __name__=="__main__":
    uvicorn.run("asgi:api",host="0.0.0.0",port=8080,reload=True)