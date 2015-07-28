### Analysis of UNOSAT Products
Series of scripts that analyze [UNOSAT datasets on HDX](https://data.hdx.rwlabs.org/organization/un-operational-satellite-appplications-programme-unosat?sort=metadata_modified+desc).

[![Build Status](https://travis-ci.org/luiscape/unosat-product-scraper-analysis.svg)](https://travis-ci.org/luiscape/unosat-product-scraper-analysis) [![Coverage Status](https://coveralls.io/repos/luiscape/unosat-product-scraper-analysis/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/unosat-product-scraper-analysis?branch=master)

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