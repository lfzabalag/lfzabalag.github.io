from flask import Flask, jsonify, request

afiliados = []
#Rutas API:
@app.route("/afiliados/<id>",methods=['GET','POST'])
def get_afiliado(id):
    if request.method == 'POST':
        #Agregar un nuevo afiliado:
        data = request.json
        ingresa_afiliado = {
            "id":len(afiliados) + 1, 
            "nombres": data['nombres'],
            "apellidos":data['apellidos'],
            "email":data['email'],
            "estado":data['estado']            
        }
        
        afiliados.append(ingresa_afiliado)
        return jsonify(data),201
    
    if request.method == 'GET':
    #Recuperar lista de afiliados
       return jsonify(afiliados),200


app= Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)