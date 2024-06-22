import os
import sys
import subprocess
from pydub import AudioSegment

def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(file_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    
    os.makedirs('chunks', exist_ok=True)
    chunk_paths = []
    for i, chunk in enumerate(chunks):
        chunk_path = f'chunks/part_{i}.wav'
        chunk.export(chunk_path, format='wav')
        chunk_paths.append(chunk_path)
    return chunk_paths

def process_chunks_with_deepfilter(chunk_paths):
    processed_chunk_paths = []
    for chunk_path in chunk_paths:
        processed_chunk_path = chunk_path.replace('chunks', 'processed_chunks')
        os.makedirs(os.path.dirname(processed_chunk_path), exist_ok=True)
        
        # Run DeepFilter command
        subprocess.run(['deepFilter', '-d', '--log-level', 'debug', chunk_path, '-o', 'processed_chunks'])
        
        processed_chunk_paths.append(processed_chunk_path)
    return processed_chunk_paths

def numerical_sort(value):
    parts = value.split('_')
    number = parts[-2].split('.')[0]
    return int(number)

def combine_chunks(chunk_paths, output_path):
    combined_audio = AudioSegment.empty()
    for file_name in sorted(os.listdir('processed_chunks'), key=numerical_sort):
        if file_name.endswith('.wav'):
            chunk_path = os.path.join('processed_chunks', file_name)
            audio = AudioSegment.from_wav(chunk_path)
            combined_audio += audio
    combined_audio.export(output_path, format='wav')

def main(input_file):
    chunk_paths = split_audio(input_file)
    processed_chunk_paths = process_chunks_with_deepfilter(chunk_paths)
    combine_chunks(processed_chunk_paths, 'output.wav')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python remove_noise_wav.py audio.wav')
        sys.exit(1)
    input_file = sys.argv[1]
    main(input_file)
