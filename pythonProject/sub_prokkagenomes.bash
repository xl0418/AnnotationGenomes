#!/bin/bash
## now loop through the above array

#SBATCH --time=2-00:03:00   # walltime
#SBATCH --ntasks=8   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=1G   # memory per CPU core
#SBATCH -J "Prokka"   # job name
#SBATCH --mail-user=liangxu@caltech.edu   # email address

module load parallel
module load apptainer

sh prokkagenomes.sh 8 all_genomes_kingdom.csv


