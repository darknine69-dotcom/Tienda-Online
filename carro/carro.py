class Carro():
    def __init__(self,request):
        self.request=request
        self.session=self.request.session #coje el auth user cactura secion 
        carro =self.session.get("carro") #y que ese session quede gusrdada en el carro
        if not carro:
            carro=self.session["carro"]={}  #q si el carro no existe lo deje en lista vacia
        # else:
        self.carro=carro
            #conserve lo q tenga en el carro
            
    # #Funcionalidad para agregar productos al carro
    # def agregar(self,producto):
    #     if (str(producto.id) not in self.carro.keys()):
    #         self.carro[producto.id]={
    #             "producto_id":producto.id,
    #             "nombre":producto.nombre,
    #             "precio": str(producto.precio),
    #             "cantidad":1, #se va aaregando de auno acumulador
    #             "imagen":producto.imagen.url 
    #         }
    #     else:
    #         for key,value in self.carro.items(): #trae clave y valor
    #             if key==str(producto.id):
    #                 value["cantidad"]=value["cantidad"]+1
    #                 break
    #     self.guardar_carro()
    
    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id]={
               "producto_id":producto.id,
               "nombre":producto.nombre,
               "precio":str(producto.precio),
               "cantidad": 1,
               "imagen":producto.imagen.url,
               }#captura las variables 
        else:
            self.carro[producto_id]["cantidad"]+=1
        self.guardar_carro()
            
            
        
        
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
            
             
             
    def restar(self,producto):
        for key,value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()#Se pueden anidar otros metodos
        
        
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        

        
        
        
        
            
            

                
                
               
        
        
        
                
    