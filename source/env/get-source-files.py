# Gets all files in source from github repo and puts them in a folder
# for easy building so i dont have to copy and paste every thing
# EX: git clone <repository_url>

import os
import sys
import shutil

def clone_repository() -> None:
  repo_url: str = 'https://github.com/itzCozi/Coop-OS'
  out_dir: str = 'C:/Users/coope/OneDrive/Desktop/Coop-OS'
  cd_command: str = f'cd {out_dir}'
  clone_command: str = f'git clone {repo_url}'