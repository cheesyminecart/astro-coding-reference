from lightkurve import search_targetpixelfile

pixelfile = search_targetpixelfile("KIC 8462852", cadence="long", quarter=16).download();
pixelfile.plot(frame=1);

lc = pixelfile.to_lightcurve(aperture_mask="all");
lc.plot();


