# -*- coding: utf-8 -*-
from flask import Flask, render_template
import scrapy

app = Flask(__name__)

class OverwatchItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)