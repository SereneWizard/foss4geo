#%%
import re
import numpy as np
from glob import glob
from xml.etree import ElementTree as ET
from shapely.geometry import Point, Polygon

def get_kml_bounds(kmlFpath):
    tree = ET.parse(kmlFpath)
    root = tree.getroot().tag
    kmlns = re.split('[{}]', root)[1]
    elems = tree.findall(".//{%s}coordinates" % kmlns)

    llx, lly, urx, ury = 360., 90., -360., -90.
    for el in elems:
        for coords in el.text.split(' '):
            x, y = coords.split(',')
            x, y = float(x), float(y)
            x = (360+x) if x<0 else x
            llx = min(llx, x)
            lly = min(lly, y)
            urx = max(urx, x)
            ury = max(ury, y)

    return (llx, lly, urx, ury)



if __name__ == "__main__":
    kmlFname = glob('./kml/*.kml')[0]
    bounds = get_kml_bounds(kmlFname)


