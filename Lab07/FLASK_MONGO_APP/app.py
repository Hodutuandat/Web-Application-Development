from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask (__name__)

client = MongoClient ("mongodb://localhost:27017/")
db = client ["student_db"]
collection = db["students"]