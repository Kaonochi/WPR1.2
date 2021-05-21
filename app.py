from flask import Flask, render_template, request, redirect, session
import datetime
import os

app = Flask(__name__)
directory = "."


@app.route("/")
def root():
    ls = os.listdir(directory)
    return str(ls)
