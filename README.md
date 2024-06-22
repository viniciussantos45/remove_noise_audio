## Remove Noise from Audio

Este projeto divide um arquivo de áudio em partes menores, aplica o DeepFilter para remover ruídos de cada parte, e depois combina as partes processadas em um novo arquivo de áudio.

### Requisitos

- Python 3.8 ou superior
- `pydub` (para manipulação de áudio)
- `deepFilter` (para remoção de ruídos)
- `ffmpeg` (necessário para `pydub`)

### Instalação

1. **Instale o `ffmpeg`:**
    
    - **Windows:** Baixe o instalador do [site oficial do FFmpeg](https://ffmpeg.org/download.html) e siga as instruções.
    - **macOS:** Use Homebrew:
        
        sh
        
        Copiar código
        
        `brew install ffmpeg`
        
    - **Linux:** Use o gerenciador de pacotes da sua distribuição. Por exemplo, no Debian/Ubuntu:
        
        sh
        
        Copiar código
        
        `sudo apt-get install ffmpeg`
        
2. **Clone este repositório:**
    
    sh
    
    Copiar código
    
    `git clone https://github.com/seu-usuario/remove-noise-audio.git cd remove-noise-audio`
    
3. **Crie um ambiente virtual e ative-o:**
    
    sh
    
    Copiar código
    
    `` python -m venv env source env/bin/activate  # No Windows use `env\Scripts\activate` ``
    
4. **Instale as dependências do Python:**
    
    sh
    
    Copiar código
    
    `pip install -r requirements.txt`
    
5. **Instale o `deepFilter`:**
    
    sh
    
    Copiar código
    
    `pip install git+https://github.com/Rikorose/DeepFilterNet.git`
    

### Uso

1. Coloque o arquivo de áudio que você deseja processar na pasta do projeto.
    
2. Execute o script `remove_noise_wav.py` com o nome do arquivo de áudio:
    
    sh
    
    Copiar código
    
    `python remove_noise_wav.py audio.wav`
    
    Isso irá:
    
    - Dividir o arquivo `audio.wav` em partes menores.
    - Aplicar o DeepFilter em cada parte para remover ruídos.
    - Combinar as partes processadas em um novo arquivo chamado `output.wav`.

### Estrutura do Projeto

bash

Copiar código

`remove-noise-audio/ ├── chunks/                # Pasta para armazenar os chunks de áudio divididos ├── processed_chunks/      # Pasta para armazenar os chunks de áudio processados ├── remove_noise_wav.py    # Script principal para remover ruídos do áudio ├── requirements.txt       # Lista de dependências do projeto └── README.md              # Este arquivo`

### Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode abrir um issue ou enviar um pull request no GitHub.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes..
