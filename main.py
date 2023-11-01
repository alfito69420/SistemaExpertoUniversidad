from experta import *


class OrientacionVocacional(KnowledgeEngine):
    @DefFacts()
    def hechos_iniciales(self):
        # Pregunta inicial
        yield Fact(pregunta="ingenieria")

    @Rule(Fact(pregunta="ingenieria"))
    def preguntar_ciencias(self):
        respuesta = input("¿Te gustan las matemáticas? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en ciencias o ingeniería.")
        else:
            self.declare(Fact(pregunta="humanidades"))

    @Rule(Fact(pregunta="humanidades"))
    def preguntar_humanidades(self):
        respuesta = input("¿Te gustaría trabajar con personas? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en humanidades o servicios sociales.")
        else:
            self.declare(Fact(pregunta="negocios"))

    @Rule(Fact(pregunta="negocios"))
    def preguntar_negocios(self):
        respuesta = input("¿Te gustaría trabajar en un entorno de negocios? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
        else:
            print("Necesitas explorar tus intereses con más detalle para obtener una recomendación precisa.")


if __name__ == "__main__":
    engine = OrientacionVocacional()
    engine.reset()

    engine.declare(Fact(pregunta="ingenieria"))

    engine.run()
