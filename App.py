def hivideo_to_srt(video, output_filename='output.srt'):
    import assemblyai as aai

    aai.settings.api_key = "c33e44723b5e4c649e159cad63137d91"
    config = aai.TranscriptionConfig(language_code='hi')
    transcriber = aai.Transcriber(config=config)

    transcript = transcriber.transcribe(video)

    subs = transcript.export_subtitles_srt()

    # Save the subtitles to a text file
    with open(output_filename, 'w') as file:
        file.write(subs)

    print(f'Subtitles saved to {output_filename}')

# Example usage
hivideo_to_srt('Sirf_Ek_Hi_Bandaa_Kaafi_Hai_HIN_AD_DX_20.mp3', 'music.srt')

# https://www.assemblyai.com/docs/speech-to-text/speech-recognition#export-srt-or-vtt-caption-files
# https://github.com/openai/whisper

