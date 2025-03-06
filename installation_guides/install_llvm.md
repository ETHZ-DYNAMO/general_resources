# Installing LLVM

Following bash script will install LLVM 19.0

```bash
#!bin/bash

#
# Step 1: Clone the LLVM
#
git clone https://github.com/llvm/llvm-project -b release/19.x
cd llvm-project
mkdir -p build
cd build

# Create the folder for installation
INSTALL_PREFIX=../../llvm-19-install
mkdir -p $INSTALL_PREFIX

# Run CMAKE to configure the compilation
# If you want to target more backends, i.e. AMDGPU and NVIDIA GPU
# please change line 33 to
# -DLLVM_TARGETS_TO_BUILD="AMDGPU;NVPTX;host"
cmake -G Ninja ../llvm \
        -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ \
        -DLLVM_CCACHE_BUILD=ON -DLLVM_USE_LINKER=lld \
        -DCMAKE_INSTALL_PREFIX=$INSTALL_PREFIX \
        -DCMAKE_BUILD_TYPE=Release \
        -DLLVM_ENABLE_PROJECTS="mlir;clang;compiler-rt;lld;openmp" \
        -DOPENMP_ENABLE_LIBOMPTARGET=OFF \
        -DLLVM_ENABLE_ASSERTIONS=OFF \
        -DCLANG_ANALYZER_ENABLE_Z3_SOLVER=0 \
        -DLLVM_TARGETS_TO_BUILD="host" \
        -DLLVM_INCLUDE_BENCHMARKS=0 \
        -DLLVM_INCLUDE_EXAMPLES=0 \
        -DLLVM_INCLUDE_TESTS=0 \
        -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
        -DCMAKE_INSTALL_RPATH=$INSTALL_PREFIX/lib \
        -DLLVM_ENABLE_OCAMLDOC=OFF \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DLLVM_TEMPORARILY_ALLOW_OLD_TOOLCHAIN=OFF \
        -DLLVM_BUILD_LLVM_DYLIB=ON \
        -DLLVM_ENABLE_DUMP=OFF

# Build the LLVM project
ninja -j 4

# Install the llvm-project
ninja install
```