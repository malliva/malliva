db = db.getSiblingDB('malliva21_db')
db.createUser(
    {
        user: "mallivay21",
        pwd: "P123Malliva",
        roles: [
            {
                role: "readWrite",
                db: "malliva21_db"
            }
        ]
    }
);