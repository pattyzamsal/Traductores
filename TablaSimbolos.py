# Archivo: TablaSimbolos
# Autores: Vanessa Balleste y Patricia Zambrano
# Carnet: 08-10091 y 09-10919
# Fecha: 10/01/2014

# Clase para la declaración de una variable
# Almacena el tipo de la variable, su identificador,
# su nivel de identacion al imprimirse y su posición en el archivo

class variable():
  def __init__(self,id,type,block = None):
    self.id = id
    self.type = type
    self.ident = ''
    self.lineno = -1
    self.colno = -1
    if block is None:
      self.blocked = 0
    else:
      self.blocked = block
  
  def setLine(self,line):
    self.lineno = line
  
  def setColumn(self,col):
    self.colno = col
    
  def setType(self,type):
    self.type = type

  def __eq__(self,otro):
    return self.id == otro.id
  
  def __str__(self):
    return self.ident + "variable: " + str(self.id) + " | tipo: " + str(self.type)
  
# Clase para la tabla de símbolos. Almacena una lista de variables, y una identación
# que se usa al imprimirse
class SymTable():
  def __init__(self):
    self.lista = []
    self.ident=''
  
  def insertar(self,var):
    error = 0
    if self.esMiembro(var.id,0):
      error = 1
    else:
      self.lista.append(var)
    return error
    
  def borrar(self,var):
    if self.esMiembro(var.id,0):
      self.lista.remove(var)
  
  def actualizar(self,var):
    pass
  
  # El parametro verbose indica si debe imprimirse errores en pantalla
  def esMiembro(self,var,verbose):
    try:
      self.lista.index(variable(var,''))
    except ValueError:
      if verbose:
        print "El valor no se encuentra en la tabla de simbolos"
      return 0
    return 1
  
  def encontrar(self,id):
    if self.esMiembro(id,0):
      return self.lista[self.lista.index(variable(id,''))]
    else:
      return None
  
  # Este procedimiento mecla dos tablas de símblos. Si hay símbolos
  # repetidos, retorna una tupla con la posición de la variable repetida. De
  # lo contrario retorna None
  
  def mezclar(self,nuevaTabla):
    error = None
    for i in nuevaTabla.lista:
      if self.esMiembro(i.id,0):
        error = (i.lineno,i.colno,i.id)
      else:
        self.insert(i)
    return error
   
  def __str__(self):
    self.ident = self.ident + '  '
    retorno = self.ident + 'Tabla de simbolos:\n'
  
    for i in self.lista:
      i.ident = self.ident
      retorno += str(i)
      retorno += '\n'
    retorno = retorno + self.ident +'---\n'
    return retorno