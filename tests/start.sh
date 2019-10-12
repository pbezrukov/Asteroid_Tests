#!/bin/bash
pytest --alluredir=result
allure serve result/ -p 5000