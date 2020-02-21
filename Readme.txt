This is the source for pokesheets app.

Pokesheets app is a pokemon api client.  It will look up the given pokemon
or pokemons in the parameter list and return with id,name,weight and possible
types of the lookup pokemon.

This app is docker contained so in order to use it, you can either pull it from 
my share dockerhub by typing:

    docker pull launchcglaptop01/pokesheets

or build it yourself by typing:

    docker build --tag pokesheets .

In this source directory.

To run this app inside of the container after pulling, please type:

    docker run -it pokesheets:latest pikachu bulbasaur