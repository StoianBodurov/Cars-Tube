from resources.auth import RegisterUser, LoginUser

routs = [
    (RegisterUser, '/register'),
    (LoginUser, '/login'),
]
