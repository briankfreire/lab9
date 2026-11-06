from flask import Flask

# Inicializa a aplicação Flask
app = Flask(__name__)


# Define a rota principal ("/")
@app.route("/")
def hello_world():
  return "<h1>Hello, World!</h1><p>Minha primeira aplicação Flask no PyCharm!</p>"


# Executa o servidor de desenvolvimento
if __name__ == "__main__":
  app.run(debug=True)