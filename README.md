### Analysis of UNOSAT Products
Series of scripts that analyze [UNOSAT datasets on HDX](https://data.hdx.rwlabs.org/organization/un-operational-satellite-appplications-programme-unosat?sort=metadata_modified+desc).

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

Those will produce results inside the `data/` folder. 