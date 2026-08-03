from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, DataStructs, rdMolDescriptors

# Two known EGFR inhibitors, SMILES sourced from PubChem (CID 123631, CID 176870)
molecules = {
    "gefitinib": "COC1=C(C=C2C(=C1)N=CN=C2NC3=CC(=C(C=C3)F)Cl)OCCCN4CCOCC4",
    "erlotinib": "COCCOC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC=CC(=C3)C#C)OCCOC",
}

mols = {}
for name, smi in molecules.items():
    mol = Chem.MolFromSmiles(smi)
    mols[name] = mol
    canon = Chem.MolToSmiles(mol)
    formula = rdMolDescriptors.CalcMolFormula(mol)
    mw = Descriptors.MolWt(mol)
    print(f"--- {name} ---")
    print(f"  input SMILES:     {smi}")
    print(f"  canonical SMILES: {canon}")
    print(f"  formula (RDKit):  {formula}")
    print(f"  MW (RDKit):       {mw:.2f}")
    print()

# Morgan fingerprints (ECFP4-equivalent: radius=2), 2048 bits
print("=== Morgan fingerprints (radius=2, 2048 bits) ===")
fps = {}
for name, mol in mols.items():
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
    fps[name] = fp
    on_bits = list(fp.GetOnBits())
    print(f"{name}: {fp.GetNumOnBits()} bits set out of 2048")
    print(f"  first 15 on-bit indices: {on_bits[:15]}")

# Tanimoto similarity between the two fingerprints
sim = DataStructs.TanimotoSimilarity(fps["gefitinib"], fps["erlotinib"])
print()
print(f"Tanimoto similarity (gefitinib vs erlotinib): {sim:.3f}")
