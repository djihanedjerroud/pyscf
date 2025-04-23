from pyscf import gto, scf

# Définir l'atome d'hélium
mol = gto.Mole()
mol.atom = 'He 0 0 0'   # position de l'atome
mol.basis = 'sto-3g'    # base minimale
mol.charge = 0
mol.spin = 0            # multiplicité singulet : 2S = 0
mol.build()

# Lancer le calcul Hartree-Fock
mf = scf.RHF(mol)
energy = mf.kernel()

print(f"Énergie Hartree-Fock (en a.u.) : {energy:.6f}")
print(f"Énergie Hartree-Fock (en eV) : {energy * 27.2114:.2f} eV")
