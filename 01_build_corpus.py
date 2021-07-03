#   ----------------------------------------------------------------------
#   ------------------ BUILD AUDIO MOSAICING CORPUS ------------------------
#   ---------------------------------------------------------------------- 

# PATHS
audio_samples = '/Users/felipe-tovar-henao/Documents/Sample collections/PeimanKhosravi44'
output_path = '/Users/felipe-tovar-henao/Documents/Camus files/corpora/'
duration = None
hop_length = 512
frame_length = 1024

# ------------------ MAIN ------------------------
# MODULES
from camus import build_corpus, save_JSON
import os
import time

st = time.time()
audio_samples = os.path.realpath(audio_samples)

corpus_dictionary = build_corpus(audio_samples, 
                                frame_length=frame_length,
                                duration=duration,
                                hop_length=hop_length)

### WRITE JSON CORPUS
outname =  os.path.basename(audio_samples) + '_corpus.json'
outdir = os.path.realpath(output_path)
outpath = os.path.join(outdir, outname)
if not os.path.exists(outdir):
    os.mkdir(outdir)

print('...saving corpus {}...'.format(outname))
save_JSON(corpus_dictionary, outpath)

end = time.time()
print('\ncorpus built in {} seconds'.format(round(end-st, 2)))