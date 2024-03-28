## Accuracy

The accuracy of the GeoMAD layers is dependent on the accuracy of the underpinning earth observation data. As the values of the geomedian and MAD are synthetic (not observed directly by satellite), they cannot be verified by field work.

To calculate a geomedian or MAD representative of clear observations, the majority of the input data must be clear of clouds, shadows or other issues that can adversely affect an observation. Where a location experiences more than 50% of time under the impact of clouds and shadows (such as areas of Tasmania) the GeoMAD can produce an output that is essentially cloud / shadow noise. As such it is necessary to use a large enough collection of data to enable clear medians to be calculated. To mitigate the impact of poor quality observations and other artefacts, the input data is first screened using the Pixel Quality product, however some poor pixels are likely to still be included in the data after screening. Increasing the period from which observations are included in the input dataset also helps to mitigate the issue. Where no-data pixels occur in locations that clear observations should occur, the cause is a lack of clear pixels to populate the GeoMAD.

% ## Quality assurance

