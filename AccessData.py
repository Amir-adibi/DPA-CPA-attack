from pathlib import Path

class AccessData:
    def __init__(self, trace='traces-00112233445566778899aabbccddeeff.bin', plaintext='plaintext_00112233445566778899aabbccddeeff.txt', number_of_traces=200, number_of_samples=370_000):
        self.data_directory = Path("dpa-master/Datasets/")
        self.trace_path = self.data_directory / trace
        self.plaintext_path = self.data_directory / plaintext

        self.number_of_traces = number_of_traces  # number of total traces
        self.number_of_samples = number_of_samples  # number of samples in each trace

    def __read_traces(self):
        file = open(self.trace_path, "rb")
        content = file.readline()  # whole data is represented in a single line
        file.close()
        return content

    def __preprocess_traces(self):
        content = self.__read_traces()
        traces = []

        # since while data is in a single line, we need to separate each trace
        # number of traces = len(content) / self.number_of_samples = self.number_of_traces
        for i in range(0, len(content), self.number_of_samples):
            temp = []
            for j in range(self.number_of_samples):
                temp.append(content[i+j])
            traces.append(temp)

        del content

        return traces

    def save_traces(self):
        traces = self.__preprocess_traces()

        with open('preprocessed_data/traces.txt', 'w') as f:
            for trace in traces:
                for num in trace:
                    f.write("%d " % num)
                f.write("\n")

        del traces

        print('Trace data has successfully written into the .txt file.')

    def __read_plaintext(self):
        file = open(self.plaintext_path, "r")
        lines = file.readlines()
        file.close()
        return lines

    def __preprocess_plaintext(self):
        lines = self.__read_plaintext()
        plaintext = []

        for line in lines:
            temp = []
            line = line.split()
            for num in line:
                temp.append(int(num, 16))
            if temp:
                plaintext.append(temp)

        del lines

        return plaintext

    def save_plaintext(self):
        plaintext = self.__preprocess_plaintext()

        with open('preprocessed_data/plaintext.txt', 'w') as f:
            for line in plaintext:
                for num in line:
                    f.write("%d " % num)
                f.write("\n")

        del plaintext

        print('Plaintext has successfully written into the .txt file.')

    @staticmethod
    def get_data():
        files = ['traces.txt', 'plaintext.txt']
        data = []

        for file in files:
            f = open("preprocessed_data/" + file, "r")
            lines = f.readlines()
            temp_data = []

            for line in lines:
                temp = []
                line = line.split()
                for num in line:
                    temp.append(int(num))
                if temp:
                    temp_data.append(temp)

            f.close()
            data.append(temp_data)

        return data

