import sys, string
from os import path, makedirs
from shutil import copyfile

def initCreateDir(directory):
    if not path.exists(directory):
        makedirs(directory)
    if not path.exists(path.join(directory, "cards")):
        makedirs(path.join(directory, "cards"))
    if not path.exists(path.join(directory, "geom")):
        makedirs(path.join(directory, "geom"))
    cards = [   "cards/parameters.part",
                "cards/materials.part",
                "cards/source.part",
                "cards/tallies.part",
                "cards/traslations.part"]
    for card in cards:
        copyfile(card, path.join(directory, "cards"))
    geom=[  "geom/cells.part",
            "geom/surfaces.part"]
    for g in geom:
        copyfile(g, path.join(directory, "geom"))
