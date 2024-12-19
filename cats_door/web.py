def index_html():
    return """<!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Arduino Cat Door</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <button id="led-on" class="button">Turn LED ON</button>
        <button id="led-off" class="button red">Turn LED OFF</button>
        <button id="option1" class="button">Option 1</button>
        <button id="option2" class="button">Option 2</button>
        <script src="script.js"></script>
    </body>
    </html>"""
