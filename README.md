# Select gene by AF use two breed AF difference to find specific position in gene CDS region   
1.First you need use select_gene_new_pos.py to get ref pos and alt pos for second step.  
2.Second you need put two pos in select_gene_gz.py ,you also can change AF in this step to find your ideal result.  
3.Last step you can use second output to run get_CDSregion.py to get gene name at all position in gene CDS region.  
4.It write by python3.9.  
## Requirment
1.Phase file split by chrom.   
2.Genome gff file.
3.Python 3.0 or above.
