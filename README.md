# STT_whisper
transform audio file to txt file with some useful methods.

## GitHub link
[OpenAI Whisper GitHub](https://github.com/openai/whisper)

## sample WAV file
[Example.wav](https://prod-files-secure.s3.us-west-2.amazonaws.com/9360b562-ba34-452b-9511-b012aa4378d1/fc0dcca2-62e9-4dfc-90f0-5573d3085590/example.wav)

## preparation

1. OpenAI Whisper package install:
    ```bash
    pip install -U openai-whisper
    ```

2. install whisper from Whisper GitHub:
    ```bash
    pip install git+https://github.com/openai/whisper.git
    ```

3. install FFmpeg:
    - [FFmpeg download link](https://ffmpeg.org/download.html#build-windows)
    - Linux:
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```

4. install Rust setuptools:
    ```bash
    pip install setuptools-rust
    ```

## How to run the code?

### 1. command line
```bash
whisper [wave file] —language Korean —model [tiny, small, medium, large] —output_format [txt]
```

### 2. Python code
1. upload wave data in `STT_whisper > speech_data > wave`
2. open `STT_whisper > speech_to_text_dir.py` file , and modify "(customize)" line
3. run the code in terminal:
    ```bash
    python STT_whisper/speech_to_text_dir.py
    ```

## Execution Results

1. The number and names of files in the specified directory are displayed.
2. The time taken to process each file is shown.
3. The final runtime is presented.
4. In the customized directory, `txt` file (containing text data in a single line) and `rm.txt` file (data separated into sentences) are generated.





