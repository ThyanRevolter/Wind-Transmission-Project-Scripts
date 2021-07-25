import os
import processing
import qgis.core
inputfolder = r'C:\Users\asakthivelu\Desktop\Personal\Wind Transmission Data\USA Wind Files State Wise\Rhode Island\Remaining Area TIFF\Sample'
state_Name = 'Rhode Island'
state_abbr = 'RI'
outputFolder = inputfolder + r'/' + state_Name
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
    out_file_name = os.path.splitext(file)[0]
    out_path = outputFolder + '/' + state_Name + ' ' + out_file_name +'.shp'
    print(out_path)
    processing.run("gdal:polygonize",{'INPUT' : file_path,
                                        'BAND' : 1,
                                        'OUTPUT' :out_path}, feedback=MyFeedBack())

for file in os.listdir(outputFolder):
  if file.endswith('.shp'):
    vector_file_path = outputFolder +'/' + file
    vlayer = QgsVectorLayer(vector_file_path, file, "ogr")
    speed = 0
    if file.find('5') != -1:
      speed = 5
    if file.find('6') != -1:
      speed = 6
    if file.find('7') != -1:
      speed = 7
    if file.find('8') != -1:
      speed = 8
    if file.find('9') != -1:
      speed = 9
    if file.find('10') != -1:
      speed = 10    
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
                                        QgsField("Area", QVariant.Double, '', 10, 3),
                                        QgsField("Speed",QVariant.Int)])    
    vlayer.updateFields()
    area_expression = QgsExpression('area($geometry)')
    context = QgsExpressionContext()
    context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(vlayer))
    with edit(vlayer):
      for feature in vlayer.getFeatures():
        context.setFeature(feature)
        feature['State_Abbr'] = state_abbr
        feature['Area'] = area_expression.evaluate(context)
        feature['Speed'] = speed
        vlayer.updateFeature(feature)
    vlayer.dataProvider().deleteAttributes([vlayer.fields().indexFromName('DN')])
    vlayer.updateFields()
    del vlayer
    if count == 0:
      for delete_file in os.listdir(outputFolder):
        if os.path.splitext(delete_file)[0] == os.path.splitext(file)[0]:
          os.remove(outputFolder +'/' + delete_file)

