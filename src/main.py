"""
main.py

This module contains a FastAPI application with a simple endpoint.

Author: Your Name
Date: January 24, 2024
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """ Test function """
    return {"Hello": "World"}
