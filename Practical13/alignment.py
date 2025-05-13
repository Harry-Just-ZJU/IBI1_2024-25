
from Bio import SeqIO

def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def calculate_alignment_score(seq1, seq2, matrix):

    score = 0
    for a, b in zip(seq1, seq2):
        if (a, b) in matrix:
            score += matrix[(a, b)]
    
    return score

def calculate_identity(seq1, seq2):

    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return (matches / len(seq1)) * 100

def main():

    p04179_seq = read_fasta("C:/Users/yxhua/Desktop/IBI/IBI1_2024-25/IBI1_2024-25/Practical13/P04179.fasta")[0]
    p09671_seq = read_fasta("C:/Users/yxhua/Desktop/IBI/IBI1_2024-25/IBI1_2024-25/Practical13/P09671.fasta")[0]
    random_seq = read_fasta("C:/Users/yxhua/Desktop/IBI/IBI1_2024-25/IBI1_2024-25/Practical13/random.fasta")[0]
    
    from Bio.Align import substitution_matrices
    blosum62 = substitution_matrices.load("BLOSUM62")
    print("\n=== Results ===")
    
    # P04179 vs P09671
    print("\nP04179 vs P09671:")
    score_1_2 = calculate_alignment_score(p04179_seq, p09671_seq, blosum62)
    identity_1_2 = calculate_identity(p04179_seq, p09671_seq)
    print(f"Score: {score_1_2}")
    print(f"Identity: {identity_1_2:.2f}%")
    
    # P04179 vs random
    print("\nP04179 vs random:")
    score_1_3 = calculate_alignment_score(p04179_seq, random_seq, blosum62)
    identity_1_3 = calculate_identity(p04179_seq, random_seq)
    print(f"Score: {score_1_3}")
    print(f"Identity: {identity_1_3:.2f}%")
    
    # P09671 vs random
    print("\nP09671 vs random:")
    score_2_3 = calculate_alignment_score(p09671_seq, random_seq, blosum62)
    identity_2_3 = calculate_identity(p09671_seq, random_seq)
    print(f"Score: {score_2_3}")
    print(f"Identity: {identity_2_3:.2f}%")

if __name__ == "__main__":
    main()