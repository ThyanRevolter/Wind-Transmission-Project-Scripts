<h1>Wind Transmission Project - Repo for Python Scripts & Arcade Expressions</h1>
<br>
<p>This repository contains the python scripts to filter/process Raster files and the OSM data. "ArcGIS Online Expressions.txt" file contains the dynamic expression used in the ArcGIS online popup attributes</p>
<section>
<h2>Polygonize Raster Files.py</h2>
<p>This python script uses the QGIS polygonize module to convert the raster to vector</p>
<br>
<ol>
<li>Download the script and open it in QGIS Python plugin</li>
<li>In the code modify the "inputfolder" variable at line#4 to the location where the .GEOTIFF Raster is located</li>
<li>In line#5 for the "outputFolder" variable enter the State Abbreviation</li>
<li>Once the above edits are completed, click on the run icon</li>
<li>Wait for the script to get completed</li>
<li>Once it has ran you will see a folder called "Vectorized" which has the converted vector files</li>
</ol>
</section>
<section>
<h2>Filter OSM Road Data.py</h2>
<p>This python script seperates the OSM Road data into Major and Minor Roads</p>
<br>
<ol>
<li>Download the script and open it in QGIS Python plugin</li>
<li>In the code modify the "folder" variable at line#2 to the location where the OSM data is located/li>
<li>Run the script in QGIS python console</li>
<li>Once it scipt completes, you can see the layers being added to the QGIS project</li>
<li>Open the folder where you had the OSM data to find a folder called Filtered</li>
<li>You can see two shapefiles in this folder named "Major_Roads" & "Minor_Roads" </li>
</ol>
</section>
<br>
<section>
<h2>ArcGIS Online Details and Steps</h2>
<p>Color Code for the remaining Area Vectors</p>
<table>
  <tr>
    <th>5 Speed</th>
    <th>#0060A6</th>
  </tr>
  <tr>
    <td>6 Speed</td>
    <td>#2782A4</td>
  </tr>
  <tr>
    <td>7 Speed</td>
    <td>#A889B8</td>
  </tr>
  <tr>
    <td>8 Speed</td>
    <td>#D78E9A</td>
  </tr>
  <tr>
    <td>9 Speed</td>
    <td>#FFA18E</td>
  </tr>
  <tr>
    <td>10 Speed</td>
    <td>#FFCABF</td>
  </tr>
</table>
</section>
