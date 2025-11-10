from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastmcp import FastMCP

mcp = FastMCP("demo-mcp")
mcp_app = mcp.http_app(path='/mcp')

@mcp.tool
def add_nums(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Startup
    print("Starting up the app...")
    # Initialize database, cache, etc.
    yield
    # Shutdown
    print("Shutting down the app...")

# Combine both lifespans
@asynccontextmanager
async def combined_lifespan(app: FastAPI):
    # Run both lifespans
    async with app_lifespan(app):
        async with mcp_app.lifespan(app):
            yield

# Use the combined lifespan
app = FastAPI(lifespan=combined_lifespan)
app.mount("/llm", mcp_app)


@app.get("/", operation_id="read_root")
def read_root():
    return {"message": "hello world"}

