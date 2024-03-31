import random
import numpy as np
from scipy.io.wavfile import write

# Define the notes and durations
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
durations = [0.25, 0.5, 1.0]

# Define the length of the melody
melody_length = 16

# Function to generate a random melody
def generate_melody():
    return [(random.choice(notes), random.choice(durations)) for _ in range(melody_length)]

# Function to evaluate the fitness of a melody
def evaluate_fitness(melody):
    # Fitness can be based on certain musical rules or subjective preference
    # Here, we'll just sum up the MIDI values of notes
    fitness = sum(ord(note) for note, _ in melody)
    return fitness

# Function to perform crossover between two melodies
def crossover(melody1, melody2):
    crossover_point = random.randint(0, len(melody1) - 1)
    return melody1[:crossover_point] + melody2[crossover_point:]

# Function to perform mutation on a melody
def mutate(melody, mutation_rate=0.1):
    mutated_melody = []
    for note, duration in melody:
        if random.random() < mutation_rate:
            mutated_melody.append((random.choice(notes), random.choice(durations)))
        else:
            mutated_melody.append((note, duration))
    return mutated_melody

# Function to select parents based on their fitness
def select_parents(population, num_parents):
    sorted_population = sorted(population, key=lambda x: evaluate_fitness(x), reverse=True)
    return sorted_population[:num_parents]

# Function to generate initial population
def generate_initial_population(population_size):
    return [generate_melody() for _ in range(population_size)]

# Function to generate waveform for a note
def generate_waveform(note, duration, fs=44100):
    frequencies = {'C': 261.63, 'D': 293.66, 'E': 329.63, 'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.88}
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequencies[note] * t)
    return waveform

# Function to generate .wav file from melody
def generate_wav_file(melody, filename='output.wav', tempo=120, fs=44100):
    melody_waveform = np.array([], dtype=np.float32)
    for note, duration in melody:
        note_waveform = generate_waveform(note, duration * 60 / tempo)
        melody_waveform = np.concatenate((melody_waveform, note_waveform))
    write(filename, fs, melody_waveform)

# Main Genetic Algorithm
population_size = 10
num_generations = 100

# Generate initial population
population = generate_initial_population(population_size)

# Evolution loop
for generation in range(num_generations):
    # Select parents
    parents = select_parents(population, 2)
    
    # Perform crossover
    child = crossover(parents[0], parents[1])
    
    # Perform mutation
    child = mutate(child)
    
    # Replace worst melody in population with the child
    population.append(child)
    population = sorted(population, key=lambda x: evaluate_fitness(x), reverse=True)[:population_size]

# Generate .wav file from the best melody
best_melody = max(population, key=lambda x: evaluate_fitness(x))
generate_wav_file(best_melody)
