def index_html():
    return """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cat's Door</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>Home</h1>
        <a href="on.html"><button id="on-button">ON</button></a>
        <br>
        <a href="off.html"><button id="off-button">OFF</button></a>
    </body>
    </html>"""


def on_html():
    return """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cat's Door</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>ON html</h1>
        <a href="off.html"><button id="off-button">OFF</button></a>
    </body>
    </html>"""


def off_html():
    return """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cat's Door</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>OFF html</h1>
        <a href="on.html"><button id="on-button">ON</button></a>
    </body>
    </html>"""
