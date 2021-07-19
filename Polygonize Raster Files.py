import os
import processing
import qgis.core
inputfolder = r'C:\Users\asakthivelu\Desktop\Personal\Wind Transmission Data\USA Wind Files State Wise\MO\Sample'
state_Name = 'MO'
outputFolder = inputfolder + r'\Vectorized'
os.makedirs(outputFolder)

class MyFeedBack(QgsProcessingFeedback):
    def setProgressText(self, text):
        print(text)

    def pushInfo(self, info):
        print(info)

    def pushCommandInfo(self, info):
        print(info)

    def pushDebugInfo(self, info):
        print(info)

    def pushConsoleInfo(self, info):
        print(info)

    def reportError(self, error, fatalError=False):
        print(error)
        
for file in os.listdir(inputfolder):
  if file.endswith('.tif'):
    file_path = inputfolder +'/'+file
    print(file_path)
    out_path = outputFolder + '/' + state_Name + ' ' + os.path.splitext(file)[0] +'.shp'
    print(out_path)
    processing.run("gdal:polygonize",{'INPUT' : file_path,
                                        'BAND' : 1,
                                        'OUTPUT' :out_path}, feedback=MyFeedBack())

for file in os.listdir(outputFolder):
  if file.endswith('.shp'):
    vector_file_path = outputFolder +'/' + file
    vlayer = QgsVectorLayer(vector_file_path, file, "ogr")
    zero_dn = []
    count = 0
    for feature in vlayer.getFeatures():
      if feature['DN'] != 1:
        zero_dn.append(feature.id())
      else:
        count +=1
    res = vlayer.dataProvider().deleteFeatures(zero_dn)
    # Removing the file as there are no corresponding Area    
    print(res)
    print(count)
    vlayer.commitChanges()
    vlayer.dataProvider().addAttributes([QgsField("State_Abbr", QVariant.String),
                                        QgsField("Area", QVariant.Double, '', 10, 3)])    
    vlayer.updateFields()
    area_expression = QgsExpression('area($geometry)')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(vlayer))
    with edit(vlayer):
      for feature in vlayer.getFeatures():
        context.setFeature(feature)
        feature['State_Abbr'] = state_Name
        feature['Area'] = area_expression.evaluate(context)
        vlayer.updateFeature(feature)
    vlayer.dataProvider().deleteAttributes([vlayer.fields().indexFromName('DN')])
    vlayer.updateFields()
    del vlayer
    if count == 0:
      for delete_file in os.listdir(outputFolder):
        if os.path.splitext(delete_file)[0] == os.path.splitext(file)[0]:
          os.remove(outputFolder +'/' + delete_file)

