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
            print("\nPodrías considerar estudiar ingeniería en sistemas computacionales.")
        else:
            self.declare(Fact(pregunta="ingenieria_bioquimica"))

    #   INGENIERIA EN QUIMICA
    @Rule(Fact(pregunta="ingenieria_bioquimica"))
    def ingenieria_bioquimica(self):
        respuesta = input("\n¿Te interesaría desarrollar y aplicar procesos, productos y "
                          "\ntecnologías relacionadas con organismos vivos y biomoléculas?  (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar estudiar ingeniería en quimica.")
        else:
            self.declare(Fact(pregunta="ingenieria_industrial"))

    #   INGENIERIA INDUSTRIAL
    @Rule(Fact(pregunta="ingenieria_industrial"))
    def ingenieria_industrial(self):
        respuesta = input("\n¿Te interesa el diseño, mejora y optimización de sistemas y procesos, "
                          "\ncon el objetivo de aumentar la eficiencia, la calidad, la productividad "
                          "\ny la rentabilidad en una amplia variedad de industrias y organizaciones?  (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar estudiar ingeniería industrial.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="ingenieria_mecanica"))

    #   INGENIERIA MECANICA
    @Rule(Fact(pregunta="ingenieria_mecanica"))
    def ingenieria_mecanica(self):
        respuesta = input("\n¿Te interesa el diseño, análisis, fabricación y "
                          "\nmantenimiento de sistemas y componentes mecánicos.?  (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar estudiar ingeniería mecanica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="ingenieria_mecatronica"))

    # INGENIERIA MECATRONICA
    @Rule(Fact(pregunta="ingenieria_mecatronica"))
    def ingenieria_mecatronica(self):
        respuesta = input("\n¿Te interesaría elementos de la ingeniería mecánica, la electrónica, la informática y "
                          "\nla automatización para diseñar y desarrollar sistemas y productos mecatrónicos?  (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar estudiar ingeniería mecatronica.")
            # self.declare(Fact(pregunta="ingenieria"))
        else:
            self.declare(Fact(pregunta="humanidades"))

    #   AREA HUMANIDADES
    @Rule(Fact(pregunta="humanidades"))
    def preguntar_humanidades(self):
        print("\nAREA HUMANIDADES")
        respuesta = input(
            "¿Te gustaría trabajar con disciplinas relacionadas con la cultura, la sociedad, la historia, el lenguaje, la filosofía, "
            "\nla literatura, las artes y otros aspectos de la experiencia humana? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="lic_historia"))
        else:
            self.declare(Fact(pregunta="negocios"))

    #   LICENCIATURA EN HISTORIA
    @Rule(Fact(pregunta="lic_historia"))
    def lic_historia(self):
        respuesta = input(
            "\n¿Te interesaría explorar eventos históricos, culturas, sociedades y tendencias, y desarrollar "
            "\nhabilidades de investigación, análisis y comunicación? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en historia.")
        else:
            self.declare(Fact(pregunta="lic_filosofia"))

    #   LICENCIATURA EN FILOSOFIA
    @Rule(Fact(pregunta="lic_filosofia"))
    def lic_filosofia(self):
        respuesta = input(
            "\n¿Te interesaría explorar cuestiones fundamentales sobre la existencia, el conocimiento, la moral, "
            "\nla lógica, la mente, la realidad y muchos otros temas abstractos? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en filosofía.")
        else:
            self.declare(Fact(pregunta="lic_sociologia"))

    #   LICENCIATURA EN SOCIOLOGIA
    @Rule(Fact(pregunta="lic_sociologia"))
    def lic_sociologia(self):
        respuesta = input("\n¿Te interesaría estudiar temas investigan cómo funcionan las sociedades, "
                          "\ncómo se desarrollan, cómo se organizan y cómo influyen en la vida de las personas? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en sociología.")
        else:
            self.declare(Fact(pregunta="lic_antropologia"))

    #   LICENCIATURA EN ANTROPOLOGIA
    @Rule(Fact(pregunta="lic_antropologia"))
    def lic_antropologia(self):
        respuesta = input("\n¿Te interesaria investigar y analizar sobre las culturas, las sociedades, la evolución "
                          "\nhumana, el comportamiento humano y las interacciones entre las personas y su entorno? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en antropología.")
        else:
            self.declare(Fact(pregunta="lic_comunicacion"))

    #   LICENCIATURA EN COMUNICACION
    @Rule(Fact(pregunta="lic_comunicacion"))
    def lic_comunicacion(self):
        respuesta = input("\n¿Te interesaria trabajar con los procesos de comunicación, la producción y difusión de "
                          "\ninformación, y la interacción entre individuos, grupos y organizaciones en contextos mediáticos y sociales? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en comunicación.")
        else:
            self.declare(Fact(pregunta="lic_educacion"))

    #   LICENCIATURA EN EDUCACION
    @Rule(Fact(pregunta="lic_educacion"))
    def lic_educacion(self):
        respuesta = input(
            "\n¿Te interesaría desempeñar roles en la dirección escolar, el diseño de currículos, la asesoría "
            "\neducativa, la formación de docentes y la investigación educativa? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una licenciatura en educación.")
        else:
            self.declare(Fact(pregunta="negocios"))

    #   AREA FINANZAS
    @Rule(Fact(pregunta="negocios"))
    def preguntar_negocios(self):
        print("\nAREA FINANZAS")
        respuesta = input("¿Te gustaría trabajar en un entorno de Negocios, Economía, "
                          "Estructura Socioeconómica de México y Contabilidad? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="admin_empresas"))
        else:
            self.declare(Fact(pregunta="salud"))

    #   ADMISNITRACIÓN DE EMPRESAS
    @Rule(Fact(pregunta="admin_empresas"))
    def admin_empresas(self):
        respuesta = input("\n¿Te interesaría gestionar y liderar organizaciones y empresas de manera efectiva? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Admnitración de empresas")
        else:
            self.declare(Fact(pregunta="finanzas"))

    #   FINANZAS
    @Rule(Fact(pregunta="finanzas"))
    def finanzas(self):
        respuesta = input(
            "\n¿Te interesaría centrarte en estudio y la gestión de los aspectos financieros de las organizaciones y las inversiones? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Finanzas")
        else:
            self.declare(Fact(pregunta="contabilidad"))

    #   CONTABILIDAD
    @Rule(Fact(pregunta="contabilidad"))
    def contabilidad(self):
        respuesta = input("\n¿Te interesaría centrarte en la recopilación, el registro, la interpretación y "
                          "\nel análisis de información financiera para ayudar a las organizaciones a tomar "
                          "\ndecisiones informadas sobre sus operaciones económicas? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Contabilidad")
        else:
            self.declare(Fact(pregunta="economia"))

    #   ECONOMÍA
    @Rule(Fact(pregunta="economia"))
    def economia(self):
        respuesta = input("\n¿Te interesaría centrarte centra en el estudio de cómo las sociedades asignan "
                          "\nrecursos escasos para satisfacer las necesidades y deseos humanos? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Economía")
        else:
            self.declare(Fact(pregunta="marketing"))

    #   MARKETING
    @Rule(Fact(pregunta="marketing"))
    def marketing(self):
        respuesta = input("\n¿Te interesaría enfocarte enfoca en el estudio y la aplicación de estrategias y "
                          "\ntécnicas para promover productos, servicios o ideas a un público objetivo con el "
                          "\nobjetivo de satisfacer las necesidades del mercado y generar valor para las empresas u organizaciones.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Marketing")
        else:
            self.declare(Fact(pregunta="comercio_int"))

    #   COMERCIO INTERNACIONAL
    @Rule(Fact(pregunta="comercio_int"))
    def comercio_int(self):
        respuesta = input("\n¿Te interesaría estudiar la gestión de las transacciones comerciales internacionales, "
                          "\nincluyendo la importación, exportación y distribución de bienes y servicios en un contexto global? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en Comercio Internacional")
        else:
            self.declare(Fact(pregunta="salud"))

    #   AREA SALUD
    @Rule(Fact(pregunta="salud"))
    def preguntar_salud(self):
        print("\nAREA SALUD")
        respuesta = input("¿Te gustaría trabajar en disciplinas dedicadas al mantenimiento, diagnóstico, tratamiento "
                          "\ny promoción del bienestar físico, mental y social de los individuos? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="medicina"))
            # ...
        else:
            self.declare(Fact(pregunta="artes"))

    #   MEDICINA
    @Rule(Fact(pregunta="medicina"))
    def medicina(self):
        respuesta = input("\n¿Te gustaria adquirir conocimientos y habilidades clínicas necesarios para "
                          "\ndiagnosticar, tratar y prevenir enfermedades, así como para cuidar y mejorar la salud de los pacientes.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en medicina")
        else:
            self.declare(Fact(pregunta="enfermeria"))

    #   ENFERMERIA
    @Rule(Fact(pregunta="enfermeria"))
    def enfermeria(self):
        respuesta = input("\n¿Te gustaria  desempeñar un papel fundamental en la atención de la salud, "
                          "\nbrindando cuidados compasivos, coordinando tratamientos, y promoviendo la "
                          "\nrecuperación y el bienestar de los pacientes en diversas áreas de la atención médica.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en enfermeria")
        else:
            self.declare(Fact(pregunta="fisioterapia"))

    #   FISIOTERAPIA
    @Rule(Fact(pregunta="fisioterapia"))
    def fisioterapia(self):
        respuesta = input("\n¿Te gustaria ser un experto en el manejo de técnicas terapéuticas y ejercicios"
                          "\n para rehabilitar y mejorar la movilidad, función y calidad de vida de los "
                          "\npacientes, abordando una variedad de condiciones médicas y lesiones.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en fisioterapia")
        else:
            self.declare(Fact(pregunta="psi_clinica"))

    #   PSICOLOGIA CLINICA
    @Rule(Fact(pregunta="psi_clinica"))
    def psi_clinica(self):
        respuesta = input("\n¿Te gustaria evaluar, diagnosticar y proporcionar tratamiento psicológico a "
                          "\nindividuos, utilizando enfoques terapéuticos para abordar aspectos emocionales "
                          "\ny mentales, y contribuyendo al bienestar mental y emocional de los pacientes.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en psicologia clinica")
        else:
            self.declare(Fact(pregunta="nutricion"))

    #   NUTRICION
    @Rule(Fact(pregunta="nutricion"))
    def nutricion(self):
        respuesta = input("\n¿Te interesaria estudiar una carrera que se centra en la interrelación entre la "
                          "\nalimentación y la salud mental, capacitando a los profesionales para comprender "
                          "\ny abordar las dimensiones psicológicas asociadas con los hábitos alimentarios, "
                          "\npromoviendo así un enfoque integral para la salud y el bienestar? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en nutricion")
        else:
            self.declare(Fact(pregunta="odontologia"))

    #   ODONTOLOGIA
    @Rule(Fact(pregunta="odontologia"))
    def odontologia(self):
        respuesta = input("\n¿T einteresaria profundizar en la comprensión de los aspectos psicológicos "
                          "\nrelacionados con la atención dental, capacitando a los profesionales para abordar "
                          "\nlas necesidades emocionales de los pacientes, promoviendo una experiencia "
                          "\nodontológica positiva y contribuyendo a la salud bucal integral.? (s/n): ")
        if respuesta.lower() == "s":
            print("Podrías considerar una carrera en odontologia")
        else:
            self.declare(Fact(pregunta="artes"))

    #   AREA ARTES
    @Rule(Fact(pregunta="artes"))
    def preguntar_artes(self):
        print("\nAREA ARTES")
        respuesta = input("¿Te gustaría estudiar alguna disciplina creativa que se centre en la expresión "
                          "\nartística y la comunicación visual? (s/n): ")
        if respuesta.lower() == "s":
            self.declare(Fact(pregunta="artes_visuales"))
        else:
            print("\nNecesitas explorar tus intereses con más detalle para obtener una recomendación precisa.")

    #   ARTES VISUALES
    @Rule(Fact(pregunta="artes_visuales"))
    def artes_visuales(self):
        respuesta = input("\n¿Te gustaría desembolverte en un disciplina artística que se centra en la creación "
                          "\nvisual y la expresión artística a través de diversas formas, como pintura, "
                          "\nescultura, grabado, fotografía y otras modalidades visuales.? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en artes visuales")
        else:
            self.declare(Fact(pregunta="interpretacion_musical"))

    #   INTERPRETACION MUSICAL
    @Rule(Fact(pregunta="interpretacion_musical"))
    def interpretacion_musical(self):
        respuesta = input("\n¿Te gustaría ser capacitado en la ejecución de instrumentos musicales o el canto, "
                          "\ncon un enfoque particular en la interpretación artística y la expresión musical? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en interpretacion musical")
        else:
            self.declare(Fact(pregunta="artes_digitales"))

    #   ARTES DIGITALES
    @Rule(Fact(pregunta="artes_digitales"))
    def artes_digitales(self):
        respuesta = input("\n¿Te gustaría explorar nuevas formas de expresión visual en el mundo digital? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en artes digitales")
        else:
            self.declare(Fact(pregunta="hist_arte"))

    #   HISTORIA DEL ARTE
    @Rule(Fact(pregunta="hist_arte"))
    def hist_arte(self):
        respuesta = input("\n¿Te gustaría enfocarte en el estudio y análisis de las manifestaciones artísticas a "
                          "\nlo largo de la historia, abarcando diversas culturas, estilos y períodos? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en historia del arte")
        else:
            self.declare(Fact(pregunta="arquitectura"))

    #   ARQUITECTURA
    @Rule(Fact(pregunta="arquitectura"))
    def arquitectura(self):
        respuesta = input("\n¿Te gustaría estudiar una disciplina que combina creatividad, diseño, tecnología y "
                          "\nconocimientos técnicos para planificar, diseñar y construir espacios arquitectónicos? (s/n): ")
        if respuesta.lower() == "s":
            print("\nPodrías considerar una carrera en arquitectura")
        else:
            print("\nNecesitas explorar tus intereses con más detalle para obtener una recomendación precisa.")


if __name__ == "__main__":
    engine = OrientacionVocacional()
    engine.reset()

    engine.declare(Fact(pregunta="ingenieria"))

    engine.run()
