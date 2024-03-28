
A Daily Validation Summary Report of the surface reflectance data collected on the date of 22 September 2023 by Geoscience&nbsp;Australia. The full data can be found in the [NSD database](https://www.dea.ga.gov.au/products/national-spectral-database).

:::{contents} In this report
:local:
:backlinks: none
:::

## Variables

The variables and other environmental factors that were present on the day the data was collected.

:::{csv-table}
:class: validation-report-variables-table

"Instrument(s) used","ASD FR4 (18179/3)"
"Time of field site measurements (UTC)","2023-11-26 00:05:36 to 2023-11-26 00:53:24"
"Time of overpass (UTC)", 2023-11-26 00:33:00
"GPS quality","Good"
"Reference position","140.64201522E, 32.17492712S (WGS84)"
"<a href='/guides/about/glossary/#pq' target='_blank'>Matchup quality</a>","Excellent"
:::

## Results

The surface reflectance statistics collected on this day are grouped into bands. This allows the data to be used to validate our other datasets which use the same standardised bands.

:::{csv-table}
:class: validation-report-results-table

"<a href='/guides/about/glossary/#band' target='_blank'>Band</a>","Sat Mean","Sat rms","Field mean","Field rms"
"CA","0.0557","0.000895","0.0508","0.00527"
"Blue","0.0681","0.00127","0.0646","0.00751"
"Green","0.118","0.00385","0.119","0.0244"
"Red","0.21","0.00766","0.21","0.0569"
"<a href='/guides/about/glossary/#nir' target='_blank'>NIR</a>","0.281","0.00876","0.279","0.0584"
"<a href='/guides/about/glossary/#swir' target='_blank'>SWIR1</a>","0.371","0.00847","0.378","0.0606"
"<a href='/guides/about/glossary/#swir' target='_blank'>SWIR2</a>","0.303","0.0075","0.318","0.0651"
:::

* {download}`Download as CSV <./Daily_Validation_Results_2023-11-26.csv>`

## Figures

Click each figure to view it at full size.

:::::{grid} 1 1 2 3
::::{grid-item}
:::{figure} ./RGB_2023-11-26.png

A satellite imagery tile showing surface reflectance.
:::
::::
::::{grid-item}
:::{figure} ./DayComparison_2023-11-26.png

A chart showing bands.
:::
::::
::::{grid-item}
:::{figure} ./OverallComparison_2023-11-26.png

A chart showing surface reflectance.
:::
::::
:::::

% :::{tags} validation, daily_validation, mullion_validation, landsat_8_validation
% :::
