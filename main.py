import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from animation import get_graph_animation, get_bar_plot_animation

# Define the FastAPI server
app = FastAPI(title="FastAPI App with Embedded Draggable Plotly Graphs")

# assets and templates folder
templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Mount the Dash app as a sub-application in the FastAPI server
# app.mount("/dash", WSGIMiddleware(dash_app.server))

# Render Template with embedded Plotly Graph
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    fig = get_graph_animation()
    fig2 = get_bar_plot_animation()
    return templates.TemplateResponse("interact.html", {"request": request, "fig_json": fig, "fig2_json": fig2 })


# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)