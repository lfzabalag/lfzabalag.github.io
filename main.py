from flask import Flask, jsonify, request

@app.route("<id>")
def get_afiliado(id):
    afiliado = {"id":id,"nombres":nombre_test,"apellidos":apellido_test,"email":email_test,"estado":activo}
    query = request.args.get('query')
    if query:
        afiliado["query"] = query
    return jsonify(afiliado),200

app= Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)