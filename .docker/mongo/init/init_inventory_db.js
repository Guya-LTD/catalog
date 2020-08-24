db.createUser(
    {
        user : "catalog_user",
        pwd  : "catalog_password",
        roles : [
            {
                role : "readWrite",
                db   : "catalog_db"
            }
        ]
    }
)