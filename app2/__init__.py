from flask import Flask, render_template, redirect, url_for, request
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app2 import routes
