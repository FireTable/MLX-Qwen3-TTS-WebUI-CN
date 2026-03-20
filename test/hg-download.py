from huggingface_hub import snapshot_download
import os

models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(models_dir, exist_ok=True)

models = [
    'mlx-community/chatterbox-turbo-fp16',
    'mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16',
    'mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-bf16',
    'mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16',
]

for model_id in models:
    local_folder = os.path.join(models_dir, model_id.replace('mlx-community/', ''))
    if os.path.exists(local_folder):
        print(f'Skipping {model_id} (already exists)')
        continue
    print(f'Downloading {model_id}...')
    snapshot_download(repo_id=model_id, local_dir=local_folder, local_dir_use_symlinks=False)
    print(f'Done: {local_folder}')

print('All models downloaded!')
