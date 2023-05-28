from typing import Callable

import numpy as np


class Spiral():
    """
    Example:
        >>>spiral = Spiral()
        >>>
        >>>N = 10000
        >>>original_domain = np.random.random(N)
        >>>altered_domain = spiral.alter_samples(original_domain)
        >>>original_image = spiral(domain)
        >>>normalized_image = spiral(original_image)
        >>>original_length = spiral.length_at_input(domain)
        >>>normalized_length = spiral.length_at_input(altered_domain)
    """

    def __init__(self, 
                 initial_angle:float=0., 
                 angular_frequency:float=2*np.pi, 
                 t_max:float=2*np.pi, 
                 *args, **kwargs):
        self.initial_angle = initial_angle
        self.angular_frequency = angular_frequency
        self.t_max = t_max
        self.length = self.length_at_input(self.t_max)
        self.domain = [0, self.t_max]

    def __call__(self, t, *args, **kwargs):
        x = t*np.cos(t*self.angular_frequency + self.initial_angle)
        y = t*np.sin(t*self.angular_frequency + self.initial_angle)
        return np.stack([x,y], axis=-1)

    def sample_normalized(self, num_samples):
        samples = self.t_max*np.random.random(num_samples)
        altered_samples = self.alter_samples(samples)
        return self(altered_samples)

    def alter_samples(self, samples):
        alterd_samples = np.array([self.input_at_length(self.length/self.t_max*sample) for sample in samples])
        return alterd_samples

    def length_at_input(self, t):
        a = self.angular_frequency
        return 1/2*t*(np.sqrt(1+(a*t)**2))+1/(2*a)*np.log(a*t+np.sqrt(1+(a*t)**2))

    def input_at_length(self, l: float) -> float:
        return self._inv_value(self.length_at_input, target_value=l, min_guess=0, max_guess=self.t_max)

    @staticmethod
    def _inv_value(f: Callable, target_value: float, min_guess: float, max_guess: float, num_guesses: int = 50) -> float:
        x_guess = (max_guess + min_guess)/2
        for _ in range(num_guesses):
            guess_value = f(x_guess)
            if guess_value < target_value:
                min_guess = x_guess
                x_guess = (max_guess + x_guess)/2
            else:
                max_guess = x_guess
                x_guess = (min_guess + x_guess)/2

        return x_guess
