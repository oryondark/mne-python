"""
============================
Export evoked data to Nitime
============================

"""
# Author: Denis Engemann <d.engemann@fz-juelichde>
#         Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#
# License: BSD (3-clause)

print(__doc__)

from mne.fiff import read_evokeds, pick_types
from mne.datasets import sample
from nitime.viz import plot_tseries
import matplotlib.pyplot as plt


data_path = sample.data_path()

fname = data_path + '/MEG/sample/sample_audvis-ave.fif'

# Reading
evoked = read_evokeds(fname, condition=0, baseline=(None, 0), proj=True)

# Pick channels to view
picks = pick_types(evoked.info, meg='grad', eeg=False, exclude='bads')

evoked_ts = evoked.to_nitime(picks=picks)

plot_tseries(evoked_ts)

plt.show()
