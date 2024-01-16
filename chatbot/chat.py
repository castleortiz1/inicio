import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

import rasa
from rasa.core.agent import Agent

# Cargar las reglas
rules = [
    rasa.shared.core.policies.RulePolicy.from_file("rules.yml"),
    rasa.shared.core.policies.FallbackPolicy.from_file("fallback.yml"),
    rasa.shared.core.policies.MemoizationPolicy(),
]

# Entrenar el modelo
agent = Agent.load("model", policies=rules)

# Iniciar el chatbot
while True:
    # Obtener la entrada del usuario
    mensaje_usuario = input("Introduce tu mensaje: ")

    # Preprocesar el mensaje
    mensaje_usuario = mensaje_usuario.lower()
    mensaje_usuario = mensaje_usuario.replace(".", "")
    mensaje_usuario = mensaje_usuario.replace(",", "")
    mensaje_usuario = mensaje_usuario.replace("!", "")
    mensaje_usuario = mensaje_usuario.replace("?", "")

    # Tokenizar el mensaje
    tokens = word_tokenize(mensaje_usuario)

    # Eliminar las palabras vacías
    stop_words = set(stopwords.words("spanish"))
    tokens = [token for token in tokens if token not in stop_words]

    # Analizar el mensaje
    doc = nlp(" ".join(tokens))

    # Obtener la predicción del modelo
    respuesta = agent.handle_text(mensaje_usuario)

    # Mostrar la respuesta
    print("Chatbot:", respuesta[0]["text"])

