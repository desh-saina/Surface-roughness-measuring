import cv2
from scipy import stats
from scipy.stats import pearsonr, spearmanr


img = cv2.imread(r"C:\Saina\MIT\Sophomore year\Spring 2025\UROP\Camera pics\9_micron_cropped_new.JPG")
rows = img.shape[0]
cols = img.shape[1]
arr = []
m = 0
for row in img:
    for pixel in row:
        v = round(0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2])
        if m < v:
            m = v
        arr.append(v)

frequencies = []
gray_levels = []
for i in range(256):
    frequencies.append(0)
    gray_levels.append(i)
for val in arr:
    frequencies[val] = frequencies[val] + 1


# Standard deviation

def std_dev(freq):
    big_n = sum(freq)
    big_x = sum([freq[i]*i for i in range(256)]) / big_n
    sq_sum = 0
    for i in range(256):
        fi = freq[i]
        sq_term = (i - big_x)**2
        sq_sum+= fi*sq_term
    
    sd = (sq_sum / (big_n - 1))**(1/2)
    return sd

standard_deviation = std_dev(frequencies)
print(f'{standard_deviation = }')

# Root mean square

def rmsValue(freq):
    big_n = sum(freq)
    fi_sq = 0
    for i in range(256):
        fi_sq += freq[i]**2
    rms = (fi_sq / big_n)**(1/2)
    return rms

rms = rmsValue(frequencies)
print(f'{rms = }')

ra = standard_deviation / rms
print(f'{ra = }')