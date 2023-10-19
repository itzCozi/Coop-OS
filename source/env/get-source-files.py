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
  os.system(f'powershell {cd_command};{clone_command}')
  os.rename(f'{out_dir}/Coop-OS', f'{out_dir}/git_clone')
  if not os.path.exists(f'{out_dir}/src'):
    os.mkdir(f'{out_dir}/src')
  else:
    usr_input: str = input('\nDo you want to remove the current "src" directory? (y/n): ')
    if usr_input == 'y' or usr_input == 'yes':
      shutil.rmtree(f'{out_dir}/src')
      os.mkdir(f'{out_dir}/src')
    else:
      print('Not removing the current "src" directory will result in undefined behavior.')
      return None
    print(f'Current github version cloned to: {out_dir}/src')

  for file in os.listdir(f'{out_dir}/git_clone/source'):
    if os.path.isfile(f'{out_dir}/git_clone/source/{file}'):
      with open(f'{out_dir}/git_clone/source/{file}', 'r') as file_in:
        content: str = file_in.read()
      with open(f'{out_dir}/src/{file}', 'w') as file_out:
        file_out.write(content)

  shutil.rmtree(f'{out_dir}/git_clone')


def run_make_file() -> None:  # Idk if make works on my PC
  out_dir: str = 'C:/Users/coope/OneDrive/Desktop/Coop-OS/src'
  cd_command: str = f'cd {out_dir}'
  os.system(f'{cd_command};make compile.mk')


def individual_compile() -> None:
  src_dir: str = 'C:/Users/coope/OneDrive/Desktop/Coop-OS/src'
  out_dir: str = 'C:/Users/coope/OneDrive/Desktop/Coop-OS/build'
  cd_command: str = f'cd {src_dir}'
  for file in os.listdir(src_dir):
    if file == 'boot.s':
      build_command: str = 'C:/i686-elf-tools/bin/i686-elf-as boot.s -o boot.o'
    elif file == 'kernel.cpp':
      build_command: str = 'C:/i686-elf-tools/bin/i686-elf-g++ -c kernel.c++ -o kernel.o -ffreestanding -O2 -Wall -Wextra -fno-exceptions -fno-rtti'
    elif file == 'linker.ld':
      build_command: str = 'C:/i686-elf-tools/bin/i686-elf-g++ -T linker.ld -o myos.bin -ffreestanding -O2 -nostdlib boot.o kernel.o -lgcc'

    if 'build_command' in locals():
      os.system(f'{cd_command};{build_command}')
    else:
      print('A file in the "src" directory has not been coded into the compile function.')
      return None

clone_repository()
