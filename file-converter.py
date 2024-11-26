import markdown
import sys


def markdown2HTML(inputfile, outputfile):
    """
    Convert .md to .html file

    Args: 
        inputfile (str or Path): markdown file path
        outputfile (str or Path): html file path to be created
    
    Returns:
        None
    """
    with open(inputfile, 'r') as f_in:
        with open(outputfile, 'a') as f_out: 
            for line in f_in:
                markdowned_line = markdown.markdown(line)
                print(markdowned_line, file=f_out)


# From CLI, getting some info
args = sys.argv
command = args[1]
inputfile = args[2]
outputfile = args[3]

# check command and Converting .md to .html
match command:
    case 'markdown':
        markdown2HTML(inputfile, outputfile)
