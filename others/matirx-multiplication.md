#   Matrix Multiplication

##  Calculation Algorithm
*   Column First
*   Row First (Cache Friendly)
*   Strassen(n by n 정사각행렬에 n이 2의 제곱일 때만 성립)
*   Winograd

##  Implementation
*   ILP: AVX 등
*   TLP: pthread, openMP, opencl 등
*   CUDA

##  Tech Stack
*   language: C/C++, CUDA
*   build: CMake
*   test:  google test
*   benchmark: googleb benchmark
*   profiler: orbit / gprof / perf(linux)