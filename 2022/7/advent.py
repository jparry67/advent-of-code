class Solution():
  def populate_directories(self, directories, curr_dir):
    curr = directories
    for dir in curr_dir:
      if dir not in curr:
        curr[dir] = {}
        curr[dir]['size'] = 0
      curr = curr[dir]
    return directories

  def populate_sizes(self, directories, curr_dir, file_name, size):
    curr = directories
    for dir in curr_dir:
      curr = curr[dir]
      curr['size'] += size
      if dir == curr_dir[-1]:
        curr[file_name] = size
    return directories

  def find_smallest_directory_sizes(self, directories):
    if type(directories) is not dict:
      return []
    sizes = []
    for k in directories.keys():
      if k == 'size':
        if directories[k] < 100000:
          sizes.append(directories[k])
      else:
        sizes.extend(self.find_smallest_directory_sizes(directories[k]))
    return sizes
    
  def possible_directory_to_delete(self, directories, space_needed):
    if type(directories) is not dict:
      return []
    sizes = []
    for k in directories.keys():
      if k == 'size':
        if directories[k] > space_needed:
          sizes.append(directories[k])
      else:
        sizes.extend(self.possible_directory_to_delete(directories[k], space_needed))
    return sizes


  def run(self, input):
    answer = 0
    directories = {}
    curr_dir = []
    for line in input.split('\n'):
      if line[:4] == '$ cd':
        if line[5:] == '..':
          curr_dir.pop()
        else:
          curr_dir.append(line[5:])
        directories = self.populate_directories(directories, curr_dir)
      elif line == '$ ls':
        pass
      else:
        first,second = line.split()
        if first == 'dir':
          curr_dir.append(second)
          directories = self.populate_directories(directories, curr_dir)
          curr_dir.pop()
        else:
          directories = self.populate_sizes(directories, curr_dir, second, int(first))
    answer = sum(self.find_smallest_directory_sizes(directories))

    filesystem_size = 70000000
    needed_space = 30000000
    unused_space = filesystem_size - directories['/']['size']
    amount_to_delete = needed_space - unused_space
    answer = min(self.possible_directory_to_delete(directories, amount_to_delete))
    return answer