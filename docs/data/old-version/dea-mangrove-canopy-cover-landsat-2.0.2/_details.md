## Background

Mangroves provide a diverse array of ecosystem services but these are impacted upon by both natural and anthropogenic drivers of change. In Australia, mangroves are protected by law and hence the natural drivers predominate.

It is important to know the extent and canopy density of mangroves in Australia so that we can measure how mangroves are responding to sea level rise, severe tropical cyclones and climatic cycles.

## What this product offers

This product provides valuable information about the extent and canopy density of mangroves for each year between 1987 and 2018 for the entire Australian coastline. 

The canopy cover classes are:

:::{list-table}

* - 20&ndash;50%
  - Pale green
* - 50&ndash;80%
  - Mid green
* - 80&ndash;100%
  - Dark green
:::

The product consists of a sequence (one per year) of 25 m resolution maps that are generated by analysing the Landsat [fractional cover](https://doi.org/10.6084/m9.figshare.94250.v1) developed by the Joint Remote Sensing Research Program and the [Global Mangrove Watch layers](https://doi.org/10.1071/MF13177) developed by the Japanese Aerospace Exploration Agency.

% ## Data description

## Applications

The sequence of mangrove maps makes it possible to see how the extent of mangroves is changing over time.  The maps can be used to understand how mangroves respond to disturbance events such as severe tropical cyclones.  The maps can also be used to improve our representation of the ecosystem services provided by mangroves, which include:

* Coastal protection
* Carbon storage
* Providing nursery grounds for commercially important fish and prawn species
* Providing habitat for migratory and endemic bird species

## Technical information

To determine annual national level changes in mangroves between 1987 and 2016, their extent (by canopy cover type) and dynamics were quantified using dense time-series (nominally every 16 days cloud permitting) of 25 m spatial resolution Landsat sensor data available within Digital Earth Australia (DEA).

The potential area that mangroves occupied over this period was established as the union of mangrove maps generated for 1996, 2007-2010 and 2015/16 through the Japanese Aerospace Exploration Agency (JAXA) Global Mangrove Watch (GMW), and then refined using tasseled cap wetness dynamics and State and Territory mangrove mapping products.   Within this area the 10th percentile of the green vegetation fraction of the  FC-PERCENTILE\_25\_2.0.0 (GVpc10) was retrieved. The percentage Planimetric Canopy Cover (PCC%) for each Landsat pixel was estimated using a relationship between GVpc10 and LiDAR-derived PCC% (< 1 m resolution and based on LIDAR acquisitions from all states supporting mangroves, excluding Victoria).   

The resulting annual maps of mangrove extent and cover indicate that the total area of mangrove forest (canopy cover > 20%; resolvable at the Landsat resolution) varied from a minima of 10,062 km2 in 1992 to a maxima of 10,642 km2 in 2010, declining to 10,434 km2 in 2016.  In 2010 (maximum extent), the forests were classified as closed canopy  (38.8%), open canopy (49.0%) and woodland mangrove (12.2%).  The majority of change occurred along the northern Australian coastline and was concentrated in the major gulfs and sounds.

## Lineage

The product development methodology is outlined in the following steps:

1) Calculate the green fractional cover (GVpc) from all available cloud-free Landsat pixels for each year of observation and compare these over an annual time series to identify areas where green cover persists throughout the year.

2) Establish a relationship between the 10th percentile of green fraction (GVpc10) observed within a year and Planimetric Canopy Cover percentage (PCC%) derived from < 1 m spatial resolution canopy masks derived from LIght Detection And Ranging (LiDAR) with this representing a unit that relates directly to forest cover.

3) Constrain the PCC% estimates to areas known to contain mangroves, with reference to the Japanese Aerospace Exploration Agency’s (JAXA) Kyoto and Carbon (K&C) Initiative Global Mangrove Watch (GMW) thematic layers for 1996, 2007-10 and 2015/16 with additional areas identified using tasseled cap wetness and State and Territory mangrove mapping products.

4) Apply PCC% thresholds to map mangrove forest extent (based on a pre-determined 20 PCC% threshold) and differentiate structural categories, namely, woodland (20-50 %), open forest (50-80 %), and closed forest (> 80 %).

5) Quantify the change in the extent of mangrove forest and canopy cover types over the period 1987 to 2018 at a national scale and establish relevance at regional (e.g., State/Territory) and local levels.

## Processing steps

1. Fractional Cover Processing

% ## Software

## References

Lymburner, L., Bunting, P., Lucas, R., Scarth, P., Alam, I., Phillips, C., Ticehurst, C., & Held, A. (2020). Mapping the multi-decadal mangrove dynamics of the Australian coastline. *Remote Sensing of Environment*, *238*, 111185. [https://doi.org/10.1016/j.rse.2019.05.004](https://doi.org/10.1016/j.rse.2019.05.004)

