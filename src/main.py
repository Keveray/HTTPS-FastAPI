
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Arc Warden</title>
    </head>
    <body>
        <img src="https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/arc_warden.png"
             alt="Arc Warden">
        <p>Это лучший герой 2</p>
    </body>
    </html>
    """
