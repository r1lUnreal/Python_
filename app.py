from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def main():
    return """
<h1>Hello</h1>
<p>Илюша 16 годиков =) В.С.Ё</p>
<img style="text-align:center" src="https://www.seekpng.com/png/detail/893-8937263_hug.png">
<a src="youtube.com">
"""

app.run()