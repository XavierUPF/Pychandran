# Pychandran

This script generates a Ramachandran plot and heatmap of a given PDB file and stores the resulting images as png.

## Libraries
You will need Biopython, Matplotlib and Numpy for this script to work.

```bash
pip install biopython matplotlib numpy
pip install biopython matplotlib numpy -U
```

## How does it work?
The script takes the φ and ψ angles of the given PDB file and represents them into a ramachandran plot.
The PDB file must be stored in the same place where the script is running. As the given folder in this repository.

### Extended explanation

1. The structure is parsed and a list of models is returned. In most cases there is only one model, but it is possible to have multiple models in a PDB file.
   The parser returns a Structure object, which has a list of models, each model has a list of chains, each chain has a list of residues, each residue has a list of atoms.
2. The list of models is iterated over.
3. Each model has a list of chains, which is iterated over.
4. A CaPPBuilder object is used to build a list of polypeptides (i.e. chains of amino acids). This is necessary since not all chains in a PDB file are polypeptides, and the CaPPBuilder only returns polypeptides.
5. The list of polypeptides is iterated over.
6. For each polypeptide, a list of phi/psi angles is returned. This is a list of tuples, where each tuple contains a phi and psi angle for each residue in the polypeptide. The phi/psi angles for the first and last residues are None.
7. This list of tuples is iterated over.
8. The phi/psi angles are written to a list. 
9. Finally the plot is generated from the phi/psi angles lists.

Execute the script and the promt will ask you to give the PDB code. (This is just only the file name without the .pdb)

For example, using the given folder files:
```bash
python3.x pychandran.py
```
![Alt Text](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/terminalexample.gif)


### Some generated plots

Ramachandran plot          |  Heatmap of the Ramachandran plot
:-------------------------:|:-------------------------:
![](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/2dkt_ramachandran.png)  |  ![](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/2dkt_heatmap_ramachandran.png)
![](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/5fil_ramachandran.png)  |  ![](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/5fil_heatmap_ramachandran.png)
