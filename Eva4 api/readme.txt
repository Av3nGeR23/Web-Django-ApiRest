Aplicacion Carrito de Compra Zapatillas

1- modificar o crear base de datos y conectar en settins.py.
2- Crear base de datos en phpmyadmin con nombre  (EvA3Django) 
3- utilizar comandos: python manage.py makemigrations / python manage.py migrate 
4- usar comando python manage.py createsuperuser para crear super usuario.
5- ingresar a http://127.0.0.1:8000/admin  ingresar credenciales -  seleccionar usuarios - selccionar super usuario creado - agregar todos los permisos en Permisos de usuario.
6- Pagina no permite ingresar productos al carrito si no esta logeado.
7- Logear, si inicia sesion con SuperUsuario podra tener acceso a la pestana de Stock donde se podra Agregar, Eliminar o Modificar productos (si no es super usuario no tendra acceso a Stock)
8- los productos ingresados se veran automanticamente en pestana Productos.
9- al agregar producto al carrito se descuentan del total de Stock.
10- Boton de Realizar Pedido - redirige a Home ya que funcionalidad aun no esta implementada.
11- http://127.0.0.1:8000/api  para ingresar a la api, solo podra ser manipulada por el superusuario.


Se Implementa Documentacion de Api  en la siguiente URL:  http://127.0.0.1:8000/docs/


utilizar 

pip install coreapi