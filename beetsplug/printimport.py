from beets.plugins import BeetsPlugin

class PrintImport(BeetsPlugin):
    def __init__(self):
        super(PrintImport, self).__init__()
        self.register_listener('album_imported', self.printimport)

    def printimport(library, album):
        print u'Musik: ' + album.albumartist + ' - ' + album.album + ' (' + album.genre + ' - ' + album.year + ') @ ' + album.bitrate + ' kBit/s'