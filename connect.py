import ibm_db

conn_str = "DATABASE=BJHADB;HOSTNAME=waldevdbclnxtst06.dev.rocketsoftware.com;PORT=60000;UID=newton;PWD=A2m8test"

connection = ibm_db.connect(conn_str,"","")

print("\n Connection string used: " + conn_str) 

if (connection):
        print ("\n python ibm_db connection in docker container : SUCCESS\n\r")
else:
        print ("\n python ibm_db connection in docker container : FAILURE\n\r")


