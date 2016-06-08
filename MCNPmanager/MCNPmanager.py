import sys, string
from os import path, makedirs,getcwd,remove
from shutil import copyfile

#This function manages the creation of the MCNP project by creating 2 directories
#   - cards : which contains files for the definition of
#           * parameters
#           * materials
#           * source
#           * tallies
#           * translations
#   - geom  : which contains files for the definition of
#           * cells
#           * surfaces
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
        copyfile(card, path.join(directory, "cards/",path.basename(card)))
    geom  = [   path.join(this_dir,"cards/cells.part"),
                path.join(this_dir,"cards/surfaces.part")]
    for g in geom:
        copyfile(g, path.join(directory, "geom/",path.basename(g)))

#This function defines a method to copy an existing project into an other project (a sort of new branch)
def cpMCNPproject(directory):
    wkdir=getcwd()
    if checkifMCNPproject(directory,1)==1:
        return 1
    elif checkifMCNPproject(wkdir,2)==2:
        return 2
    else:
        cards = [   path.join(directory,"cards/parameters.part"),
                    path.join(directory,"cards/materials.part"),
                    path.join(directory,"cards/source.part"),
                    path.join(directory,"cards/tallies.part"),
                    path.join(directory,"cards/traslations.part")]
        geom  = [   path.join(directory,"geom/cells.part"),
                    path.join(directory,"geom/surfaces.part")]
        for card in cards:
            try:
                copyfile(card, path.join(wkdir, "cards/",path.basename(card)))
            except Exception as e:
                print "\n\033[1;34mMCNPmanager cp error:\033[1;32m %s \033[0m\n" % (e)

        for g in geom:
            try:
                copyfile(g, path.join(wkdir, "geom/",path.basename(g)))
            except Exception as e:
                print "\n\033[1;34mMCNPmanager cp error:\033[1;32m %s \033[0m\n" % (e)
        return 0

def buildMCNPproject(directory=getcwd()):
    if checkifMCNPproject(directory,1)==1:
        return 1,"no file"
    cards = [   path.join(directory,"cards/parameters.part"),
                path.join(directory,"cards/materials.part"),
                path.join(directory,"cards/source.part"),
                path.join(directory,"cards/tallies.part"),
                path.join(directory,"cards/traslations.part")]
    f = open( path.join(directory,"cards/alltogether.part"),"w")
    for card in cards:
        cf = open(card,"r")
        f.write(cf.read())
        cf.close()
    f.close()
    geom  = [   path.join(directory,"geom/cells.part"),
                path.join(directory,"geom/surfaces.part"),
                path.join(directory,"cards/alltogether.part")]
    title = "MCNPmanager project input file"
    outputfile = "mcnp.inp"
    f = open("lessphotons12.inp", "w")
    f.write(title+" -> "+outputfile)
    for g in geom:
        cf = open(g,'r')
        f.write("\r\n"+cf.read())
        cf.close()
    f.close()
    return 0,outputfile

#Check if a directory contains an MCNPmanager project
def checkifMCNPproject(directory,r):
    if not path.exists(path.join(directory, "cards")):
        print "\n\033[1;34mMCNPmanager cp error:\033[1;32m %s contains no MCNPmanager project\033[0m\n" % (directory)
        return r
    elif not path.exists(path.join(directory, "geom")):
        print "\n\033[1;34mMCNPmanager cp error:\033[1;32m %s contains no MCNPmanager project\033[0m\n" % (directory)
        return r
