from Bio import SeqIO, Seq
import sys
import re
import gzip

'''Script created by Tomasz Molcan. This script find sequences motif 
in long sequence in forward and reverse orientation. To use it please 
look instruction provided below:
python3 MotifFinded.py ATGATGATG genome.fasta.gz'''

# Please provide motif sequence: Ex. AGTGCTA
input_fasta = sys.argv[1]
# Please provide genome fasta file in .gz fil: Ex. Fusarium_graminearum.fasta.gz
genome_fasta = sys.argv[2]

def Get_sequence_motif(motif_sequence, genome_sequence, strand_orientation="+"):
    '''This function search sequence motif in long sequence.'''
    for sequence in SeqIO.parse(gzip.open(genome_sequence, "rt"), "fasta"):
        for motif in re.finditer(motif_sequence, str(sequence.seq)):
            print("{}\t{}\t{}\t{}".format(sequence.id, motif.start() + 1, motif.end(), strand_orientation ))

def getSequence(fasta):
    '''Create dictionary for analyzing sequence and get sequence
    oreintation.'''
    fasta_dict = {fasta : "+"}
    fasta_dict.update({str(Seq.Seq(fasta).complement()) : "-"})
    return fasta_dict

fasta_motif = getSequence(input_fasta)
for keys, values in fasta_motif.items():
    Get_sequence_motif(keys, genome_fasta, values)
