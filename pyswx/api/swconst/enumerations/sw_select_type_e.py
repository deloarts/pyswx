# Filename: sw_select_type_e.py

"""
swSelectType_e Enumeration

Values for types of returned IDs.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html
"""

from enum import IntEnum


class SWSelectTypeE(IntEnum):
    """Enumeration of selection type values (returned IDs)."""

    SW_SEL_ADVSTRUCTMEMBER = 295  # See Remarks
    SW_SEL_ANNOTATIONTABLES = 98  # See Remarks
    SW_SEL_ANNOTATIONVIEW = 139  # See Remarks
    SW_SEL_ARROWS = 49  # See Remarks
    SW_SEL_ATTRIBUTES = 8  # See Remarks
    SW_SEL_BELTCHAINFEATS = 149  # See Remarks
    SW_SEL_BLOCKDEF = 99  # See Remarks
    SW_SEL_BLOCKINST = 93  # See Remarks
    SW_SEL_BODYFEATURES = 22  # See Remarks
    SW_SEL_BODYFOLDER = 118  # See Remarks
    SW_SEL_BOMFEATURES = 97  # See Remarks
    SW_SEL_BOMS = 54  # See Remarks
    SW_SEL_BOMTEMPS = 64  # See Remarks
    SW_SEL_BORDER = 254  # See Remarks
    SW_SEL_BREAKLINES = 31  # See Remarks
    SW_SEL_BROWSERITEM = 69  # See Remarks
    SW_SEL_CAMERAS = 136  # See Remarks
    SW_SEL_CENTERLINES = 103  # See Remarks
    SW_SEL_CENTERMARKS = 28  # See Remarks
    SW_SEL_CENTERMARKSYMS = 100  # See Remarks
    SW_SEL_COMMENT = 127  # See Remarks
    SW_SEL_COMMENTSFOLDER = 126  # See Remarks
    SW_SEL_COMPONENTS = 20  # See Remarks
    SW_SEL_COMPPATTERN = 37  # See Remarks
    SW_SEL_COMPSDONTOVERRIDE = 72  # See Remarks
    SW_SEL_CONFIGURATIONS = 47  # See Remarks
    SW_SEL_CONNECTIONPOINTS = 66  # See Remarks
    SW_SEL_COORDSYS = 61  # See Remarks
    SW_SEL_COSMETICWELDS = 220  # See Remarks
    SW_SEL_CTHREADS = 39  # See Remarks
    SW_SEL_CUSTOMSYMBOLS = 60  # See Remarks
    SW_SEL_DATUMAXES = 5  # See Remarks
    SW_SEL_DATUMLINES = 62  # See Remarks
    SW_SEL_DATUMPLANES = 4  # See Remarks
    SW_SEL_DATUMPOINTS = 6  # See Remarks
    SW_SEL_DATUMTAGS = 36  # See Remarks
    SW_SEL_DCABINETS = 42  # See Remarks
    SW_SEL_DETAILCIRCLES = 17  # See Remarks
    SW_SEL_DIMENSIONS = 14  # See Remarks
    SW_SEL_DISPLAYSTATE = 148  # See Remarks
    SW_SEL_DOCSFOLDER = 125  # See Remarks
    SW_SEL_DOWELSYMS = 86  # See Remarks
    SW_SEL_DRAWINGVIEWS = 12  # See Remarks
    SW_SEL_DTMTARGS = 40  # See Remarks
    SW_SEL_EDGES = 1  # See Remarks
    SW_SEL_EMBEDLINKDOC = 123  # See Remarks
    SW_SEL_EMPTYSPACE = 72  # See Remarks (duplicate of SW_SEL_COMPSDONTOVERRIDE)
    SW_SEL_EQNFOLDER = 55  # See Remarks
    SW_SEL_EVERYTHING = -3  # See Remarks
    SW_SEL_EXCLUDEMANIPULATORS = 111  # See Remarks
    SW_SEL_EXPLLINES = 45  # See Remarks
    SW_SEL_EXPLSTEPS = 44  # See Remarks
    SW_SEL_EXPLVIEWS = 43  # See Remarks
    SW_SEL_EXTSKETCHPOINTS = 25  # See Remarks
    SW_SEL_EXTSKETCHSEGS = 24  # See Remarks
    SW_SEL_EXTSKETCHTEXT = 88  # See Remarks
    SW_SEL_FABRICATEDROUTE = 70  # See Remarks
    SW_SEL_FACES = 2  # See Remarks
    SW_SEL_FACETS = 268  # See Remarks
    SW_SEL_FRAMEPOINT = 77  # See Remarks
    SW_SEL_FTRFOLDER = 94  # See Remarks
    SW_SEL_GENERALTABLEFEAT = 142  # See Remarks
    SW_SEL_GRAPHICSBODY = 262  # See Remarks
    SW_SEL_GTOLS = 13  # See Remarks
    SW_SEL_HELIX = 26  # See Remarks
    SW_SEL_HOLESERIES = 83  # See Remarks
    SW_SEL_HOLETABLEAXES = 105  # See Remarks
    SW_SEL_HOLETABLEFEATS = 104  # See Remarks
    SW_SEL_IMPORTFOLDER = 57  # See Remarks
    SW_SEL_INCONTEXTFEAT = 29  # See Remarks
    SW_SEL_INCONTEXTFEATS = 32  # See Remarks
    SW_SEL_JOURNAL = 124  # See Remarks
    SW_SEL_LEADERS = 84  # See Remarks
    SW_SEL_LIGHTS = 73  # See Remarks
    SW_SEL_LOCATIONS = -2  # See Remarks
    SW_SEL_MAGNETICLINES = 225  # See Remarks
    SW_SEL_MANIPULATORS = 79  # See Remarks
    SW_SEL_MATEGROUP = 30  # See Remarks
    SW_SEL_MATEGROUPS = 33  # See Remarks
    SW_SEL_MATES = 21  # See Remarks
    SW_SEL_MATESUPPLEMENT = 138  # See Remarks
    SW_SEL_MESHFACETEDGES = 269  # See Remarks
    SW_SEL_MESHFACETVERTICES = 270  # See Remarks
    SW_SEL_MESHSOLIDBODIES = 274  # See Remarks
    SW_SEL_MIDPOINTS = 59  # See Remarks
    SW_SEL_NOTES = 15  # See Remarks
    SW_SEL_NOTHING = 0  # See Remarks
    SW_SEL_OBJGROUP = 155  # See Remarks
    SW_SEL_OBJHANDLES = 48  # See Remarks
    SW_SEL_OLEITEMS = 7  # See Remarks
    SW_SEL_PICTUREBODIES = 80  # See Remarks
    SW_SEL_PLANESECTIONS = 219  # See Remarks
    SW_SEL_POINTREFS = 41  # See Remarks
    SW_SEL_POSGROUP = 68  # See Remarks
    SW_SEL_PUNCHTABLEFEATS = 234  # See Remarks
    SW_SEL_REFCURVES = 23  # See Remarks
    SW_SEL_REFEDGES = 51  # See Remarks
    SW_SEL_REFERENCECURVES = 26  # See Remarks (duplicate of SW_SEL_HELIX)
    SW_SEL_REFFACES = 52  # See Remarks
    SW_SEL_REFSILHOUETTE = 53  # See Remarks
    SW_SEL_REFSURFACES = 27  # See Remarks
    SW_SEL_REVISIONCLOUDS = 240  # See Remarks
    SW_SEL_REVISIONTABLE = 113  # See Remarks
    SW_SEL_REVISIONTABLEFEAT = 119  # See Remarks
    SW_SEL_ROUTECURVES = 63  # See Remarks
    SW_SEL_ROUTEPOINTS = 65  # See Remarks
    SW_SEL_ROUTESWEEPS = 67  # See Remarks
    SW_SEL_SECTIONLINES = 16  # See Remarks
    SW_SEL_SECTIONTEXT = 18  # See Remarks
    SW_SEL_SELECTIONSETFOLDER = 258  # See Remarks
    SW_SEL_SELECTIONSETNODE = 259  # See Remarks
    SW_SEL_SFSYMBOLS = 35  # See Remarks
    SW_SEL_SHEETS = 19  # See Remarks
    SW_SEL_SILHOUETTES = 46  # See Remarks
    SW_SEL_SIMELEMENT = 102  # See Remarks
    SW_SEL_SIMULATION = 101  # See Remarks
    SW_SEL_SKETCHBITMAP = 85  # See Remarks
    SW_SEL_SKETCHCONTOUR = 96  # See Remarks
    SW_SEL_SKETCHES = 9  # See Remarks
    SW_SEL_SKETCHHATCH = 56  # See Remarks
    SW_SEL_SKETCHPOINTFEAT = 71  # See Remarks
    SW_SEL_SKETCHPOINTS = 11  # See Remarks
    SW_SEL_SKETCHREGION = 95  # See Remarks
    SW_SEL_SKETCHSEGS = 10  # See Remarks
    SW_SEL_SKETCHTEXT = 34  # See Remarks
    SW_SEL_SOLIDBODIES = 76  # See Remarks
    SW_SEL_SOLIDBODIESFIRST = 81  # See Remarks
    SW_SEL_SUBATOMFOLDER = 121  # See Remarks
    SW_SEL_SUBSKETCHDEF = 154  # See Remarks
    SW_SEL_SUBSKETCHINST = 114  # See Remarks
    SW_SEL_SUBWELDFOLDER = 107  # See Remarks
    SW_SEL_SURFACEBODIES = 75  # See Remarks
    SW_SEL_SURFBODIESFIRST = 78  # See Remarks
    SW_SEL_SWIFTANNOTATIONS = 130  # See Remarks
    SW_SEL_SWIFTFEATURES = 132  # See Remarks
    SW_SEL_SWIFTSCHEMA = 159  # See Remarks
    SW_SEL_TITLEBLOCK = 192  # See Remarks
    SW_SEL_TITLEBLOCKTABLEFEAT = 206  # See Remarks
    SW_SEL_UNSUPPORTED = -1  # See Remarks
    SW_SEL_VERTICES = 3  # See Remarks
    SW_SEL_VIEWERHYPERLINK = 58  # See Remarks
    SW_SEL_WELDBEADS = 122  # See Remarks
    SW_SEL_WELDMENT = 106  # See Remarks
    SW_SEL_WELDMENTTABLEFEATS = 116  # See Remarks
    SW_SEL_WELDS = 38  # See Remarks
    SW_SEL_WIREBODIES = 74  # See Remarks
    SW_SEL_ZONES = 50  # See Remarks
