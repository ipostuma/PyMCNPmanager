import sys, string
from os import path, makedirs
from shutil import copyfile

def initCreateDir(directory):
    this_dir, this_filename = path.split(__file__)
    if not path.exists(directory):
        makedirs(directory)
    if not path.exists(path.join(directory, "cards")):
        makedirs(path.join(directory, "cards"))
    if not path.exists(path.join(directory, "geom")):
        makedirs(path.join(directory, "geom"))
    cards = [   path.join(this_dir,"cards/parameters.part"),
                path.join(this_dir,"cards/materials.part"),
                path.join(this_dir,"cards/source.part"),
                path.join(this_dir,"cards/tallies.part"),
                path.join(this_dir,"cards/traslations.part")]
    for card in cards:
        print "move "+card+" in "+path.join(directory, "cards/",path.basename(directory))
        #copyfile(card, path.join(directory, "cards/",path.basename(directory)))
    geom=[  path.join(this_dir,"cards/cells.part"),
            path.join(this_dir,"cards/surfaces.part")]
    for g in geom:
        print "move "+g+" in "+path.join(directory, "geom/",path.basename(g))
        #copyfile(g, path.join(directory, "geom/",path.basename(g)))
