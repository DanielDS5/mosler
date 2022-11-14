import PyQt5

def asks(ask):
    while True:
        try:
            x = int(input(""+ask+" :"))
            if 1 <= x <=5:
                return x
            else:
                print("Debe ser un número entre 1 y 5")
        except:
            print("Debe ser un número")

    
def Criterion(ask1, ask2, ask3):
    return (asks(ask1) + asks(ask2) + asks(ask3))/3

def er(f, s, p, e, a, v):
    
    er = (f * s + p * e) * (a * v)
    print("Importancia del suceso: "+ f*s)
    print("Daños ocasionados: " + p*e)
    print("Carácter de riesgo: " + (f*s + p*e))
    print("Probabilidad: " + a*v)
    print("Riesgo considerado: " + er)
    
    if 2 < er < 250:
        return "Muy Bajo, Verde"
    elif 251 < er < 500:
        return "Pequeño, Amarillo"
    elif 501 < er < 750:
        return "Normal, Amarillo"
    elif 751 < er < 1000:
        return "Grande, Rojo"
    elif 1001 < er < 1250:
        return "Elevado, Rojo"

f = Criterion("1. Los daños a personal, ¿Cómo puede afectar?",
"2 .Los fallos en los sistemas, ¿Cómo puede afectar?",
"3. Los errores humanos, ¿Cómo puede afectar?")

s = Criterion("1. El sistema a sustituir, ¿se puede encontrar?",
"2. Los trabajos de sustitución, ¿serán rápidos?",
"3. La actividad en el área de trabajo, ¿continuará?")

p = Criterion("1. ¿Causan perturbaciones en el personal?",
"2. ¿Causan perturbaciones en los clientes?",
"3. ¿Causan perturbaciones en el sector de trabajo (ministerio)?")

e = Criterion("1. Los daños en la imagen de la entidad, ¿han sido?",
"2. Los daños económicos, ¿han sido?",
"3. Los daños en los bienes, ¿han sido?")
 
a = Criterion("1. ¿Hay una historia de eventos como el que está siendo evaluado o es este un evento aislado?",
"2. ¿Qué otro sistema o tipos de componentes similares pueden tener defectos similares?",
"3. ¿Cuál es la frecuencia de uso del sistema bajo evaluación?")

v = Criterion("1. ¿Los daños podrán evitarse con las medidas de seguridad existentes?",
"2. ¿Cuánto personal de mantenimiento debe trabajar con el sistema en cuestión?",
"3. ¿Las pérdidas de vidas están aseguradas?")

print(er(f, s, p, e, a, v))5
 