from flask import Flask, jsonify, request

afiliados = []
#Rutas API:
@app.route('/afiliados/<id>',methods=['GET','POST'])
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
        #busqueda/filtro:
        search = request.args.get('search','').lower()
        
        #Ordenar
        sort_by = request.args.get('sort_by','id')
        
        order = request.args.get('order','desc')
        
        #Paginación
        #Numero de pag
        page = int(request.args.get('page',1))
        #Numero de afiliados por pagina
        per_page = int(request.args.get('per_page',15))
        
        #Recuperar lista de afiliados
        return jsonify(afiliados),200


app= Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)