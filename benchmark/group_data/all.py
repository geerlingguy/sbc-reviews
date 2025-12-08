# Inventory variables applied to all hosts.

# These two variables, when multiplied, should generally equal the core count.
hpl_ps = 1
hpl_qs = 4

# PHP version available in system package manager (used for PTS installation).
php_version = "8.3"

# Select from 'llama.cpp' or 'ollama'.
ai_benchmark = 'llama.cpp'

# llama.cpp build options (e.g. '-DGGML_VULKAN=1' or '-DGGML_CUDA=1')
# llama_cpp_build_opts = ''
llama_cpp_build_opts = '-DGGML_VULKAN=1'
# For Nvidia DGX Spark / GB10 systems:
# llama_cpp_build_opts = '-DGGML_CUDA=1 -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc'

# https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md
llama_bench_opts = '-n 128 -p 512,4096 -pg 4096,128 -ngl 99 -r 2'

# Select which models to benchmark. Ideally they will run entirely in VRAM.
# The `urls` list can include multiple URLs for larger multi-part models.
llama_cpp_models = {
  'tinyllama-1.1b-1t-openorca.Q4_K_M.gguf': {
    'urls': ['https://huggingface.co/TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF/resolve/main/tinyllama-1.1b-1t-openorca.Q4_K_M.gguf'],
    'size_in_gb': 0.7,
  },
  'Llama-3.2-3B-Instruct-Q4_K_M.gguf': {
    'urls': ['https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf'],
    'size_in_gb': 1.9,
  },
  # 'llama-2-13b.Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q4_K_M.gguf'],
  #   'size_in_gb': 7.4,
  # },
  # 'DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-14B-Q4_K_M.gguf'],
  #   'size_in_gb': 8.4,
  # },
  # 'gpt-oss-20b-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/unsloth/gpt-oss-20b-GGUF/resolve/main/gpt-oss-20b-Q4_K_M.gguf'],
  #   'size_in_gb': 11.6,
  # },
  # 'Qwen_Qwen3-30B-A3B-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/bartowski/Qwen_Qwen3-30B-A3B-GGUF/resolve/main/Qwen_Qwen3-30B-A3B-Q4_K_M.gguf'],
  #   'size_in_gb': 18.6,
  # },
  # 'Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf': {
  #   'urls': ['https://huggingface.co/bartowski/Meta-Llama-3.1-70B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-70B-Instruct-Q4_K_M.gguf'],
  #   'size_in_gb': 42.5,
  # },
  # 'gpt-oss-120b-Q4_K_M-00001-of-00002.gguf': {
  #   'urls': [
  #     'https://huggingface.co/unsloth/gpt-oss-120b-GGUF/resolve/main/Q4_K_M/gpt-oss-120b-Q4_K_M-00001-of-00002.gguf',
  #     'https://huggingface.co/unsloth/gpt-oss-120b-GGUF/resolve/main/Q4_K_M/gpt-oss-120b-Q4_K_M-00002-of-00002.gguf',
  #   ],
  #   'size_in_gb': 62.9,
  # },
}
