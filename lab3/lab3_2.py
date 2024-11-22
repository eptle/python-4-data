from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path


def histogram(image_path=''):
   image = Image.open(image_path)
   width = image.width
   height = image.height
   r, g, b = image.split()

   r_hist = r.histogram()
   g_hist = g.histogram()
   b_hist = b.histogram()        
   histogram = image.histogram()

   histograms = (r_hist, g_hist, b_hist, histogram)
   hist_names = ('red', 'green', 'blue', 'overall')

   try:
      Path.mkdir('lab3/histograms', exist_ok=True)
   except:
      pass

   for hist, name in zip(histograms, hist_names):
      fig, axe = plt.subplots(figsize=(width/400, height/400))
      if name == 'overall':
         axe.bar(range(len(hist)), hist, color='gray')
      else:
         axe.bar(range(len(hist)), hist, color=name)
      axe.set_xlim(0, 256)
      axe.set_title(f'{name} histogram')
      fig.savefig(f"lab3/histograms/{name}_hist.jpg")
      plt.close(fig)

   r_hist_img = Image.open('lab3/histograms/red_hist.jpg')
   g_hist_img = Image.open('lab3/histograms/green_hist.jpg')
   b_hist_img = Image.open('lab3/histograms/blue_hist.jpg')
   hist_img = Image.open('lab3/histograms/overall_hist.jpg')

   canvas = Image.new('RGB', (width + width//4, height))
   canvas.paste(image, (0, 0))
   canvas.paste(hist_img, (width, 0))
   canvas.paste(r_hist_img, (width, height//4))
   canvas.paste(g_hist_img, (width, height//2))
   canvas.paste(b_hist_img, (width, height//4*3))
   canvas.show()

if __name__ == '__main__':
   path = 'lab2/src/nature.jpg'
   histogram(path)