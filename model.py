import numpy as np

class MockModel:
    """
        This is just a mock.
        For a submission, you would normally use a foolbox wrapped model here,
        based on your framework of choice.
        For more details, have a look here:
        https://foolbox.readthedocs.io/en/latest/modules/models.html
    """

    def channel_axis(self):
        return 1

    def predictions(self, images):
        lower_bound = 0
        upper_bound = self.num_classes()
        return np.random.randint(lower_bound, upper_bound)

    def bounds(self):
        return (0, 255)

    def num_classes(self):
        # Assuming TinyImagenet
        return 200



def create_mock_model():
    net = MockModel()
    return net
