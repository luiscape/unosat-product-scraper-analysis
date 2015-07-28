### Analysis of UNOSAT Products
Series of scripts that analyze [UNOSAT datasets on HDX](https://data.hdx.rwlabs.org/organization/un-operational-satellite-appplications-programme-unosat?sort=metadata_modified+desc).

[![Build Status](https://travis-ci.org/luiscape/unosat-product-scraper-analysis.svg)](https://travis-ci.org/luiscape/unosat-product-scraper-analysis) [![Coverage Status](https://coveralls.io/repos/luiscape/unosat-product-scraper-analysis/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/unosat-product-scraper-analysis?branch=master)

### Results and Recommendations

![Figure 1: shapefiles per resource](analysis-copy_files/figure-html/unnamed-chunk-2-1.png) 


Figure 1 above shows that at least 16 resources contain single shapefiles. That means that, on their respective datasets, a geo-preview will very likely not cause confusion to the users. For a more detailed review, please refer to the [analysis page](output/analysis.md).

As a result, I see two possible actions:

1. **Manually edit datasets**: activate the geo-preview only on those datasets in which the resources have a single shapefile. This would include editing ~16 datasets and keeping watch for future additions. 

2. **Expose Geo-preview Through API call**: at the moment the geo-preview is automatic. It detects resources that could be previewed and activates the geo-preview without user intervention. If we added a property to a dataset (i.e. `geo_preview: false`), an user could have more control over what to preview and what not to preview. This could be coded into the scraper and configured to only activate the geo-preview on those datasets that have a single shapefile per resource.

`1` is short-term; `2` is medium / long-term. 

`2` is preferred as I believe this kind of issue could become more and more common.


### Installation and Usage
Use the `Makefile`:

```makefile
run:
  bash bin/run.sh;

test:
  bash bin/test.sh;

setup:
  bash bin/setup.sh;
```

Those will produce results inside the `[output/](/output)` folder.


### Editing Analysis File
The analysis output is generated with a combination of `R` scripts and R markdown. Assuming you have R installed, run the following: 

```shell
$ make install_edit
$ make edit
```

A live editor will start, allowing you to to edit the analysis report.