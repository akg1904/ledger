from flask_restful import Resource
from flask import request

from src.database.db.db_instance import DBInstance

conn = DBInstance().db


users = []
password = []






