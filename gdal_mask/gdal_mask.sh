#!/bin/bash
for x in ./raster/*.tif; 
do 
	echo $x
done
inrast=$x

outputdir='output'
if [[ -d $outputdir ]]; 
then
	rm -R -f $outputdir
fi
mkdir $outputdir

for inshp in *.shp;
do
	outfname="$(echo $inshp | cut -d'.' -f1)_mask.tif"
	outrast="$outputdir/$outfname"
	echo $outrast 
	gdalwarp -cutline $inshp -crop_to_cutline $inrast $outrast
done

