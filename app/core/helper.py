from .stream_processor import StreamProcessor
from .match import Match
from ..config import SAMPLE_RATE, FRAME_RATE, HOP_LENGTH, CHUNK_SIZE, N_FFT


def start_performance_following(piece_path):
    sp = StreamProcessor(SAMPLE_RATE, CHUNK_SIZE, hop_length=HOP_LENGTH, n_fft=N_FFT, verbose=False, query_norm=None)
    match = Match(sp, piece_path, window_size=FRAME_RATE*3, verbose=False, hop_length=HOP_LENGTH, max_run_count=3, ref_norm=None)
    match.run()
