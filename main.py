from experta import *


class OrientacionVocacional(KnowledgeEngine):
    @DefFacts()
    def hechos_iniciales(self):
        # Pregunta inicial
        yield Fact(pregunta="logico_matematico")

    #   AREA LOGICO-MATEMATICA
    @Rule(Fact(pregunta="logico_matematico"))
    def preguntar_ciencias(self):
        respuesta = input("¿Te gustan las matemáticas, física o la química? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="ingenieria_sistemas"))
        else:
            self.declare(Fact(pregunta="humanidades"))

    #   INGENIERIA EN SISTEMAS
    @Rule(Fact(pregunta="ingenieria_sistemas"))
    def area_ingenieria_sistemas(self):
        respuesta = input("\n¿Tienes interés en el diseño, desarrollo, implementación y gestión "
                          "\nde sistemas de información y tecnología de la información?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería en sistemas computacionales.")
        else:
            self.declare(Fact(pregunta="ingenieria_bioquimica"))

    #   INGENIERIA EN QUIMICA
    @Rule(Fact(pregunta="ingenieria_bioquimica"))
    def area_ingenieria_bioquimica(self):
        respuesta = input("¿Te interesaría desarrollar y aplicar procesos, productos y "
                          "\ntecnologías relacionadas con organismos vivos y biomoléculas?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería en quimica.")
        else:
            self.declare(Fact(pregunta="ingenieria_industrial"))

    #   INGENIERIA INDUSTRIAL
    @Rule(Fact(pregunta="ingenieria_industrial"))
    def area_ingenieria_industrial(self):
        respuesta = input("\n¿Te interesa el diseño, mejora y optimización de sistemas y procesos, "
                          "\ncon el objetivo de aumentar la eficiencia, la calidad, la productividad "
                          "\ny la rentabilidad en una amplia variedad de industrias y organizaciones?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería industrial.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="ingenieria_mecanica"))

    #   INGENIERIA MECANICA
    @Rule(Fact(pregunta="ingenieria_mecanica"))
    def area_ingenieria_mecanica(self):
        respuesta = input("\n¿Te interesa ?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería mecanica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="ingenieria_mecatronica"))

    #INGENIERIA MECATRONICA
    @Rule(Fact(pregunta="ingenieria_mecatronica"))
    def area_ingenieria_mecatronica(self):
        respuesta = input("\n¿?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería mecatronica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="humanidades"))

    #   AREA HUMANIDADES
    @Rule(Fact(pregunta="humanidades"))
    def preguntar_humanidades(self):
        respuesta = input("\n¿Te gustaría trabajar con personas? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en humanidades o servicios sociales.")
        else:
            self.declare(Fact(pregunta="negocios"))

    #   AREA FINANZAS
    @Rule(Fact(pregunta="negocios"))
    def preguntar_negocios(self):
        respuesta = input("\n¿Te gustaría trabajar en un entorno de Negocios, Economía, "
                          "Estructura Socioeconómica de México y Contabilidad? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
        else:
            self.declare(Fact(pregunta="salud"))

    #   AREA SALUD
    @Rule(Fact(pregunta="salud"))
    def preguntar_negocios(self):
        respuesta = input("\n¿Te gustaría ? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
            #...
        else:
            print("Necesitas explorar tus intereses con más detalle para obtener una recomendación precisa.")

if __name__ == "__main__":
    engine = OrientacionVocacional()
    engine.reset()

    engine.declare(Fact(pregunta="ingenieria"))

    engine.run()
