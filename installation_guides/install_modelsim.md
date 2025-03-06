# Installing ModelSim on Ubuntu

> Tested on Ubuntu 20.04

> If you only need Modelsim please directly check ***Dependencies needed for Modelsim*** Section


## Steps:

- Download corresponding files from https://fpgasoftware.intel.com/

  - Both Standard and Lite edition will be fine.

  - Please choose version ***20.1***. If you choose the latest one, it will be Questa instead of Modelsim(The functionality for those two apps are almost the same, Questa supports System Verilog better than Modelsim). Thus, you'll need to change the scripts.

  - Both **Complete Download** or **Individual Files** are fine (But most of the time you don't need Complete Download)

- Just click on the `QuartusSetup.XXX.run` you just downloaded. It will install Modelsim as well.

## Dependencies needed for Modelsim:

> Based on documentation given by Intel, lots of packages need to be installed to run Modelsim (even some pretty old 32-bit version libraries....)

> Install libc6:i386, libncurses5:i386, libxtst6:i386, libxft2:i386, libc6:i386, libncurses5:i386, libstdc++6:i386, libc6-dev-i386 libxft2, lib32z1, lib32ncurses5, lib32bz2-1.0, and libpng12 libraries

> Please check this [blog](https://vhdlwhiz.com/modelsim-quartus-prime-lite-ubuntu-20-04/) for detailed steps of installing all those dependencies (**don't use sudo to run the script from VHDLwhiz.com!**)


## Versioning

Modelsim version shipped with Quartus version

`ModelSim 10.5b : Quartus Prime 17.1`

## Potential Problems:

1. After clicking `QuartusSetup.XXX.run`, it says `Could Not Display "QuartusSetup-XXX-linux.run`.

   - When you are using a completely new Ubuntu machine(VM), it will show things like that.

   - Right click on the corresponding folder, open the terminal, and type the following command:

     - `chmod +x ./name_of_the_file`

     - `sudo ./name_of_the_file`

2. No permission to run quartus or modelsim

   - Enter `Installation_path/intelFPGA/20.1/bin/`

   - Open terminal, type `chmod 744 *`

   - The same for modelsim

3. Error when building freetype on new Debian machine: `configure: error: C compiler cannot create executables`
   - `sudo apt install gcc-multilib`

4. Can not install `lib32gcc1`, use the following command instead:
   ```
   sudo apt-get install libgcc1
   ```
## Working Match Between Vivado and Free ModelSim Versions:

Compiling simulation library for modelsim

| Vivado | ModelSim |
| --     | --       |
| [2019.1](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html) | [2020.1](https://www.intel.com/content/www/us/en/software-kit/750511/modelsim-intel-fpgas-pro-edition-software-version-20-1.html)   |

## Sample script

```bash
#!/bin/bash
# Install modelsim for ubuntu machine:
# https://vhdlwhiz.com/modelsim-quartus-prime-lite-ubuntu-20-04/ start with
# ModelSimSetup-*-linux in your home directory Open a terminal in your home
# directory Update your system
sudo dpkg --add-architecture i386
sudo apt-get update; sudo apt-get upgrade

sudo apt-get install -y build-essential gcc-multilib g++-multilib lib32z1 \
	lib32stdc++6 lib32gcc-s1 libxt6:i386 libxtst6:i386 expat:i386 fontconfig:i386 \
	libfreetype6:i386 libexpat1:i386 libc6:i386 libgtk-3-0:i386 libcanberra0:i386 \
	libice6:i386 libsm6:i386 libncurses5:i386 zlib1g:i386 libx11-6:i386 \
	libxau6:i386 libxdmcp6:i386 libxext6:i386 libxft2:i386 libxrender1:i386

# Run the installer (change the version of the installer to the appropriate
# version, but we recommend 20.1)
INSTALLER=~/ModelSimSetup-20.1.0.711-linux.run
chmod +x $INSTALLER
$INSTALLER

# Make the vco script writable
chmod u+w ~/intelFPGA/*.*/modelsim_ase/vco

# Make a backup of the vco file
(cd ~/intelFPGA/*.*/modelsim_ase/ && cp vco vco_original)

# Edit the vco script manually, or with these commands:
sed -i 's/linux\_rh[[:digit:]]\+/linux/g' ~/intelFPGA/*.*/modelsim_ase/vco
sed -i 's/MTI_VCO_MODE:-""/MTI_VCO_MODE:-"32"/g' ~/intelFPGA/*.*/modelsim_ase/vco
sed -i '/dir=`dirname "$arg0"`/a export LD_LIBRARY_PATH=${dir}/lib32' ~/intelFPGA/*.*/modelsim_ase/vco

# Check that the correct lines have changed
diff ~/intelFPGA/*.*/modelsim_ase/vco ~/intelFPGA/*.*/modelsim_ase/vco_original

# Download the old 32-bit version of libfreetype
[ -f "freetype-2.4.12.tar.bz2" ] || wget https://ftp.osuosl.org/pub/blfs/conglomeration/freetype/freetype-2.4.12.tar.bz2
tar xjf freetype-2.4.12.tar.bz2

# Compile libfreetype
cd freetype-2.4.12/
./configure --build=i686-pc-linux-gnu "CFLAGS=-m32" "CXXFLAGS=-m32" "LDFLAGS=-m32"
make clean && make

cd ~/intelFPGA/*.*/modelsim_ase/
mkdir lib32
cp ~/freetype-2.4.12/objs/.libs/libfreetype.so* lib32/

# Run the vsim script to start ModelSim
cd ~
~/intelFPGA/*.*/modelsim_ase/bin/vsim

```
