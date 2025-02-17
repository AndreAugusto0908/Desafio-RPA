from flask import Flask
import Service.ScrapperService as ScrapperService
app = Flask(__name__)

ScrapperService.abrindoPagina()
ScrapperService.melhoresNotas()
print("Encerrado")
app.run()