import web
# @
from web import form
from datos import Clientes
from datos import Peliculas
render=web.template.render('templates')
urls = (
    '/(.*)', 'index'
)

db = web.database(dbn='mysql', db='Rentapeliculas', user='root', pw='1234')

Clientes = Clientes()  
Clientes.read()
Pelis=Peliculas()
Pelis.read()

myform = form.Form( 
    form.Dropdown('NombreCliente', Clientes.getClientes()), 
    form.Dropdown('Pelicula',Pelis.getPeliculas()), 
    form.Dropdown('Formato', ["BluRay","DVD","VHS"]),
    form.Dropdown('Duracion', ["1","2","3","4"])
    
    ) 
class index:
    def GET(self,results):
        form = myform()
        resultado=db.select('renta')
        return render.index(form,resultado)
        
    def POST(self,results): 
        form = myform() 
        if not form.validates(): 
            return render.index(form)
        else:
            precio=0
            if form.d.Formato=="Blueray":
                precio=20
            elif form.d.Formato=="DVD":
                precio=10
            elif form.d.Formato=="VHS":
                precio=5

            total=int(form.d.Duracion)*precio

            db.insert('renta',
            pelicula=form.d.Pelicula, 
            formato=form.d.Formato,
            duracion=form.d.Duracion,
            nombreCliente=form.d.NombreCliente,
             total=total)
            
            resultado=db.select('renta')

            return render.index(form,resultado)
    

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()