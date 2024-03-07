from extractor_openai.rea import Rea
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a la variable de entorno API_KEY
api_key = os.getenv('API_KEY')

rea = Rea(api_key)


objetivo = "Comprender colectivamente el proceso de transformación de significados sobre el buen vivir con un grupo de jóvenes del corregimiento de San Cristóbal que participan de un proceso de Investigación Acción Participativa y Educación popular que promueve el florecimiento humano"
metodologia = "1. METODOLOGÍA: LOS PRINCIPIOS DE LA IAP Enfoque: Investigación acción participativa con enfoque de educación popular e investigación temática. Como se ha mencionado en apartados anteriores, este proyecto recibe influencias de la educación popular, las epistemologías del sur, la investigación narrativa, la sistematización de experiencias y la Investigación Acción Participativa. Esta última es nuestra alternativa central, de ella retomamos sus principios de inserción, compromiso, y transformación social como forma de conocimiento, elementos claves para lograr los propósitos de este estudio. A continuación destacaremos algunos de los elementos que serán útiles para responder a la pregunta de investigación en el estudio. Iniciaremos presentando el concepto de praxis, el cual es entendido como la base de los principios que retomamos de la IAP, pues es este el modelo de investigación desde el que sustentamos todo el estudio, para continuar mostrando cómo funciona la investigación temática en círculos de cultura de la educación popular. Pasaremos a presentar el papel que juegan las historias de vida, así como las narrativas en este proceso, y posteriormente presentaremos dos componentes esenciales de esta investigación: la evaluación y la sistematización de experiencias como los dispositivos de reflexión que nos ayudarán a comprender cómo se construye conocimiento en este estudio. Investigación Acción Participativa: la investigación de la acción y la transformación. cuestiona las formaciones de lo que define como ciencia normal y plantea que el problema de las ciencias tradicionales con orientación positivista, es que buscan explicar los acontecimientos y fenómenos humanos desvelando sus propias lógicas y leyes, es decir, el conocimiento de los objetos en sí, y no para sí. El sociólogo colombiano propone una Sociología comprometida con la transformación social que denuncia las formas de construcción de conocimiento no interesado en la liberación y que promueve la construcción de conocimiento para el ejercicio del poder de las bases. Para Fals el problema de la praxis en el positivismo es que es vista como objeto de estudio o “como manipulación tecnológica y del control racional de los procesos naturales y sociales” , no es una categoría para el análisis, sino temática y de interés del investigador, lo cual hace que pierda capacidad y potencia revolucionaria. Esta cuestión se plantea problematizando la relación entre conocimiento y praxis. Para este autor la praxis es el fundamento único de la construcción del conocimiento crítico y pragmático; de ahí que no compare acción con conocimiento, pues hacen parte del mismo proceso para él. Así, sus bases conceptuales surgen de los planteamientos de Marx en las tesis sobre Feuerbach, considerando la noción dialéctica de praxis de Hegel, y la noción de frónesis aristotélica. , se refiere a la frónesis de la siguiente manera: “Se ha sentido la necesidad de fundar las vivencias no sólo en la praxis como viene dicho, sino en algo más allá, porque no es suficiente con llegar a ser un mero activista. Ello ha llevado a añadir al concepto marxista-hegeliano de praxis, otro de Aristóteles: el de “frónesis”. La frónesis debe suministrar la serenidad en procesos políticos participativos, debe ayudar a encontrar el justo medio y la proporción adecuada para las aspiraciones, y sopesar las relaciones hermenéuticas entre “corazón” y “corteza” que provee la técnica del Logos-Mythos” Pp:10 En esta perspectiva se plantea que en el mundo occidental, el conocimiento tradicionalmente se ha orientado más al sostenimiento del orden social y al control de las regiones que se han reconocido como del tercer mundo. , este conocimiento se define como formal, es producido por las élites, se superpone cuestionándolo y presentándolo anodino al conocimiento popular, aunque este último sea su origen y fundamento . Dicho conocimiento tiene tendencias conservadoras, lo que podría al decir de este autor, ser cuestionado y superado por la Investigación Acción Participativa el conocimiento tradicional se fundamenta en el odio y las diferenciaciones, requiere distinguir entre sujeto/objeto, elementos contrarios a los que propone la Investigación Acción Participativa –reconocida como un paradigma de las ciencias sociales por estos autores-, desde donde se produce un conocimiento en perspectiva de horizontalidad y solidaridad, reconociendo a todos (sujetos y objetos) como investigadores o personas sentipensantes; esto es: que tienen capacidad de sentir y pensar en el proceso de conocimiento y transformación . En esta nueva relación se buscan los puentes que articulen todas las formas de conocer (las de la academia y las del pensamiento popular), recibiendo cada una estatus similares, pero puestas al servicio de las personas y su dignidad en un sentido crítico. En esta línea teórica se entiende que no existe una sola forma de conocimiento, y que todas pueden ser cuestionables y requieren revisarse, incluyendo a las del saber popular evitando de esa forma una apología al populismo. Como lo afirman Fals y Rahman (2014, P: 270): “Los científicos instrumentales pueden así descubrir fórmulas que capaciten llegar a la luna; pero sus prioridades y valores personales les impiden resolver los sencillos problemas de la campesina que debe buscar cada día el agua para su casa. Lo primero es de interés del desarrollo técnico; lo segundo es expresión de inhumanidad e inequidad.” Retomando lo discutido, podríamos afirmar que la praxis es un concepto articulador de distintos tipos de conocimientos, remite también a la acción social transformadora, no diferencia entre hacer y conocer, y posibilita desarrollar una perspectiva crítica. Los conocimientos tratados así tienen un propósito emancipador (al decir de Hábermas), pero además se construyen de forma prudente, o desde lo que hemos definido como la frónesis, lo que los hace ver como acciones sociales reflexivas y los dota de una dimensión ética. La noción de praxis que más se acerca a nuestra forma de apreciarla, está planteada en el trabajo del educador popular , quien no diferencia entre hacer y reflexionar, sino que define a la praxis como la acción dinámica de actuar y reflexionar permanente desde los principios de su pedagogía crítica y problematizadora. La praxis desde este autor debería conducir a la concienciación, los temas generadores por su parte,"


entidad_obj = rea.extractor_obj(objetivo)
endidades_pob_tem = rea.extractor_pob_tem(objetivo)
endidades_met = rea.extractor_met(metodologia)

print(F"--> Este es el objetivo: {objetivo}\n")
print(F"--> Esta es la entidad de objeto: {entidad_obj}")
print(F"--> Esta es la entidades poblacion y tem: {endidades_pob_tem}\n")
# print(F"--> Metodología : {metodologia}")

print("Las entidades de metodología son")
print(endidades_met)
