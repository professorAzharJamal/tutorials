import random
from music21 import stream, note

# Define the range of musical notes
NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Define the genetic algorithm parameters
POPULATION_SIZE = 10
NUM_GENERATIONS = 20

# Function to generate a random musical sequence
def generate_random_sequence(length):
    return [random.choice(NOTES) for _ in range(length)]

# Function to evaluate the fitness of a musical sequence
def evaluate_fitness(sequence):
    # You can define your own fitness function based on musical rules or preferences
    # For simplicity, let's just return a random fitness score
    return random.random()

# Function to perform selection based on fitness scores
def selection(population, scores):
    return random.choices(population, weights=scores, k=2)

# Function to perform crossover between two sequences
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation on a sequence
def mutation(sequence):
    mutation_point = random.randint(0, len(sequence) - 1)
    new_note = random.choice(NOTES)
    sequence[mutation_point] = new_note
    return sequence

# Function to convert a musical sequence to a music21 stream
def sequence_to_stream(sequence):
    music_stream = stream.Stream()
    for note_name in sequence:
        if note_name != ' ':
            new_note = note.Note(note_name)
            music_stream.append(new_note)
    return music_stream

# Function to export a music21 stream to a MIDI file
def export_to_midi(music_stream, file_name):
    file_path = f"{file_name}.mid"
    music_stream.write('midi', fp=file_path)
    print(f"Music file '{file_path}' has been created.")

# Main genetic algorithm loop
def genetic_algorithm():
    # Initialize the population
    population = [generate_random_sequence(8) for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation + 1}:")
        
        # Evaluate the fitness of each sequence in the population
        fitness_scores = [evaluate_fitness(sequence) for sequence in population]

        # Select parents based on fitness scores and perform crossover
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = selection(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([child1, child2])

        # Perform mutation on the new population
        population = [mutation(sequence) for sequence in new_population]

        # Print the best sequence in the current generation
        best_sequence = max(population, key=evaluate_fitness)
        print("Best sequence:", ' '.join(best_sequence))
        print("Fitness score:", evaluate_fitness(best_sequence))
        print()

        # Convert the best sequence to music21 stream and export it to a MIDI file
        best_music_stream = sequence_to_stream(best_sequence)
        export_to_midi(best_music_stream, file_name=f"generation_{generation + 1}")

if __name__ == "__main__":
    genetic_algorithm()
