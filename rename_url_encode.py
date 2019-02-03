from pathlib import Path
import urllib.parse
import os
import sys

class Rename:
  def __init__(self):
    pass

# rename directory name only
  def dir(self, path):
    self.d_path = path

    if self.d_path.is_dir():
      for p in self.d_path.iterdir():
        encoded = urllib.parse.quote(str(p))
        p.rename(encoded)
        self.dir(p)

# rename file name only
  def file(self, path):
    self.f_path = path

    if self.f_path.is_dir():
      for p in self.f_path.iterdir():
        self.file(p)

    elif self.f_path.is_file():
      encoded = urllib.parse.quote(str(self.f_path))
      print('[変換前] %s -> [変換後] %s ' % (self.f_path.name, encoded))


if __name__=='__main__':
  args = sys.argv

  if len(args) != 2:
    print("Let me input you want to translate directory!")
    print("ex: python3 rename_url_encode.py <dir1>")
    exit()


  _path = Rename()
  _path_obj = Path(args[1])
  _path.dir(_path_obj)
  _path.file(_path_obj)



