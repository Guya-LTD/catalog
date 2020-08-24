db.createUser(
    {
        user : "inventory_user",
        pwd  : "inventory_password",
        roles : [
            {
                role : "readWrite",
                db   : "inventory_db"
            }
        ]
    }
)