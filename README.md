# AQI-Deployment

App hosted in heroku platform :https://airqualityindexbypm.herokuapp.com/

you can get the App From the above link

Air Quality Index:

  This project is used to  find the air Quality by using climatic parameters Such as:

T	Average Temperature (°C)
TM	Maximum temperature (°C)
Tm	Minimum temperature (°C)
SLP	Atmospheric pressure at sea level (hPa)
H	Average relative humidity (%)
PP	Total rainfall and / or snowmelt (mm)
VV	Average visibility (Km)
V	Average wind speed (Km/h)
VM	Maximum sustained wind speed (Km/h)
VG	Maximum speed of wind (Km/h)
RA	Indicate if there was rain or drizzle (In the monthly average, total days it rained)
SN	Snow indicator (In the monthly average, total days that snowed)
TS	Indicates whether there storm (In the monthly average, Total days with thunderstorm)
FG	Indicates whether there was fog (In the monthly average, Total days with fog)

            To find the Target Variable PM2.5
In my Machine Learning Model I selected 7 Important parameters such as(T,TM,Tm,H,PP,VV,V,VM) to predict my Target variable

This Project is build from the  scratch which follows the DataScience Life cycle :

Data Understanding
Data Preparation
Modelling
Evaluation
Deployment

 Data collected from the :https://en.tutiempo.net/climate (web scrapping).

 files that are Resposible for this Project:
* Html_AQI.py --> for the Webscripping And saving files in Data Floder.
* Plot_AQI.py --> for the geeting my target variable from the csv file.
* Extract_Combine.py --> This File will get the html pages from the link using Requests api and store in Respective path.and the html pages have chennai climatic conditions
* MOdelSelectionAndValidation.ipynb --> use to EDA And model Selection and evalution.

** AQI_Deployment --> used to deloy in to heroku platflom

* For more Details on PM2.5 and factors Responsible for Climatic conditions Refer "About.txt" file  &
https://www.airveda.com/blog/Understanding-Particulate-Matter-and-Its-Associated-Health-Impact 

