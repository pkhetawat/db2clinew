package main

import(
    "fmt"
    _ "github.com/ibmdb/go_ibm_db"
    "database/sql"
)

func main(){
    db, err := sql.Open("go_ibm_db", "HOSTNAME=waldevdbclnxtst06.dev.rocketsoftware.com;DATABASE=BJHADB;PORT=60000;UID=newton;PWD=A2m8test")
    if err != nil {
        fmt.Println("go ibm driver connection: FAILURE\n" ,err)
    }
    if err = db.Ping(); err != nil {
        fmt.Println("go ibm driver connection: FAILURE\n" ,err)
    } else {
    fmt.Println("go ibm driver connection: SUCCESS\n")
    }
}

