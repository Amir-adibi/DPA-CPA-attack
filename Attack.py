# First S-box
import numpy as np
from AccessData import *
from Plot import *

s_box = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

# Byte Hamming Weight Table
hamming_weight_8bit_table = [
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]


class Attack:

    def __init__(self, traces, plaintexts, offset=45000, end_offset=330_000):
        self.traces = np.array(traces)  # 200 x 370,000
        self.plaintexts = np.array(plaintexts)

        self.number_of_traces = self.traces.shape[0]  # number of traces
        self.trace_size = self.traces.shape[1]  # number of samples in each trace

        self.offset = offset  # beginning of encryption process in power trace
        self.end_offset = end_offset
        self.segment_len = (end_offset - offset) // 10  # length of one round of power trace

        self.columns = 16  # each plaintext is 16-bytes
        self.rows = self.traces.shape[0]  # there are 200 plaintexts, hence 200 rows

    def dpa_attack(self):
        res = []

        for byte in range(16):  # the key is 16 bytes, at each step we try to break one byte of the key
            candidates = []

            for key in range(256):  # each byte of the key has 256 possibilities
                ones = np.array([0] * self.segment_len)
                zeros = np.array([0] * self.segment_len)

                count_ones = 0
                count_zeros = 0

                print('byte =', byte + 1, ', key =', key + 1)
                for i in range(self.number_of_traces):  # i = trace index
                    trace = self.traces[i][self.offset:self.offset + self.segment_len].reshape(1, self.segment_len)
                    xor = self.plaintexts[i][byte] ^ key
                    s_val = self.apply_sbox(xor)
                    hm = hamming_weight_8bit_table[s_val]

                    if hm > 4:
                        ones = ones + trace
                        count_ones += 1
                    else:
                        zeros = zeros + trace
                        count_zeros += 1

                delta = abs(ones / count_ones - zeros / count_zeros)
                candidates.append(np.max(delta))
            candidates = np.array(candidates)
            res.append(np.argmax(candidates))

        key = []
        for i in res:
            print(format(i, '08b'))
            key.append(format(i, '08b'))

        AccessData().save_key('key.txt', key)

    def cpa_attack(self):
        key = []
        mean_traces = np.mean(self.traces[:, self.offset:self.offset + self.segment_len], axis=0)

        for byte in range(16):
            corr = [0] * 256
            max_corr = [0] * 256

            for key_guess in range(256):
                print('Byte {} - Guess {} - Key {}'.format(byte + 1, key_guess + 1, key))

                hw = np.zeros(self.number_of_traces)

                # A hw (hamming weight) vector of size (self.number_of_traces, ) is created in the next part
                for i in range(self.number_of_traces):
                    xor = self.plaintexts[i][byte] ^ key_guess
                    iv = self.apply_sbox(xor)
                    hw[i] = hamming_weight_8bit_table[iv]

                # Now we need to calculate correlation coefficient between given hw and power traces
                # The formula for calculating correlation coefficient is as follows:
                # r = sigma((x[i] - mean(x))(y[i] - mean(y))) / sqrt(sigma((x[i] - mean(x))**2 (y[i] - mean(y))**2))

                numerator = np.zeros(self.segment_len)
                denominator_model = np.zeros(self.segment_len)
                denominator_measured = np.zeros(self.segment_len)
                mean_hw = np.mean(hw)
                # mean_traces = np.mean(self.traces[:][self.offset:self.offset + self.segment_len], axis=0)

                for i in range(self.number_of_traces):  # sigma
                    trace = self.traces[i][self.offset:self.offset + self.segment_len]
                    hw_diff = hw[i] - mean_hw  # x - mean(x)
                    trace_diff = trace - mean_traces  # y - mean(y)
                    numerator += hw_diff * trace_diff  # (x - x_bar)(y - y_bar)

                    denominator_model += hw_diff ** 2  # (x - x_bar)^2
                    denominator_measured += trace_diff ** 2  # (y - y_bar)^2

                corr[key_guess] = numerator / np.sqrt(denominator_model * denominator_measured)
                max_corr[key_guess] = max(abs(corr[key_guess]))

            key.append(format(np.argmax(max_corr), '08b'))
            print(key)

    @staticmethod
    def apply_sbox(idx):
        return s_box[idx]