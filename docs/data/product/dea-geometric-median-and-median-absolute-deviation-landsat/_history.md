## Changelog

<span id="v4.0.0"></span>

### Version 4.0.0

* **Breaking change: Shift in grid origin point** &mdash; The south-west origin point of the DEA Summary Product Grid has been shifted 20 tiles west and 17 tiles south. Therefore, all tile grid references have been changed. For instance, a tile reference of `x10y10` has changed to `x30y27`. The tile grid references of all derivative products generated from 2024 onwards will also be changed; however, Analysis Ready Data products will not be affected.
* **Enhanced cloud masking to reduce noise** &mdash; An enhancement to cloud masking has reduced cloud and shadow noise. This enhancement (known as 'cloud buffering') involved cleaning cloud masks 
 using a 3-pixel morphological opening on clouds and a 6-pixel dilation on cloud and shadows. Note that some areas of very high surface reflectance (e.g. sand dunes and ocean areas) may exhibit worsened noise or data gaps, but these are infrequent occurrences with low impact.
* **Combined Landsat 8 and 9 product** &mdash; A single combined product for Landsat 8 and Landsat 9 is provided. It achieves better performance than the standalone Landsat 8 product due to using a larger number of available observations. A standalone Landsat 8 product will no longer be provided from calendar year 2022 onwards.
* **Prefixed band measurement names** &mdash; An 'nbart' prefix was added to band measurement names for consistency with our Analysis Ready Data products. For example, the `red` band has been renamed to `nbart_red`.

<img src="/_static/geomedian/Geomedian_2020_Tasmania_v4_0_vs_v3_1.gif" alt="A comparison of the Geomedian Tasmania: v4.0 vs v3.1." style="max-width: 600px;">
