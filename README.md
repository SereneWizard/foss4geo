# foss4geo

The objective of this repository is to provide introduction to some good resources for using the open source tools to carry out geospatial analysis. The objecitive of this repository is to reduce our dependency on ArcGIS, and other proprietary softwares for geospatial analyis. 

<ol>

[foss4geo_intro.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/foss4geo_intro.ipynb)
This page provides a gentle introduction to the capacity of Python and command lines tools like GDAL to provide geospatial functionality. 

[point_to_shapefile.pynb](https://github.com/SereneWizard/foss4geo/blob/master/point_to_shapefile.ipynb)
Shows how to generate point features from the co-ordinates listed in the .csv file (along with other attributes)

[buffer_multiline.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/Buffer_multiline.ipynb)
Shows how to buffer line feature. The output is a polygon fetaure. The buffer distance has to be provided in the unit of measurement of the line feature file. 

[transform_shapefile.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/transform_shapefile.ipynb)
Shows how to use `pyproj` library to transform shapefile from one co-ordinate system to another. 

[shapefile_to_postgis.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/shapefile_to_postgis.ipynb)
Shows how to convert a shapefile to PostGIS table. This code uses `fiona` library for lazy evaluation of the shapefile features, and `psycopg2` for uploading each feature as Postgres table records. Lazy evaluation is useful in the sense that we don't have to upload the whole file in the memory in the beginning, and therefore, is advantageous for working with large shapefiles. 

[read_bounds_of_kml.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/read_bounds_of_kml.ipynb)
Extract bounds of the kml file. The kml file may have one or more features. 

[intersection.ipynb](https://github.com/SereneWizard/foss4geo/blob/master/intersection.ipynb)
Extract points in a grid intersected by a polygon. It uses `rtree` package (wrapped in `geopandas`) to create spatial index and then uses two-pass filtering for faster querying of the intersection points. 
<ol>