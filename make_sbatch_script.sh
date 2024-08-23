#! /bin/bash

touch $1
scriptname=$(echo $1 | cut -d '.' -f '1')
error=$scriptname".out"
email=$2 #or hardcode this

echo '#!/bin/bash' >> $1
echo '#SBATCH -J'$scriptname'                  # Job name' >> $1
echo '#SBATCH --account=gts-alind6                 # charge account' >> $1
echo '#SBATCH -N1 --ntasks-per-node=8                 # Number of nodes and cores per node required' >> $1
echo '#SBATCH --mem-per-cpu=1G                        # Memory per core' >> $1
echo '#SBATCH -t8:00:00                               # Duration of the job (Ex: 1 hour)' >> $1
echo '#SBATCH -qinferno                               # QOS Name' >> $1
echo '#SBATCH -oReport-%x-%j.out                         # Combined output and error messages file' >> $1
echo '#SBATCH --mail-type=END,FAIL              # Mail preferences' >> $1
echo '#SBATCH --mail-user='$email'       # E-mail address for notifications' >> $1

