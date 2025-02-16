from flask import Flask
import Service.ScrapperService as ScrapperService
app = Flask(__name__)

ScrapperService.abrindoPagina()
ScrapperService.melhoresNotas()
print("-------------------------")
print("-------------------------")
ScrapperService.pioresNotas()

app.run()