import requests
import socket
from flask_restful import Resource
from flask import request
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


class RutaClientes(Resource):
    @jwt_required()
    def get(self, id_repartidor):
        hostIp = socket.gethostbyname(socket.gethostname())
        if id_repartidor == 1:
            response = {
                "HTTPCode": 200,
                "IP": hostIp,
                "RutaEntrega": {
                    "Cliente1": "Tienda de Pedro",
                    "Direccion1": "Santa Fe, Bogota",
                    "Cliente2": "Tienda de Juan",
                    "Direccion2": "Santa Teresa, Bogota",
                    "Cliente3": "Tienda de Felipe",
                    "Direccion3": "Kennedy, Bogota",
                    "Cliente4": "Tienda de Pedro",
                    "Direccion4": "Puente Aranda, Bogota",
                },
            }
        else:
            response = {
                "HTTPCode": 409,
                "IP": hostIp,
            }

        return response

app = Flask(__name__)
cors = CORS(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)


app_context = app.app_context()
app_context.push()
api = Api(app)

# Agregamos el recurso que expone la funcionalidad ventas
api.add_resource(RutaClientes, "/cpp/RutaClientes/<int:id_repartidor>")

# Agregamos el recurso que expone la funcionalidad ventas
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
