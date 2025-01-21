import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
app = Flask(__name__)
if __name__ == '__main__':    # app.run(debug=True)
    app.run( debug=True)