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
The PDB file must be stored in the same place where the script is located. As the given folder in this repository.

Execute the script and the promt will ask you to give the PDB code. (This is just only the file name without the .pdb)

For example, using the given folder files:
```bash
python3.x pychandran.py
```
![Alt Text](https://github.com/XavierUPF/Pychandran/blob/main/Pychandran/terminalexample.gif)
