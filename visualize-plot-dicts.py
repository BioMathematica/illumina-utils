# -*- coding: utf-8 -*-

import os
import sys
import cPickle

sys.path.append('/bioware/seqinfo/illumina-utils/')
import fastqlib as u

def main(plot_dict, figure_dest, title = None, split_tiles = False):
    u.visualize_qual_stats_dict(plot_dict, figure_dest, title, split_tiles)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Visualize Plot Dicts')
    parser.add_argument('plot_dict', metavar = 'PLOT_DICT',
                                        help = 'cPickle dictionary that contains quality score info ready for plotting')
    parser.add_argument('-d', '--dest', metavar = 'DEST_FILE', default = None,
                                        help = 'Figure destination')
    parser.add_argument('--title', metavar = 'TITLE', default = None,
                                        help = 'Title to appear at the top of the figure')
    parser.add_argument('--split-tiles', action = 'store_true', default = False,
                                        help = 'When set, quality curves will be shown separately for each tile')

    args = parser.parse_args()
    
    plot_dict = cPickle.load(open(args.plot_dict))
    dest = args.dest if args.dest else args.plot_dict
    title = args.title if args.title else os.path.basename(args.plot_dict)
    split_tiles = args.split_tiles

    main(plot_dict, dest, title, split_tiles)

