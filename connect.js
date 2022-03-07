var ibmdb = require("ibm_db")
  , connStr = "DATABASE=BJHADB;HOSTNAME=waldevdbclnxtst06.dev.rocketsoftware.com;PORT=60000;PROTOCOL=TCPIP;UID=newton;PWD=A2m8test";

ibmdb.open(connStr, function (err, connection) {
    if (err)
    {     
      console.log("\n Nodejs connection in docker container : FAILURE\n\r" , err);
      return;
    }
    else
    {
      console.log("\n Nodejs connection in docker container : SUCCESS\n\r");
    }

});

