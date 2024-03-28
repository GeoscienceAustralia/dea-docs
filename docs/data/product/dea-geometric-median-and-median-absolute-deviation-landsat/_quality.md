## Accuracy

The accuracy of the GeoMAD layers is dependent on the accuracy of the earth observation data on which it is based. 

To calculate a reliable geomedian or MAD, the majority of the input data must be free of clouds, shadows, or other visual obstructions. For locations that experience more than 50% of time under clouds and shadows (such as areas of Tasmania) the GeoMAD can produce an output that is obscured by visual noise. Therefore, it is necessary to use a large enough collection of data to prevent this occurring. 

To reduce the impact of poor-quality earth observation data, the input data is screened using the Pixel Quality product.  

Note that where no-data pixels occur in locations that clear observations should occur, the cause is a lack of clear pixels to populate the GeoMAD. 

Also, note that since  the geomedian and MAD are synthetic (not observed directly by satellite), they cannot be verified by field work.
