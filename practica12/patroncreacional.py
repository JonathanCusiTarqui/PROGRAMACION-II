class ConexionBaseDeDatos:
    _instancia_unica = None

    def __new__(cls):
        if cls._instancia_unica is None:
            print("Creando una nueva conexión a la base de datos...")
            cls._instancia_unica = super(ConexionBaseDeDatos, cls).__new__(cls)
        return cls._instancia_unica

    def ejecutar_consulta(self):
        print("Ejecutando consulta en la base de datos...")

# Uso
conexion1 = ConexionBaseDeDatos()
conexion2 = ConexionBaseDeDatos()

print(conexion1 is conexion2) 
conexion1.ejecutar_consulta()
