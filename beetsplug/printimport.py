from beets.plugins import BeetsPlugin

class PrintImport(BeetsPlugin):
    def __init__(self):
        super(PrintImport, self).__init__()
        self.register_listener('album_imported', self.printimport)

    def printimport(library, album):
        print "Musik: {albumartist}  - {album} ({genre} - {year})".format(**album) # @ {bitrate} kBit/s