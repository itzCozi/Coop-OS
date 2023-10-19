# Gets all files in source from github repo and puts them in a folder
# for easy building so i dont have to copy and paste every thing
# EX: git clone <repository_url>

import os
import sys

def clone_repository() -> None:
  repo_url: str = 'https://github.com/itzCozi/Coop-OS'