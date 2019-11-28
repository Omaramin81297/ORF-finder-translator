import re
# We print a welcome message, explaining the usage of this tool and its outcome and how do we choose from the choices given.
print('''Welcome to the ORF finder & DNA translator tool. this will help you find all possible open reading frames
and predicting their protein sequence.

The result of this program will be in a text file called completeframes which has all the info
about every single ORF in all frames.

It will also create 6 fasta files called orf_frame_n, n for each frame.

please choose any option you like by writing its number only. \n''')
# We make a while loop, in order to return to the start point if there's a user error. if there's none, the loop will be broken and the code is continued.
while True:
    # Entering 1 will choose to input from file, 2 will choose to input from terminal
    choice=input('''First, how would you like to enter your sequences?
    1: Enter the sequences through a file
    2: Enter them through the terminal
    ''')
    # Make an error statement to show if the user didn't put anything
    if choice=='':
        print("\nError: You didn't choose an option!\n")
    # Make an error statement to show if the user wrote something that isn't present in the choices above
    elif choice not in ['1','2']:
        print("\nError: Your entry isn't from the choices above!\n")
    # If everything is fine, break the loop
    else:
        break
# A conditional where the file was chosen
if choice=='1':
    # Another while loops for file error
    while True:
        while True:
            # -fileo- is the name of the input file
            fileo=input('\nInput file name with the extension: ')
            # Error statement if the user skipped putting the file name
            if fileo=='':
                print("\nError: You didn't enter a file name!")
            # If he wrote something:
            else:
                # We now try to see if this file exists or not, we test for python errors now
                try:
                    fasta=open(fileo).read()
                # If it doesn't exist, print this message
                except IOError:
                    print('\nError: File not found in this directory!')
                # If the file exists and everything is fine, break the loop and open the file
                else:
                    break
        # Using a patern, we find all sequences with its names inside the file and put it in variable -name_with_seq-, and we create
        # two empty lists called -names- and -sequences-
        name_with_seq=re.findall(r'>.*\n[\w\n]*',fasta)
        names=[]
        sequences=[]
        # We take every string in the list and split it by the first \n, that will split between the name and the sequence
        for i in name_with_seq:
            # -one_name- is the name of the sequence and -one_seq- is the sequence, we append the name to -names- and the sequence to -sequences-
            one_name,one_seq=re.split(r'\n',i,1)
            names.append(one_name)
            sequences.append(one_seq)
        # -errornum- is used to break the big while loop if all the sequences in -sequences- have no wrong characters or errors
        errornum=0
        for i in range(0,len(sequences)):
            invalid=re.search(r'[^ATGCatgcnN\n\s]',sequences[i])
            if invalid:
                print('Error: ('+names[i]+') has invalid DNA sequence characters at location '+str(invalid.start()+1))
                errornum+=1
        # If nothing's wrong, break the loop
        if errornum==0:
            break
    # Make an empty list called -seqs_final-, this will be the last modified sequences which will be used in the code
    seqs_final=[]
    # Loop through every sequence in -sequences-
    for i in sequences:
        # Remove every newline from every sequence, and append the result to -seqs_final-
        seqs_final.append(i.replace('\n','').replace(' ',''))
# A conditional where the manual input was chosen
if choice=='2':
    names=[]
    sequences=[]
    seqs_final=[]
    # We create something called -seqcounter- which will help us if the user didn't want to put a sequence name
    seqcounter=1
    # As long as the loop continues, the user can put as many sequences as he wants
    while True:
        # Input the name of the sequences
        name=input('\nInput your sequence name or header (If you skip this, it will be named >Sequence number): ')
        # If the user decided not to give it a name, it will be named >Sequence n, n for the value in seqcounter
        if name=='':
            name='>Sequence '+str(seqcounter)
        # If the program didn't find the starter tag, it adds is automatically
        if re.search(r'^>',name)==None:
            name='>'+name
        # Another loop to check for errors in the entered DNA sequence, I used here a special technique to solve the pasta problem
        while True:
            print('\nInput your DNA sequence for '+name+':')
            seq=''
            while True:
                line=input('')
                seq+=line
                if line=='':
                    break
            # If the user didn't enter a sequence, an error message will be printed
            invalid=re.search(r'[^ATGCatgcnN\s]',seq)
            if seq=='':
                print("Error: You didn't enter a sequence!")
            # If we found any character other than ATGC,atgc and N, an error message will be printed
            elif invalid:
                print('Error: Your DNA sequence has invalid characters at position '+str(invalid.start()+1))
            # If all is ok, break the loop
            else:
                break
        # Append the name to -names-
        names.append(name)
        # Append the sequence to -sequences-
        sequences.append(seq)
        # We now ask if the user wants to add more sequences
        while True:
            choicemaker=input('''\nDo you wish to enter more sequences?
    1: Yes
    2: No
    ''')
            # We do the causual error handling here
            if choicemaker not in ['1','2']:
                print("\nError: Your entry isn't from the choices above!\n")
            else:
                break
        # If we choose 1, -seqcounter- will be increased by one, so for example the second sequence will be >Sequence 2 if the user didn't choose a name
        if choicemaker=='1':
            seqcounter+=1
        # If he chose 2, break the loop
        elif choicemaker=='2':
            break
    # Loop through the manually entered sequences
    for i in sequences:
        # Remove all newlines and spaces
        seqs_final.append(i.replace('\n','').replace(' ','').upper())
# Choose the genetic code number and assign it to -genetic_code_num-
while True:
    genetic_code_num=input('''\nPlease choose your genetic code number:
    1:  Standard Code
    2:  Vertebrate Mitochondrial Code
    3:  Yeast Mitochondrial Code
    4:  Mold, Protozoan, and Coelenterate Mitochondrial Code and Mycoplasma/Spiroplasma Code
    5:  Invertebrate Mitochondrial Code
    6:  Ciliate, Dasycladacean and Hexamita Nuclear Code
    7:  Echinoderm and Flatworm Mitochondrial Code
    8:  Euplotid Nuclear Code
    9:  Bacterial, Archaeal and Plant Plastid Code
    10: Alternative Yeast Nuclear Code
    11: Ascidian Mitochondrial Code
    12: Alternative Flatworm Mitochondrial Code
    13: Chlorophycean Mitochondrial Code
    14: Trematode Mitochondrial Code
    15: Scenedesmus obliquus Mitochondrial Code
    16: Thraustochytrium Mitochondrial Code
    17: Pterobranchia Mitochondrial Code
    18: Candidate Division SR1 and Gracilibacteria Code
    19: Pachysolen tannophilus Nuclear Code
    20: Karyorelict Nuclear Code
    21: Condylostoma Nuclear Code
    22: Mesodinium Nuclear Code
    23: Peritrich Nuclear Code
    24: Blastocrithidia Nuclear Code
    25: Cephalodiscidae Mitochondrial UAA-Tyr Code
    ''')
    # An error statement if user didn't choose anything
    if genetic_code_num=='':
        print("Error: You didn't choose a specific code!")
# An error statement when user puts anything other than a number or a number different than the choices
    elif re.search(r'^[1-9]$|^1[0-9]$|^2[0-5]$',genetic_code_num)==None:
        print("\nError: Your entry isn't from the choices above!")
    else:
        break
# Input the number of the minimum ORF size
while True:
    n=input('\nPlease enter the minimum ORF length (you can skip this, it will be set automatically to 100 base pairs): ')
    # Set to 100 if -n- is ''
    if n=='':
        n=100
        break
    # If it has a value, but it's not a number, we validate that by regex pattern and print an error and exit the program
    elif re.search(r'\D',n):
        print("Error: You didn't enter a valid number!")
    # If everything is good, we make -n- an integer to use later on
    else:
        n=int(n)
        break
# We make the user choose between three lettered amino acids and one lettered amino acids
while True:
    letterchoice=input('''\nHow would you like to view the amino acids?
    1: One letter amino acids
    2: Three letters amino acids
    ''')
    # Same error handling
    if letterchoice=='':
        print("Error: You didn't choose an amino acid view!")
    elif letterchoice not in ['1','2']:
        print("\nError: Your entry isn't from the choices above!\n")
    else:
        break
# Those are the dictionaries of the codes and the three letters to one letter amino acid dictionary
# End of dictionaries is at line 749
standard={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)|TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
vertebrate_mitochondria={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)|AG(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TGG|TGA',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C)',
'Met':r'AT(G|A)',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
yeast_mitochondria={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)',
'Ser':r'TC(A|G|T|C)|AG(T|C|A|G)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TGG|TGA',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C)',
'Met':r'AT(G|A)',
'Thr':r'AC(A|G|T|C)|CT(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
mo_pro_co_mito_myco_spiro={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'AGC|AGT',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TGG|TGA',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'AGA|AGG',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
invertebrate_mitochondria={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'AG(A|G|T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TGG|TGA',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|T|C|G)',
'Ile':r'AT(T|C)',
'Met':r'AT(A|G)',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
cil_das_hexamita={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'TA(A|G)|CA(A|G)',
'Arg':r'CG(A|T|C|G)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
echino_flat={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C|A|G)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C|A)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|T|C|G)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C|A)',
'Lys':r'AAG',
'_X_':r'N'}
euplotid_nuclear={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C|A)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|T|C|G)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
bact_arch_plnt_plst={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)|TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
alt_yeast_nuc={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)|CTG',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)|TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
ascid_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)|AG(A|G)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C)',
'Met':r'AT(G|A)',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
alter_flat_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)',
'Ser':r'TC(A|G|T|C)|AG(T|C|A|G)',
'Tyr':r'TA(T|C|A)',
'Ter':r'TAG',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C|A)',
'Lys':r'AAG',
'_X_':r'N'}
chl_phy_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)|TAG',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TAA|TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
trema_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)',
'Ser':r'TC(A|G|T|C)|AG(T|C|A|G)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C)',
'Met':r'AT(A|G)',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C|A)',
'Lys':r'AAG',
'_X_':r'N'}
scen_obliq={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)|TAG',
'Ser':r'TC(G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'T(C|A|G)A',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
thraus_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TTG|CT(A|T|C|G)',
'Ser':r'TC(G|T|C|A)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'T(A|T|G)A|TAG',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
ptero_branc_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C|G)',
'Ser':r'TC(G|T|C|A)|AG(T|C|A)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)|AGG',
'_X_':r'N'}
candi_divis_gracil={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)|TGA',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
pachy_tanno={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)|CTG',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TA(A|G)|TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
karyorelict={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Cys':r'TG(T|C)',
'Trp':r'TG(G|A)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'(T|C)A(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
condylostoma={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'(T|C)A(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
mesodinium={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(A|G|T|C)',
'Ter':r'TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
peritrich={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'(G|T)A(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Ter':r'TGA',
'Cys':r'TG(T|C)',
'Trp':r'TGG',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
blastocrithidia={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'(T|G)A(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(T|C)',
'Tyr':r'TA(T|C)',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)|AG(A|G)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)',
'_X_':r'N'}
cephalo_mito={'Val':r'GT(A|G|T|C)',
'Ala':r'GC(A|G|T|C)',
'Asp':r'GA(T|C)',
'Glu':r'GA(G|A)',
'Gly':r'GG(A|G|T|C)',
'Phe':r'TT(T|C)',
'Leu':r'TT(A|G)|CT(A|G|T|C)',
'Ser':r'TC(A|G|T|C)|AG(A|T|C)',
'Tyr':r'TA(T|C|A)',
'Ter':r'TAG',
'Cys':r'TG(T|C)',
'Trp':r'TG(A|G)',
'Pro':r'CC(A|G|T|C)',
'His':r'CA(T|C)',
'Gln':r'CA(A|G)',
'Arg':r'CG(A|G|T|C)',
'Ile':r'AT(T|C|A)',
'Met':r'ATG',
'Thr':r'AC(A|G|T|C)',
'Asn':r'AA(T|C)',
'Lys':r'AA(A|G)|AGG',
'_X_':r'N'}
replacement={'Val':'V',
'Ala':'A',
'Asp':'D',
'Glu':'E',
'Gly':'G',
'Phe':'F',
'Leu':'L',
'Ser':'S',
'Tyr':'Y',
'Cys':'C',
'Trp':'W',
'Pro':'P',
'His':'H',
'Gln':'Q',
'Arg':'R',
'Ile':'I',
'Met':'M',
'Thr':'T',
'Asn':'N',
'Lys':'K',
'_X_':'X'}
# A list of all the dictionaries
genetics=[standard,vertebrate_mitochondria,yeast_mitochondria,mo_pro_co_mito_myco_spiro,invertebrate_mitochondria,cil_das_hexamita,echino_flat,euplotid_nuclear,bact_arch_plnt_plst,alt_yeast_nuc,ascid_mito,alter_flat_mito,chl_phy_mito,trema_mito,scen_obliq,thraus_mito,ptero_branc_mito,candi_divis_gracil,pachy_tanno,karyorelict,condylostoma,mesodinium,peritrich,blastocrithidia,cephalo_mito]
# We make the selected codon as an index in the dictionaries list, and we assign it to -aa_aacodons-
aa_aacodons=genetics[int(genetic_code_num)-1]
# We create the file 'completeframes.txt' to write the final result
completeframes=open('completeframes.txt','w')
# We create 6 fasta files called orf_frame_n.fasta to write the DNA, mRNA and protein sequences of all frames in all sequences
orf_fasta1=open('orf_frame_1.fasta','w')
orf_fasta2=open('orf_frame_2.fasta','w')
orf_fasta3=open('orf_frame_3.fasta','w')
orf_fasta_r1=open('orf_frame_-1.fasta','w')
orf_fasta_r2=open('orf_frame_-2.fasta','w')
orf_fasta_r3=open('orf_frame_-3.fasta','w')
# We now define a function which will translate all 6 frames completely
def translate(dna,codes,n):
    rf=''
    # We loop through the range of the complete sequence and jump every 3 nucleotides
    for i in range(0,len(dna),3):
        # We loop through the items of the dictionaries, --aa-- is the amino acid and --aacodons-- is the pattern of the codon
        for aa,aacodons in codes.items():
            # if any pattern corresponds to the (dna[i+n:i+3+n]), which are every three codons, it will add the translated aa to --rf--
            if re.search(aacodons,dna[i+n:i+3+n]):
                rf+=aa
    # The function will return the translated frame completely
    return rf
# We now make a function to search for the open reading frames in all the reading frames
def orf_f(rf,cutoff):
    orffound=''
    fastawriter=''
    # We make an iterable object that has a specific pattern that searches for Methionine and the terminating sequences
    # It can also search for Methionine and no terminating sequence if the ORF ends at the end of the strand
    x=re.finditer(r'Met.*?Ter|Met.*',rf)
    # We iterate on every ORF, i.group() here is found ORF
    for i in x:
        # We choose the ORF that is bigger than the cutoff score (-n-)
        if len(i.group())>=cutoff:
            final=''
            # We remove the Ter word from the ORF (because the ORF doesn't contain a stop codon), and we assign it to --prefinal--
            prefinal=re.sub(r'Ter','',i.group())
            # We loop through a range of numbers in the --prefinal-- characters, and we jump every 3 characters
            for j in range(0,len(prefinal),3):
                # If we choose the one letter: we replace every three lettered aa by its one lettered aa, and we add it to --final-- and add a space after every aa
                if letterchoice=='1':
                    for three, one in replacement.items():
                        if re.search(three,prefinal[j:j+3]):
                            final+=one
                #If we choose three letters: we put every three letters (For example: Met) to --final-- and we add a space after every one.
                elif letterchoice=='2':
                    final+=prefinal[j:j+3]
            # --orffound-- now contains all the information related to the ORF and the protein translated, that will be written in the text file
            # --fastawriter-- now contains the DNA, RNA and protein sequence for the reading frame
            orffound+=dna_f[i.start():i.end()]+'\n'+"It's found in locations "+str(i.start()+1)+' to '+str(i.end())+'\n'+'Its length is '+str(len(dna_f[i.start():i.end()]))+'\n'+'Protein translated: '+final+'\n'+'Its length is: '+str(int(len(prefinal)/3))+'\n\n'
            fastawriter+=nameofseq+' (open reading frame sequence)'+'('+str(i.start()+1)+':'+str(i.end())+')'+'\n'+dna_f[i.start():i.end()]+'\n\n'+nameofseq+' (mRNA sequence)'+'('+str(i.start()+1)+':'+str(i.end())+')'+'\n'+dna_f[i.start():i.end()].replace('T','U')+'\n\n'+nameofseq+' (protein sequence)'+'('+str(i.start()+1)+':'+str(i.end())+')'+'\n'+final+'\n\n'
    # We return the value orffound
    return [orffound,fastawriter]
# A function for the reverse strand that has the same function like the one before it, we change in the location numbers because it is the reverse strand
def orf_r(rf,cutoff):
    orffound=''
    fastawriter=''
    x=re.finditer(r'Met.*?Ter|Met.*',rf)
    for i in x:
        if len(i.group())>=cutoff:
            final=''
            prefinal=re.sub(r'Ter','',i.group())
            for j in range(0,len(prefinal),3):
                if letterchoice=='1':
                    for three, one in replacement.items():
                        if re.search(three,prefinal[j:j+3]):
                            final+=one
                elif letterchoice=='2':
                    final+=prefinal[j:j+3]
            orffound+=dna_r[i.start():i.end()]+'\n'+"It's found in locations "+str(len(dna_f)-i.start())+' to '+str(len(dna_f)-i.end()+1)+'\n'+'Its length is '+str(len(dna_r[i.start():i.end()]))+'\n'+'Protein translated: '+final+'\n'+'Its length is: '+str(int(len(prefinal)/3))+'\n\n'
            fastawriter+=nameofseq+' (open reading frame sequence)'+'('+str(len(dna_f)-i.start())+':'+str(len(dna_f)-i.end()+1)+')'+'\n'+dna_r[i.start():i.end()]+'\n\n'+nameofseq+' (mRNA sequence)'+'('+str(len(dna_f)-i.start())+':'+str(len(dna_f)-i.end()+1)+')''\n'+dna_r[i.start():i.end()].replace('T','U')+'\n\n'+nameofseq+' (protein sequence)'+'('+str(len(dna_f)-i.start())+':'+str(len(dna_f)-i.end()+1)+')'+'\n'+final+'\n\n'
    return [orffound,fastawriter]
for i in range(0,len(seqs_final)):
    # Write in the text file each sequence name, a newline after it
    nameofseq=names[i]
    completeframes.write(nameofseq+'\n')
    # -dna_f- will be one of every sequence in loop
    dna_f=(seqs_final[i])
    # -dna_r- will be every reverse complementary strand, in order to get the start and stop codons from 5' to 3' in the 3' to 5' strand
    dna_r=dna_f[::-1].replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()
    # We define a function that will translate every frame completely, still without finding the open reading frames
    # --dna-- is either -dna_f- or -dna_r-, --codes-- is the genetic code, and --n-- is the frame number minus one

    # We change the number from zero to two in order to change the frame, and we assign the value of the frames to every possible frames
    # We add 'X' in frame 2 and 3 in both strands, to keep the position similar to the DNA strand
    rf1=translate(dna_f,aa_aacodons,0)
    rf2='X'+translate(dna_f,aa_aacodons,1)
    rf3='XX'+translate(dna_f,aa_aacodons,2)
    rfr1=translate(dna_r,aa_aacodons,0)
    rfr2='X'+translate(dna_r,aa_aacodons,1)
    rfr3='XX'+translate(dna_r,aa_aacodons,2)

    # Now we write this sentence in the file before we put every ORF in its specific frame
    completeframes.write("-Open reading frames found in frame 1 (5'-3'): "+'\n\n')
    completeframes.write(orf_f(rf1,n)[0])
    completeframes.write("-Open reading frames found in frame 2 (5'-3'): "+'\n\n')
    completeframes.write(orf_f(rf2,n)[0])
    completeframes.write("-Open reading frames found in frame 3 (5'-3'): "+'\n\n')
    completeframes.write(orf_f(rf3,n)[0])
    completeframes.write("-Open reading frames found in frame 1 (3'-5'): "+'\n\n')
    completeframes.write(orf_r(rfr1,n)[0])
    completeframes.write("-Open reading frames found in frame 2 (3'-5'): "+'\n\n')
    completeframes.write(orf_r(rfr2,n)[0])
    completeframes.write("-Open reading frames found in frame 3 (3'-5'): "+'\n\n')
    completeframes.write(orf_r(rfr3,n)[0])
    # Now we write in the 6 fasta files
    orf_fasta1.write(orf_f(rf1,n)[1])
    orf_fasta2.write(orf_f(rf2,n)[1])
    orf_fasta3.write(orf_f(rf3,n)[1])
    orf_fasta_r1.write(orf_r(rfr1,n)[1])
    orf_fasta_r2.write(orf_r(rfr2,n)[1])
    orf_fasta_r3.write(orf_r(rfr3,n)[1])
print('''\nThanks for using the ORF finder tool, Valar Morghulis.

Press enter to save the files''')
enter_to_finish=input('')
