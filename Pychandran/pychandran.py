import math
import Bio.PDB
import matplotlib.pyplot as plt
import numpy as np
import os

absolute_path = os.path.abspath(os.getcwd()) # Just to print the path once the plots are saved


print("REMEMBER! The PDB file must be in the same folder where the script is being executed.")
pdbfile = input("PDB file code: ")

def degrees(rad_angle) :
    """Converts any angle in radians to degrees.

    If the input is None, the it returns None.
    For numerical input, the output is mapped to [-180,180]
    """
    if rad_angle is None :
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180 :
        angle = angle - 360
    while angle < -180 :
        angle = angle + 360
    return angle 

pdb_code = pdbfile

structure = Bio.PDB.PDBParser().get_structure(pdb_code, "%s.pdb" % pdb_code)

anglesphi = []
anglespsi = []

for model in structure :
    for chain in model :
        polypeptides = Bio.PDB.CaPPBuilder().build_peptides(chain)
        for poly_index, poly in enumerate(polypeptides) :
            phi_psi = poly.get_phi_psi_list()
            for res_index, residue in enumerate(poly) :
                phi, psi = phi_psi[res_index]
                if phi and psi :
                  #Don't write output when missing an angle
                  anglesphi.append(degrees(phi))
                  anglespsi.append(degrees(psi))


# HERE THE PLOT SECTION

plt.figure(1, figsize=(10, 10))

# plot function, you can change the colour to the one you like
plt.scatter(x=anglesphi, y=anglespsi,  s=2, color = "#8eca74", marker=".")

# set the plot title
plt.title(f'{pdbfile} Ramachandran Plot')

# set the limitation of axes
plt.xlim((-180, 180))
plt.ylim((-180, 180))

# set the name of axes
plt.xlabel('\u03C6')
plt.ylabel('\u03C8')

# set the tags of axes
plt.xticks(np.arange(-180, 180, step=60))
plt.yticks(np.arange(-180, 180, step=60))

# set grid
plt.grid(True, linestyle="--", alpha=0.5, zorder=1)

print(f"Saving plot as {pdbfile}_ramachandran.png in folder...")
plt.savefig(f"{pdbfile}_ramachandran.png", dpi=400)
print("Done!")

plt.clf()

# Heatmap
plt.figure(1, figsize=(10, 10))
plt.hist2d(x=anglesphi, y=anglespsi, bins=100)
plt.title(f'{pdbfile} Heatmap Ramachandran Plot')
plt.xlim((-180, 180))
plt.ylim((-180, 180))
plt.xlabel('\u03C6')
plt.ylabel('\u03C8')
plt.xticks(np.arange(-180, 180, step=60))
plt.yticks(np.arange(-180, 180, step=60))
plt.grid(True, linestyle="--", alpha=0.5)
print(f"Saving plot as {pdbfile}_heatmap_ramachandran.png in folder...")
plt.savefig(f"{pdbfile}_heatmap_ramachandran.png", dpi=400)
print("Done!")
print(f"Both the ramachandran plot and the heatmap have been saved in {absolute_path}.")