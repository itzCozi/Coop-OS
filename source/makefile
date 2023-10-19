all: boot kernel linker

boot: boot.s
  C:/i686-elf-tools/bin/i686-elf-as boot.s -o boot.o

kernel: kernel.cpp
  C:/i686-elf-tools/bin/i686-elf-g++ -c kernel.c++ -o kernel.o -ffreestanding -O2 -Wall -Wextra -fno-exceptions -fno-rtti

linker: linker.ld
	C:/i686-elf-tools/bin/i686-elf-gcc -T linker.ld -o myos.bin -ffreestanding -O2 -nostdlib boot.o kernel.o -lgcc
