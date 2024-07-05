from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os, requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")