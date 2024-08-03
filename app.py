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
                justify-content:bottom;
                align-items: bottom;
                height: 100vh;
                background-color: yellow;
                margin: 0;

                font-family: 'Arial', sans-serif;
                background-color: grey;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .certificate {
                border: 10px solid #3a3a3a;
                padding: 50px;
                background: MediumSeaGreen;
                width: 800px;
                text-align: center;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            }
            .certificate h1 {
                font-size: 50px;
                margin: 0;
                color: yellow;
            }
            .certificate h2 {
                font-size: 30px;
                margin: 20px 0;
                color: yellow;
            }
            .certificate p {
                font-size: 20px;
                margin: 10px 0;
                color: yellow;
            }
            .certificate .recipient {
                font-size: 25px;
                margin: 20px 0;
                font-weight: bold;
                color: yellow;
            }
            .certificate .date {
                margin-top: 30px;
                font-size: 18px;
                color: yellow;
            }
            .certificate .logo {
                margin: 0;
                padding: 0;
                float: left;
                width: 50px;
            
            .container {
                text-align: bottom;       
                padding: 20px;
                color: yellow;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
        <div class="certificate">
        <img src="./static/images/MyLogo.png" alt="Logo" class="logo">
    	<h1>Deployment in Render</>
        <p>As Web Service</p>
        <h2>Deploy code in Github</h2>
        <h2>Deploy in Render</h2>
    	<h2>Share the generated URL with friends and relatives</h2>        
            <h2>{{ current_date }}</h2>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, current_date=current_date)