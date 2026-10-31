# Configuración del proyecto Django.
# PyMySQL permite conectar Django con MySQL sin depender de una compilación local de mysqlclient.
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
