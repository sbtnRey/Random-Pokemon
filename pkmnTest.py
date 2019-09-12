'''
Simple Python3.7 + Flask app that shows random pokemon and some info about said
pokemon. Page refreshes every 10 seconds showing a new pokemon. API calls are
using the Python pokebase library to call pokeapi.
'''

from flask import Flask, redirect, url_for, request
import pokebase as pb
import os
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():


    pkmnNum = random.randint(1, 807)
    pkmnSprite = pb.pokemon_sprite(pkmnNum)
    pkmnName = pb.pokemon(pkmnNum)
    im = pkmnSprite.path
    pkmnImage = (im.split('/')[7])
    dex = pb.pokemon_species(pkmnNum)

    #API info sent to html page
    pkmnInfo = [dex.generation, pkmnName.weight, pkmnName.height, dex.habitat, pkmnName.types[0].type]

    # Move path of cached sprite to static folder (may need to change second argument to full path based on user setup)
    os.rename(im, "/static/" + pkmnImage)

    return '''
<html>
    <head>
        <title>Pokemon</title>
    </head>
    <body>
        <center><h1 style = "font-family:'Helvetica Neue';font-size:50px;font-style:bold;">''' + str(pkmnName).capitalize() +'''</h1></center>
        <center><img src= "/static/''' + str(pkmnNum).capitalize() + '''.png" style="width:270px;height:270px;"></center>
        <center><p style = "font-family:'Helvetica Neue';font-size:20px;font-style:bold;">
        <br> Generation: '''+ str(pkmnInfo[0]) +'''
        <br> Weight: '''+ str(pkmnInfo[1]) +'''
        <br> Height: '''+ str(pkmnInfo[2]) +'''
        <br> Habitat: '''+ str(pkmnInfo[3]) +'''
        <br> Type: '''+ str(pkmnInfo[4]) +'''
        </p></center>
    </body>
    <meta http-equiv="refresh" content="10" >
</html>
'''

if __name__ == '__main__':
   app.run(debug = True)
