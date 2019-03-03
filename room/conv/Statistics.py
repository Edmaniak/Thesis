class StatisticalRecord:
    def __init__(self, core, object_class, accuracy=0):
        self.core = core,
        self.object_class = object_class
        self.accuracy = accuracy


class TrainingStatistics:
    def __init__(self, convolution_cores=[], object_classes=[]):
        self.history_accuracy = []
        self.convolution_cores = convolution_cores
        self.object_classes = object_classes

    def add_core_class(self, record: StatisticalRecord, accuracy=None):
        if accuracy is not None:
            record.accuracy = accuracy
        self.history_accuracy.append(record)

    def get_average_accuracy(self):
        total_sum = 0
        for record_i in range(0, len(self.history_accuracy)):
            total_sum += self.history_accuracy[record_i].accuracy
        return total_sum / len(self.history_accuracy)

    def print_summary(self):
        average = self.get_average_accuracy()
        for record in self.history_accuracy:
            print(
                "CORE: " + self.get_convolution_core_by_key(record.core) + " | Class: " + self.get_object_class_by_key(
                    record.object_class) + " ===> " + str(record.accuracy))
            print("AVERAGE: " + str(average))

    def get_convolution_core_by_key(self, index):
        return str(self.convolution_cores[index])

    def get_object_class_by_key(self, index):
        return str(self.object_classes[index])
