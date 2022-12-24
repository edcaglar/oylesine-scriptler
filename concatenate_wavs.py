import os
import tqdm
from pydub import AudioSegment
import argparse
import sys

def concat_audio_files(source_path, destination_path, duration):

    labels = os.listdir(source_path)
    for label in tqdm.tqdm(labels):
        label_path = os.path.join(source_path, label)
        combined_signal = AudioSegment.empty()
        save_label = os.path.join(destination_path, label)
        os.mkdir(save_label)

        for wav_name in os.listdir(label_path):
            wav_file = os.path.join(label_path, wav_name)
            signal = AudioSegment.from_wav(wav_file)
            if  signal.duration_seconds + combined_signal.duration_seconds <= duration:
                combined_signal = combined_signal.append(signal, crossfade=False)
            else:
                overflow_idx = duration - combined_signal.duration_seconds
                #floating_signal = signal[(overflow_idx-1)*1000:-1] # gerek olursa sona gelen sinyallerin tasan kismi bosa gitmesin diye eklenebilir
                signal = signal[0:overflow_idx*1000]
                combined_signal = combined_signal.append(signal, crossfade=False)
                save_file =os.path.join(save_label, wav_name)
                combined_signal.export(save_file, format='wav')
                combined_signal = AudioSegment.empty()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Audio Concatenate")
    parser.add_argument('--source', '-s', type=str, required=True)
    parser.add_argument('--destination', '-d', type=str, required=True)
    parser.add_argument('--duration', '-t', help="time by seconds", type=float, required=True)

    args= parser.parse_args(sys.argv[1:])
    source_path = args.source
    destination_path = args.destination
    duration = args.duration
    #source_path = "Dev/"
    #destination_path = "Dev1min/"

    if(os.path.exists(source_path)):
        os.mkdir(destination_path)
        concat_audio_files(source_path, destination_path, duration)


