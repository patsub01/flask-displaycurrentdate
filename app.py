from flask import Flask, render_template_string
import threading
import datetime

app = Flask(__name__)

@app.route('/')
def display_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%y")
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Date</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f0f0;
                margin: 0;
            }
            .container {
                text-align: center;
                background: white;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            
            <p>{{ current_date }}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, current_date=current_date)