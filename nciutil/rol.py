from pathlib import Path


def strip_rol_output(file_path: Path):
    """
    Reads a log file from a gadopt simulation extracting the lines
    associated with the rol status check. The output is written to a new file
    with the same name as the input file but with a .strip
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)
    file_path = file_path.resolve()

    # read the file and extract the relevant lines associated with rol
    output_lines = read_rol_statuscheck(file_path=file_path)

    # write the output to a new file with .strip suffix
    strip_finame = file_path.with_stem(file_path.stem + "_stripped")

    # write the output to the new file
    with strip_finame.open("w") as fo:
        fo.write(output_lines)

    return strip_finame


def read_rol_statuscheck(file_path: Path):
    """ Reads a log file from a gadopt simulation extracting the lines
    associated with the rol status check. The output is a string with the
    relevant lines.
    """
    # if file_path is a string convert it to a Path object
    if isinstance(file_path, str):
        file_path = Path(file_path)
    finame = file_path.resolve()

    # open the file and read the header line
    with finame.open() as fi:
        for line in fi:
            # find the header line: it has "gnorm" in it
            if "gnorm" in line:
                header_line = line
                break

        # number of outputs is the number of columns in the header line
        number_of_outputs = len(header_line.split())
        # read the rest of the file
        output_lines = "# " + header_line[2:]
        for line in fi:
            # if the line has the same number of columns as the header line
            if len(line.split()) == number_of_outputs:
                # add it to the output
                output_lines += line
    return output_lines
