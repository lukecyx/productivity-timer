import simpleaudio as sa
import time


CYMBALS_WAV = "./cymbals.wav"
BIG_BEN_WAV = "./chime_big_ben.wav"
CHEERING_WAV = "./cheering.wav"
INTERVAL_TIME = (1 * 60) * 20  # 20 minutes.
INTERVAL_TIME = 3
INTERVAL_BREAK_TIME = 20  # 20 seconds.
INTERVAL_BREAK_TIME = 5
INTERVAL_BLOCK_BREAK_TIME = (1 * 60) * 30  # 30 minutes.
INTERVAL_BLOCK_BREAK_TIME = 10


def create_wav_obj(wav_file: str) -> sa.WaveObject:
    wav_obj = sa.WaveObject.from_wave_file(wav_file)
    return wav_obj


def time_loop(
    interval_sound: sa.WaveObject,
    break_end_sound: sa.WaveObject,
    interval_block_break_sound: sa.WaveObject,
) -> None:
    interval_count = 0
    while True:
        print("main interval....")
        interval_count += 1
        time.sleep(INTERVAL_TIME)
        interval_sound.play()

        while True:
            print("interval break....")
            time.sleep(INTERVAL_BREAK_TIME)
            break_end_sound_play = break_end_sound.play()
            break_end_sound_play.wait_done()
            break

        # 30 min break
        while interval_count == 3:
            print("interval block break ...")
            time.sleep(INTERVAL_BLOCK_BREAK_TIME)
            interval_block_break_sound_play = interval_block_break_sound.play()
            interval_block_break_sound_play.wait_done()
            interval_count = 0
            break


def main():
    interval_sound = create_wav_obj(CYMBALS_WAV)
    break_end_sound = create_wav_obj(BIG_BEN_WAV)
    interval_block_break_sound = create_wav_obj(CHEERING_WAV)

    time_loop(interval_sound, break_end_sound, interval_block_break_sound)


if __name__ == "__main__":
    main()
