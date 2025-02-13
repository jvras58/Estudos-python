import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.task.router import router as task_router

app = FastAPI()

# ----------------------------------
#  APP CORSMiddleware
# ----------------------------------
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# ----------------------------------
#   APP ROUTERS
# ----------------------------------
app.include_router(task_router, prefix='/task', tags=['task'])
# ----------------------------------


@app.get('/')
def read_root():
    return {'message': 'Wellcome to API!'}


# ==========================================================================
# FastAPI Start
# ==========================================================================
if __name__ == '__main__':
    uvicorn.run("src.main:app", host='0.0.0.0', port=8000, reload=True)    
