folder=r'C:\Users\asakthivelu\Desktop\Personal\Wind Transmission Data\Geofabrik Data\rhode-island-latest-free.shp'

import os
import processing

#get the path of the file in the 'path' variable
for file in os.listdir(folder):    
    if file.find('roads') != -1 and file.endswith(".shp") :
        print(file)
        path = folder+'/'+file
        print(path)
        vlayer = QgsVectorLayer(path, file, "ogr")
        print(vlayer)

print(vlayer)
countMajor = 0
countMinor = 0

fields =vlayer.fields()
crs = vlayer.sourceCrs()
transform_context = QgsProject.instance().transformContext()
save_options = QgsVectorFileWriter.SaveVectorOptions()
save_options.driverName = "ESRI Shapefile"
save_options.fileEncoding = "UTF-8"

mjr_outputpath = r"C:\Users\asakthivelu\Desktop\Personal\Wind Transmission Data\Geofabrik Data\Major_Roads.shp"
mnr_outputpath = r"C:\Users\asakthivelu\Desktop\Personal\Wind Transmission Data\Geofabrik Data\Minor_Roads.shp"

mjr_outfile = QgsVectorFileWriter.create(
  mjr_outputpath,
  fields,
  vlayer.wkbType(),
  crs,
  transform_context,
  save_options
)

mnr_outfile = QgsVectorFileWriter.create(
  mnr_outputpath,
  fields,
  vlayer.wkbType(),
  crs,
  transform_context,
  save_options
)
if mjr_outfile.hasError() != QgsVectorFileWriter.NoError:
    print("Error when creating shapefile: ",  mjr_outfile.errorMessage())

if mnr_outfile.hasError() != QgsVectorFileWriter.NoError:
    print("Error when creating shapefile: ",  mnr_outfile.errorMessage())

for feature in vlayer.getFeatures():
  className = feature['fclass']
  if className == 'living_street' or className == 'motorway'or \
     className == 'residential' or className == 'secondary' or \
     className == 'secondary_link' or className == 'tertiary' or \
     className == 'tertiary_link' or className == 'trunk' or className == 'trunk_link':
    countMajor+=1
    mjr_attributes = feature.attributes()
    mjr_geometry = feature.geometry()
    mjr_featureAdd = QgsFeature()
    mjr_featureAdd.setAttributes(mjr_attributes)
    mjr_featureAdd.setGeometry(mjr_geometry)
    mjr_outfile.addFeature(mjr_featureAdd)
  else:
    countMinor+=1
    mnr_attributes = feature.attributes()
    mnr_geometry = feature.geometry()
    mnr_featureAdd = QgsFeature()
    mnr_featureAdd.setAttributes(mnr_attributes)
    mnr_featureAdd.setGeometry(mnr_geometry)
    mnr_outfile.addFeature(mnr_featureAdd)

print(countMinor)
print(countMajor)
    
iface.addVectorLayer(mjr_outputpath,'Major_Roads','ogr')
iface.addVectorLayer(mnr_outputpath,'Minor_Roads','ogr')
del mjr_outfile
del mnr_outfile