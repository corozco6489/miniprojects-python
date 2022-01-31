from sqlite3 import Cursor
import mysql.connector

class Datos():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',database='base_datos',user='carlos',password='')
        
    def insertar_productos(self,codigo,nombre,modelo,precio,cantidad):
        cur =self.conexion.cursor()
        sql ='''INSERT INTO productos (CODIGOS , NOMBRE , MODELO , PRECIO , CANTIDAD) VALUES ('{}','{}','{}','{}','{}')'''.format(codigo,nombre,modelo,precio,cantidad)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        
    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = 'SELECT * FROM productos'
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def buscar_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX
    
    
    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql  = '''DELETE FROM productos WHERE NOMBRE={}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        
        
    def actualiza_productos(self, Id , codigo , nombre , modelo , precio,cantidad):
        cur=self.conexion.cursor()
        sql = '''UPDATE productos SET CODIGO = '{}' , NOMBRE = '{}' , PRECIO = '{}' , CANTIDAD = '{}' WHERE ID = '{}' '''.format(codigo,nombre,modelo,precio,cantidad,Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
        
        
    
    
    
