
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from glob import glob

today = '2023-05-07'
# set the path to the directory containing the plots
plot_dir = f"/Users/eusracenorth/Documents/suzaku_A222-223/xmm_data/merged/{today}_merge_obs_inst_bands/png/10am/{today}"

# get a list of all files in the directory
# files = os.listdir(plot_dir)
files = glob(f'{plot_dir}/*inclfila_bigeschipgapmasked.png')
# create a PDF object
os.system(f'rm {plot_dir}/inclfila_bigeschipgapmasked_{today}.pdf')
pdf = PdfPages(f"{plot_dir}/inclfila_bigeschipgapmasked_{today}.pdf")

# loop over all files in the directory
for file in files:
    # check if the file is a plot (i.e. has a ".png" extension)
    # if file.endswith(".png"):
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
