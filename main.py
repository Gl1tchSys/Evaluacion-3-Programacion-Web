from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)
registros = []
contador_registros = 0


#Menu principal

@app.route("/")
def inicio():
    return render_template("index.html")

#Historial de actividades

@app.route("/historial")
def historial():
    return render_template(
        "historial.html",
        registros=registros
    )

#Eliminar los registros del historial

@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar_registro(id):

    for registro in registros:
        if registro["id"] == id:
            registros.remove(registro)
            break

    return redirect("/historial")


#Menú con URL de los ejercicios, para la selección de ellos

@app.route("/ejercicio/<int:numero>")
def seleccionar_ejercicio(numero):

    if numero == 1:
        return redirect("/ejercicio1")

    elif numero == 2:
        return redirect("/ejercicio2")

    else:
        abort(404)



#Ejercicio 1: Notas y asistencias

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":

        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        #Verificacion adicional de los valores ingresados para evitar errores
        if (nota1 < 10 or nota1 > 70 or
            nota2 < 10 or nota2 > 70 or
            nota3 < 10 or nota3 > 70 or
            asistencia < 0 or asistencia > 100):

            resultado = "Error: Valores fuera de rango. Intente de nuevo."
            promedio = None

        else:
            promedio = round((nota1 + nota2 + nota3) / 3, 2)

            if promedio >= 40 and asistencia >= 75:
                resultado = "¡APROBADO!"
            else:
                resultado = "REPROBADO"

        #Guardado de registro
        global contador_registros

        if promedio is not None:
            registros.append({
                "id": contador_registros,
                "ejercicio": "Notas y asistencia",
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3,
                "asistencia": asistencia,
                "promedio": promedio,
                "resultado": resultado
            })

            contador_registros += 1

        return render_template(
            "ejercicio1.html",
            promedio=promedio,
            resultado=resultado,
            asistencia=asistencia
        )

    return render_template("ejercicio1.html")

# Ejercicio 2: Comparación de caracteres de nombres

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    if request.method == "POST":

        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        # Verificación de nombres diferentes
        nombres = [
            nombre1.casefold(),
            nombre2.casefold(),
            nombre3.casefold()
        ]

        if len(set(nombres)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Error: Debe ingresar nombres diferentes."
            )

        cantidad1 = len(nombre1)
        cantidad2 = len(nombre2)
        cantidad3 = len(nombre3)

        # Comparación de nombres según cada caso
        if cantidad1 == cantidad2 == cantidad3:

            nombre_mayor = f"{nombre1}, {nombre2} y {nombre3}"
            cantidad_mayor = cantidad1

        elif cantidad1 == cantidad2 and cantidad1 > cantidad3:

            nombre_mayor = f"{nombre1} y {nombre2}"
            cantidad_mayor = cantidad1

        elif cantidad1 == cantidad3 and cantidad1 > cantidad2:

            nombre_mayor = f"{nombre1} y {nombre3}"
            cantidad_mayor = cantidad1

        elif cantidad2 == cantidad3 and cantidad2 > cantidad1:

            nombre_mayor = f"{nombre2} y {nombre3}"
            cantidad_mayor = cantidad2

        elif cantidad1 > cantidad2 and cantidad1 > cantidad3:

            nombre_mayor = nombre1
            cantidad_mayor = cantidad1

        elif cantidad2 > cantidad1 and cantidad2 > cantidad3:

            nombre_mayor = nombre2
            cantidad_mayor = cantidad2

        else:

            nombre_mayor = nombre3
            cantidad_mayor = cantidad3

        # Preparamos los resultados que se imprimirán en la web
        resultado = f"El nombre con mayor cantidad de caracteres es: {nombre_mayor}."
        detalle = f"El nombre tiene: {cantidad_mayor} caracteres."

        # Guardado de registro
        global contador_registros

        registros.append({
            "id": contador_registros,
            "ejercicio": "Comparación de nombres",
            "nombre1": nombre1,
            "nombre2": nombre2,
            "nombre3": nombre3,
            "resultado": resultado,
            "detalle": detalle
        })

        contador_registros += 1

        return render_template(
            "ejercicio2.html",
            resultado=resultado,
            detalle=detalle
        )

    return render_template("ejercicio2.html")

#Ejecución

if __name__ == "__main__":
    app.run(debug=True)
