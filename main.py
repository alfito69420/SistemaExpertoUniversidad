from experta import *


class OrientacionVocacional(KnowledgeEngine):
    @DefFacts()
    def hechos_iniciales(self):
        # Pregunta inicial
        yield Fact(pregunta="logico_matematico")

    #   AREA LOGICO-MATEMATICA
    @Rule(Fact(pregunta="logico_matematico"))
    def preguntar_ciencias(self):
        print("AREA LÓGICO-MATEMÁTICA")
        respuesta = input("¿Te gustan las matemáticas, física o la química? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="ingenieria_sistemas"))
        else:
            self.declare(Fact(pregunta="humanidades"))

    #   INGENIERIA EN SISTEMAS
    @Rule(Fact(pregunta="ingenieria_sistemas"))
    def ingenieria_sistemas(self):
        respuesta = input("\n¿Tienes interés en el diseño, desarrollo, implementación y gestión "
                          "\nde sistemas de información y tecnología de la información?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería en sistemas computacionales.")
        else:
            self.declare(Fact(pregunta="ingenieria_bioquimica"))

    #   INGENIERIA EN QUIMICA
    @Rule(Fact(pregunta="ingenieria_bioquimica"))
    def ingenieria_bioquimica(self):
        respuesta = input("\n¿Te interesaría desarrollar y aplicar procesos, productos y "
                          "\ntecnologías relacionadas con organismos vivos y biomoléculas?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería en quimica.")
        else:
            self.declare(Fact(pregunta="ingenieria_industrial"))

    #   INGENIERIA INDUSTRIAL
    @Rule(Fact(pregunta="ingenieria_industrial"))
    def ingenieria_industrial(self):
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
    def ingenieria_mecanica(self):
        respuesta = input("\n¿Te interesa el diseño, análisis, fabricación y "
                          "\nmantenimiento de sistemas y componentes mecánicos.?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería mecanica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="ingenieria_mecatronica"))

    # INGENIERIA MECATRONICA
    @Rule(Fact(pregunta="ingenieria_mecatronica"))
    def ingenieria_mecatronica(self):
        respuesta = input("\n¿Te interesaría elementos de la ingeniería "
                          "\nmecánica, la electrónica, la informática y "
                          "\nla automatización para diseñar y desarrollar sistemas y productos mecatrónicos?  (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar estudiar ingeniería mecatronica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="humanidades"))

    #   AREA HUMANIDADES
    @Rule(Fact(pregunta="humanidades"))
    def preguntar_humanidades(self):
        print("\nAREA HUMANIDADES")
        respuesta = input("¿Te gustaría trabajar con disciplinas relacionadas con "
                          "\nla cultura, la sociedad, la historia, el lenguaje, la filosofía, "
                          "\nla literatura, las artes y otros aspectos de la experiencia humana? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="lic_historia"))
        else:
            self.declare(Fact(pregunta="negocios"))

    #   LICENCIATURA EN HISTORIA
    @Rule(Fact(pregunta="lic_historia"))
    def lic_historia(self):
        respuesta = input("\n¿Te interesaría explorar eventos históricos, "
                          "\nculturas, sociedades y tendencias, y desarrollar "
                          "\nhabilidades de investigación, análisis y comunicación? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en historia.")
        else:
            self.declare(Fact(pregunta="lic_filosofia"))

    #   LICENCIATURA EN FILOSOFIA
    @Rule(Fact(pregunta="lic_filosofia"))
    def lic_filosofia(self):
        respuesta = input("\n¿Te interesaría explorar cuestiones fundamentales "
                          "\nsobre la existencia, el conocimiento, la moral, "
                          "\nla lógica, la mente, la realidad y muchos otros temas abstractos? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en filosofía.")
        else:
            self.declare(Fact(pregunta="lic_sociologia"))

    #   LICENCIATURA EN SOCIOLOGIA
    @Rule(Fact(pregunta="lic_sociologia"))
    def lic_sociologia(self):
        respuesta = input("\n¿Te interesaría estudiar temas investigan cómo funcionan "
                          "\nlas sociedades, cómo se desarrollan, cómo se organizan "
                          "\ny cómo influyen en la vida de las personas? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en sociología.")
        else:
            self.declare(Fact(pregunta="lic_antropologia"))

    #   LICENCIATURA EN ANTROPOLOGIA
    @Rule(Fact(pregunta="lic_antropologia"))
    def lic_antropologia(self):
        respuesta = input("\n¿T einteresaria investigar y analizar sobre las culturas, "
                          "\nlas sociedades, la evolución humana, el comportamiento humano"
                          "\n y las interacciones entre las personas y su entorno? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en antropología.")
        else:
            self.declare(Fact(pregunta="lic_comunicacion"))

    #   LICENCIATURA EN COMUNICACION
    @Rule(Fact(pregunta="lic_comunicacion"))
    def lic_comunicacion(self):
        respuesta = input("\n¿Te interesaria trabajar con los procesos "
                          "\nde comunicación, la producción y difusión de "
                          "\ninformación, y la interacción entre individuos, "
                          "\ngrupos y organizaciones en contextos mediáticos y sociales? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en comunicación.")
        else:
            self.declare(Fact(pregunta="lic_educacion"))

    #   LICENCIATURA EN EDUCACION
    @Rule(Fact(pregunta="lic_educacion"))
    def lic_educacion(self):
        respuesta = input("\n¿Te interesaría desempeñar roles en la dirección "
                          "\nescolar, el diseño de currículos, la asesoría "
                          "\neducativa, la formación de docentes y la investigación educativa? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una licenciatura en educación.")
        else:
            self.declare(Fact(pregunta="negocios"))

    #   AREA FINANZAS
    @Rule(Fact(pregunta="negocios"))
    def preguntar_negocios(self):
        print("\nAREA FINANZAS")
        respuesta = input("¿Te gustaría trabajar en un entorno de Negocios, Economía, "
                          "Estructura Socioeconómica de México y Contabilidad? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
        else:
            self.declare(Fact(pregunta="salud"))

    #   AREA SALUD
    @Rule(Fact(pregunta="salud"))
    def preguntar_salud(self):
        print("\nAREA SALUD")
        respuesta = input("¿Te gustaría ? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
            # ...
        else:
            self.declare(Fact(pregunta="artes"))

    #   AREA ARTES

    @Rule(Fact(pregunta="artes"))
    def preguntar_artes(self):
        print("\nAREA ARTES")
        respuesta = input("¿Te gustaría ? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en negocios o administración.")
            # ...
        else:
            print("Necesitas explorar tus intereses con más detalle para obtener una recomendación precisa.")


if __name__ == "__main__":
    engine = OrientacionVocacional()
    engine.reset()

    engine.declare(Fact(pregunta="ingenieria"))

    engine.run()
