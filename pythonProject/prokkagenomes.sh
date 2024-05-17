#!/bin/bash

# prokka genomes in parallel for all genomes in the input file
prokka_data(){
    # take the input file and split it by "/"
    IFS='/' read -ra ADDR <<< "$1"
    dir1=${ADDR[6]}
    genome1=${ADDR[7]}
#    echo $dir1
#    echo $genome1
    prokkaoutput="prokkaOutput"

    if [[ ! -e $prokkaoutput/$dir1/$genome1 ]]; then
        singularity exec prokka.sif prokka --norrna --notrna --centre X --compliant --kingdom Bacteria $1 --prefix $genome1 --outdir $prokkaoutput/$dir1/$genome1 #--prefix $prokkaoutput/$dir1
    fi
}
export -f prokka_data

echo "Prokka Starts"

# The second argument specifies the input file
inputfile=$2

# parallel the download function with the first argument specifying number of cores
cat $inputfile | parallel -j $1 prokka_data

echo "Done"
