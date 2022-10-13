#!/bin/bash
#SBATCH -A ABC123
#SBATCH -J visit_test
#SBATCH -N 1
#SBATCH -p gpu
#SBATCH -t 0:05:00

cd $SLURM_SUBMIT_DIR
date

module load visit

visit -nowin -cli -v 3.2.2 -l srun -np 1 -nn 1 -s visit_example.py
