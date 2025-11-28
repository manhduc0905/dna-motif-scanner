from Bio import Entrez, SeqIO 
Entrez.email = "bioinformatics@edu.org"

def fetch_p21_promoter():
    handle = Entrez.efetch(db = "nucleotide", id="NG_009364.1", rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    promoter_seq = record.seq[2400:5000]
    output_path = "../tests/p21_promoter.fasta"
    with open(output_path, "w") as f:
        f.write(">CDKN1A_Promoter_2.6kb_upstream\n")
        f.write(str(promoter_seq))
        
    print(f"Success! Saved to {output_path}")
if __name__ == "__main__":
    fetch_p21_promoter()
