#!/bin/bash

echo "install.packages(c('devtools', ''), repos='http://cran.us.r-project.org')" | sudo R --no-save
echo "devtools::install_github('trestletech/shinyAce')" | sudo R --no-save
echo "devtools::install_github('swarm-lab/editR')" | sudo R --no-save