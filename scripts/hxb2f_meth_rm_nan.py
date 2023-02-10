#!/usr/bin/env python3
"""Work with raefcon on github"""

import pandas as pd

__copyright__ = "Copyright (C) 2023-present, Raefcon & DV Klopfenstein, PhD. All rights reserved"
__author__ = "DV Klopfenstein, PhD"


def main():
    """Work with raefcon on github"""
    fin_tsv = 'data/hxb2f.meth.tsv'
    fout_tsv = 'data/hxb2f.meth_cleaned.tsv'
    fout_txt = 'data/hxb2f.meth_cleaned.txt'

    # Read tab-separated table into a Pandas dataframe
    dataframe = pd.read_csv(fin_tsv, sep='\t', header=None)
    print(f'  {dataframe.shape[0]:4} rows  READ: {fin_tsv}')

    # Add column headers to the Pandas dataframe
    dataframe.columns = _get_colhdrs()
    num_rows_orig = dataframe.shape[0]
    assert num_rows_orig == 4147, f'NUMBER OF ROWS({dataframe.shape[0]}) != 4147'
    #_prt_colhdrs(dataframe)

    # Remove rows with Nans (Not-a-Number) in column K or 11 (Percentage of modified bases)
    # https://www.datasciencelearner.com/pandas-dropna-remove-nan-rows-python/
    dataframe.dropna(subset=['PERC'], inplace=True)
    #_chk_numrows_cleaner(dataframe, num_rows_orig)
    _prt_colhdrs(dataframe)

    # Write .txt file to make it easier to open in Excel
    _wr_tsv(fout_txt, dataframe)
    _wr_tsv(fout_tsv, dataframe)




def _wr_tsv(fout, dataframe):
    """Write a tsv file"""
    dataframe.to_csv(fout, sep="\t", header=None, index=False)
    print(f'  {dataframe.shape[0]:4} rows WROTE: {fout}')

def _get_colhdrs():
    """Get column headers using information from data/hxb2f.meth.png"""
    return [
        'RNAME',    #  1 A reference sequence name
        'POS',      #  2 B 0-based start position
        'END',      #  3 C 0-based exclusive end position
        'METH',     #  4 D Abbreviated name of modified-base examined
        'SCORE',    #  5 E "Score" 1000*(...)
        'STRAND',   #  6 F Strand(of reference sequence). Forward "+", or reverse "-"
        'IGNORE0',  #  7 G Ignore, included simply for compatibility
        'IGNORE1',  #  8 H Ignore, included simply for compatibility
        'IGNORE2',  #  9 I Ignore, included simply for compatibility
        'COVERAGE', # 10 J Read coverage at reference position
        'PERC',     # 11 K Percentage of modified bases, as a proportion of canonical & modified
                    #      (no calls and filtered), substitutions, and deletions).
                    #      100 * Nmod/(Nmod + Ncanon)
    ]

def _prt_colhdrs(dataframe):
    """Print column headers in a dataframe"""
    hdr_int = list(dataframe.columns.values)
    hdr_abc = [chr(i) for i in range(ord('A'), ord('K') + 1)]
    hdr_istr = [f'{i:8}' for i in hdr_int]
    hdr_ichr = [f'{i:8}' for i in hdr_abc]
    print(f'''COLUMS: {" ".join(hdr_ichr)}''')
    print(f'''COLUMS: {" ".join(hdr_istr)}''')

def _chk_numrows_cleaner(dataframe, num_rows_orig):
    num_rows_cleaned = dataframe.shape[0]
    print(f'{num_rows_orig:4} rows in original table')
    print(f'{num_rows_cleaned:4} rows in table with Nan percentage of modified bases removed')
    assert num_rows_cleaned < num_rows_orig

if __name__ == '__main__':
    main()

# Copyright (C) 2023-present, Raefcon & DV Klopfenstein, PhD. All rights reserved
