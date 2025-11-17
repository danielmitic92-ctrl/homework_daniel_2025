def read_file_into_lines(file_path):
    """"
    read file and remove the character at the end
    """
    lines=[]
    with open (file_path,"r") as infile:
      for line in infile.readlines():
          cleaned=line.rstrip()
          lines.append(cleaned)
    return lines