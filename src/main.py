"""
main.py

This module contains a FastAPI application with a simple endpoint.

Author: Your Name
Date: January 24, 2024
"""

from fastapi import FastAPI
from os import getenv
import uvicorn

class App:
    '''The main app Function for FastAPI'''
    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/")
        def read_root():
            """Test function"""
            return {"Hello": "World"}

    def run(self):
        '''Test run funtion'''
        uvicorn.run(self.app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    app = App()
    app.run()
