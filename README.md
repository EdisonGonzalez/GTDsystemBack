# GTDsystemBack
Esto es una aplicación desarrollada con Python + Flask y que su idea es exponerse en Heroku.

Configuracion venv:
https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3
https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3

Tutoriales base:
https://dev.to/paultopia/the-easiest-possible-way-to-throw-a-webapp-online-flask--heroku--postgres-185o
http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/
https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
http://www.pythondiario.com/2019/01/parametros-get-y-post-con-flask.html
https://stackoverflow.com/questions/22947905/flask-example-with-post
https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

Para tener en cuenta PSQL:
http://ujwalafossist.blogspot.com/2015/01/operationalerror-fesendauth-no-password.html
https://stackoverflow.com/questions/50121432/flask-authenticate-hashed-password-from-sqlalchemy

gist:
https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/
https://gist.github.com/dushan14

Algunas de los enlaces sobre el despliegue en Heroku:
https://devcenter.heroku.com/articles/logging#view-logs
https://devcenter.heroku.com/articles/multiple-environments
https://stackoverflow.com/questions/41804507/h14-error-in-heroku-no-web-processes-running
https://stackoverflow.com/questions/48512013/couldnt-find-that-process-type-heroku

Algunos enlaces sobre el manejo de paquetes:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Para tener en cuenta:
1. Después de clonar el proyecto corra los siguientes comandos:
    1.1. pip3 install virtualenv (Si no tiene dicho paquete)
    1.2. virtualenv <nombre-de-su-virtual-environment>
    1.3. source <nombre-de-su-virtual-environment>/bin/activate
         NOTA: Para desactivarlo solo use deactivate
    1.4. pip3 install -r requirements.txt
         NOTA: Recuerde que esto es gracias al paquete gunicorn, si quiere generar un nuevo archivo de paquetes
         use el comando: pip freeze > requirements.txt (El tomara los paquetes del venv que este activo)
2. Para crear la base de datos en postgressql:
    2.1. Puede usar pgAdmin en MacOSx y hacerlo por la consola de administración web.
    2.2. Puede usar los comandos o lo que desee, algunos ejemplos son:
        2.2.1. sudo -u <name_of_user> createdb <nombre-basededatos>
        2.2.2. psql -U <name_of_user> -d <nombre-basededatos>
    2.3. Puede revisar la documentación PSQL: https://www.postgresql.org/
3. Configure las variables de entorno en un archivo .env y además importelas en su sistema:
    3.1. Ejemplo en MacOSx:
        export APP_SETTINGS="config.DevelopmentConfig"
        export DATABASE_URL="postgresql://<user for example: postgres>:<password-db-postgres>@localhost/<nombre-base-de-datos>"
4. Ejecute:
    Si no ha modificado nada las migraciones con la base de datos son las mismas solo realice el upgrade y el runserver, sino elimine la carpeta de migraciones y ejecute los siguientes comandos:
    4.1. python3 manage.py db init
        NOTA: Verifique en done o hecho las tareas de creación de carpeta migraciones el cual contiene (versiones, script, env, README, alembic).
    4.2. python3 manage.py db migrate
        NOTA: Debe obtener: Context impl PostgresqlImpl, Will assume transactional DDL, detected added table <name-table> 
        Ahora puede verificar en PSQL la existencia de la tabla alembic
    4.3. python3 manage.py db upgrade
        NOTA: Ahora puede ver la tabla con los campos de su modelo
    NOTA: En caso de que la migración no sea exitosa (Y por lo tanto no puede hacer el Upgrade) intente hacer un DROP/DELETE de la tabla Alembic (drop table alembic_version;)
    4.4. Para finalizar es simplemente la ejecución con:
        python3 manage.py runserver
    NOTA: Allí puede ver los logs
