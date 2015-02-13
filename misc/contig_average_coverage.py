import argparse
import sys

def coverage(args):
    cov = 0
    prevname = None
    name = None
    i = 0
    for line in args.covfile:
        if prevname:
            name = line.split('\t')[0]
            if name == prevname:
                cov = cov + float(line.split('\t')[1])
                i = i + 1
            else:
                sys.stdout.write(prevname)
                print '\t', round(cov/i, 1)
                cov = float(line.split('\t')[1])
                i = 1
        else:
            name = line.split('\t')[0]
            prevname = name
            i = i + 1
            cov = float(line.split('\t')[1])
        prevname = name
    sys.stdout.write(prevname)
    print '\t', round(cov/i, 1)




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Print average coverage to stdout. Provide a file with coverage per base on the format 'contigname[tab]coverage'")

    parser.add_argument("covfile", 
                    type = argparse.FileType('r'), 
                    help = "Name of the input coverage file", 
                    default = sys.stdin)
    args = parser.parse_args()

    coverage(args)

    args.covfile.close()
