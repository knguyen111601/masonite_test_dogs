"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "OwnerController@index").name("index"),
        Get("/@id", "OwnerController@show").name("show"),
        Post("/", "OwnerController@create").name("create")
    ], prefix="/owners", name="owners"),

    RouteGroup([
        Get("/", "DoggiesController@index").name("index"),
        Get("/@id", "DoggiesController@show").name("show"),
        Post("/", "DoggiesController@create").name("create")
    ], prefix="/dogs", name="dogs")
]
