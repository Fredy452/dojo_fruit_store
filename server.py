from flask import Flask, render_template, request, session

app = Flask(__name__)  


# Configurar Secret Key para poder almacenar en cache
app.secret_key = "supersecret"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():

    #En vez de enviar los formularios por parametro vamos a almacenar en session para
    #Recuperar en el checkout

    # Datos de las frutas
    session["strawberry"] = request.form["strawberry"]
    session["raspberry"] = request.form["raspberry"]
    session["apple"] = request.form["apple"]

    # Datos del usuario
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]

    #Cobrando a cliente
    total_amount = int(session['strawberry']) + int(session['raspberry']) + int(session['apple'])  # noqa: E501
    print(f"Cobrando a {session['first_name']} por total {total_amount} frutas")


    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    