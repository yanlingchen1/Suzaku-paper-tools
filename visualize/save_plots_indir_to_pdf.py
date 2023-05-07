
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# set the path to the directory containing the plots
plot_dir = "/Users/eusracenorth/Documents/suzaku_A222-223/xmm_data/merged/2023-05-04/png/2023-05-04"

# get a list of all files in the directory
files = os.listdir(plot_dir)
# create a PDF object
pdf = PdfPages(f"{plot_dir}/profiles_sep_instruments_bands_obs_2023-05-04.pdf")

# loop over all files in the directory
for file in files:
    # check if the file is a plot (i.e. has a ".png" extension)
    if file.endswith(".png"):
        # load the plot into memory
        plot_dat = plt.imread(os.path.join(plot_dir, file))
        # add the plot to the PDF object
        plt.imshow(plot_dat)
        plt.xticks([])
        plt.yticks([])
        pdf.savefig()
        plt.close()

# close the PDF object
pdf.close()
