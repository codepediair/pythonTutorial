import math

import matplotlib.pyplot as plt
import librosa.display
import numpy as np


# binary search
import pygame


def bin_search(arr, target):
    index = int(len(arr) / 2)
    min_index = 0
    max_index = len(arr) - 1
    found = False

    if target < arr[0]:
        return 0
    
    if target > arr[len(arr) - 1]:
        return len(arr) - 1

    while not found:

        if min_index == len(arr) - 2:
            return len(arr) - 1

        if arr[index] < target < arr[index + 1] or arr[index] == target:
            return index

        if arr[index] > target:
            max_index = index
        else:
            min_index = index

        index = int((min_index + max_index) / 2)

def rotate(xy, theta):
    # https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions
    cos_theta, sin_theta = math.cos(theta), math.sin(theta)

    return (
        xy[0] * cos_theta - xy[1] * sin_theta,
        xy[0] * sin_theta + xy[1] * cos_theta
    )


def translate(xy, offset):
    return xy[0] + offset[0], xy[1] + offset[1]


def clamp(min_value, max_value, value):

    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


class AudioAnalyzer:

    def __init__(self):

        self.frequencies_index_ratio = 0
        self.time_index_ratio = 0 
        self.spectrogram = None 

    def load(self, filename):

        time_series, sample_rate = librosa.load(filename)
        stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

        self.spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

        frequencies = librosa.core.fft_frequencies(n_fft=2048*4)
        times = librosa.core.frames_to_time(np.arange(self.spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)

        self.time_index_ratio = len(times)/times[len(times) - 1]

        self.frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]




    def show(self):

        librosa.display.specshow(self.spectrogram,
                                 y_axis='log', x_axis='time')

        plt.title('spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
        plt.show()

    def get_decibel(self, target_time, freq):

        return self.spectrogram[int(freq*self.frequencies_index_ratio)][int(target_time*self.time_index_ratio)]

        # returning the current decibel according to the indexes which found by binary search
        # return self.spectrogram[bin_search(self.frequencies, freq), bin_search(self.times, target_time)]

    def get_decibel_array(self, target_time, freq_arr):

        arr = []

        for f in freq_arr:
            arr.append(self.get_decibel(target_time,f))

        return arr


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):

        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)

    def render(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))


class AverageAudioBar(AudioBar):

    def __init__(self, x, y, rng, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):
        super().__init__(x, y, 0, color, width, min_height, max_height, min_decibel, max_decibel)

        self.rng = rng

        self.avg = 0

    def update_all(self, dt, time, analyzer):

        self.avg = 0

        for i in self.rng:
            self.avg += analyzer.get_decibel(time, i)

        self.avg /= len(self.rng)
        self.update(dt, self.avg)


class RotatedAverageAudioBar(AverageAudioBar):

    def __init__(self, x, y, rng, color, angle=0, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):
        super().__init__(x, y, 0, color, width, min_height, max_height, min_decibel, max_decibel)

        self.rng = rng

        self.rect = None

        self.angle = angle


    def render(self, screen):

        pygame.draw.polygon(screen, self.color, self.rect.points)

    def render_c(self, screen, color):

        pygame.draw.polygon(screen, color, self.rect.points)

    def update_rect(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)

        self.rect.rotate(self.angle)


class Rect:

    def __init__(self,x ,y, w, h):
        self.x, self.y, self.w, self.h = x,y, w, h

        self.points = []

        self.origin = [self.w/2,0]
        self.offset = [self.origin[0] + x, self.origin[1] + y]

        self.rotate(0)

    def rotate(self, angle):

        template = [
            (-self.origin[0], self.origin[1]),
            (-self.origin[0] + self.w, self.origin[1]),
            (-self.origin[0] + self.w, self.origin[1] - self.h),
            (-self.origin[0], self.origin[1] - self.h)
        ]

        self.points = [translate(rotate(xy, math.radians(angle)), self.offset) for xy in template]

    def draw(self,screen):
        pygame.draw.polygon(screen, (255,255, 0), self.points)
